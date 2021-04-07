import React, { useEffect, useRef } from "react";
import useState from "react-usestateref";

import Map from "ol/Map";
import View from "ol/View";
import TileLayer from "ol/layer/Tile";
import VectorLayer from "ol/layer/Vector";
import VectorSource from "ol/source/Vector";
import XYZ from "ol/source/XYZ";
import { transform, fromLonLat } from "ol/proj";
import Zoom from "ol/control/Zoom";

import {
  pathArrayToLineFeature,
  pathArrayToPointFeature,
} from "../../util/OpenLayersFeatures";

const itbLat = -6.890282;
const itbLng = 107.6104;

const Result = (props) => {
  const { result, nodes } = props;
  const [map, setMap] = useState();
  const mapElement = useRef();

  const [featuresLayer, setFeaturesLayer, featuresLayerRef] = useState();

  useEffect(() => {
    // create and add vector source layer
    const initalFeaturesLayer = new VectorLayer({
      source: new VectorSource(),
    });

    // create map
    const initialMap = new Map({
      target: mapElement.current,
      layers: [
        // Google Maps Terrain
        new TileLayer({
          source: new XYZ({
            url: "http://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}",
          }),
        }),

        initalFeaturesLayer,
      ],
      view: new View({
        projection: "EPSG:3857",
        center: fromLonLat([itbLng, itbLat]),
        zoom: 14,
      }),
      controls: [new Zoom()],
    });
    // save map and vector layer references to state
    setMap(initialMap);
    setFeaturesLayer(initalFeaturesLayer);
  }, []);

  useEffect(() => {
    if (!result?.error) {
      const lineFeatures = pathArrayToLineFeature(result.path, nodes);
      const pointFeatures = pathArrayToPointFeature(result.path, nodes);
      const features = [...lineFeatures, ...pointFeatures];

      featuresLayerRef.current.setSource(
        new VectorSource({
          features: features,
        })
      );
    }
  }, [result]);
  return (
    <div>
      <div>
        <h3 className="mb-4 text-center result-title">Path Result</h3>
      </div>

      {!result?.error ? (
        <div>
          <h5>Jarak lintasan: {result.gn} KM</h5>
          <div ref={mapElement} className="map-result"></div>
        </div>
      ) : (
        <div className="text-center">
          <h4>Path not found</h4>
        </div>
      )}

      <style>
        {`
            .result-title {
                background: #B98389;
                color: #E4DBD9;
                padding: .5rem 1rem;
                border-radius: 7px; 
            }
            .map-result {
                height: 65vh;
                width: 100%;
            }
          `}
      </style>
    </div>
  );
};

export default Result;
