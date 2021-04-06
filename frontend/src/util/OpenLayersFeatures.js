import GeoJSON from "ol/format/GeoJSON";
import Text from "ol/style/Text";
import Style from "ol/style/Style";
import { Circle, Fill } from "ol/style";

const getPointStyle = (feature) => {
  var style = new Style({
    text: new Text({
      placement: "point",
      font: 'bold 11px "Open Sans", "Arial Unicode MS", "sans-serif"',
      offsetY: -10,
    }),
    image: new Circle({
      fill: new Fill({ color: "black" }),
      radius: 4,
    }),
  });

  style.getText().setText(feature.get("name"));

  return style;
};

export const parseFeatureWithGeoJSON = (feature) => {
  const wktOptions = {
    dataProjection: "EPSG:4326",
    featureProjection: "EPSG:3857",
  };
  var parsedFeatures = new GeoJSON().readFeatures(feature, wktOptions);

  parsedFeatures.forEach((parsedFeature, i) => {
    const featureType = parsedFeature.getGeometry().constructor.name;

    if (featureType === "Point") {
      parsedFeature.set("name", feature.name);
      console.log(parsedFeature.get("name"));

      const pointStyle = getPointStyle(parsedFeature);
      parsedFeature.setStyle(pointStyle);
    }
  });

  //   console.log(parsedFeatures);

  return parsedFeatures;
};

export const nodesToPointsFeature = (nodes) => {
  var result = [];

  nodes.forEach((node) => {
    const feature = {
      type: "Point",
      coordinates: [node.longitude, node.latitude],
      name: node.name,
    };

    result = result.concat(parseFeatureWithGeoJSON(feature));
  });

  //   console.log(result);
  return result;
};

export const adjacencyMatrixToLineFeature = (matrix, nodes) => {
  var result = [];

  matrix.forEach((row, i) => {
    row.forEach((el, j) => {
      if (el === 1) {
        const feature = {
          type: "LineString",
          coordinates: [
            [nodes[i].longitude, nodes[i].latitude],
            [nodes[j].longitude, nodes[j].latitude],
          ],
        };

        result = result.concat(parseFeatureWithGeoJSON(feature));
      }
    });
  });

  return result;
};
