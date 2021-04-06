// source : https://taylor.callsen.me/using-openlayers-with-react-functional-components/
// accessed on April 4 2021, 22:26 WIB

// react
import React, { useEffect, useRef } from "react";
import useState from "react-usestateref";

// openlayers
import Map from "ol/Map";
import View from "ol/View";
import TileLayer from "ol/layer/Tile";
import VectorLayer from "ol/layer/Vector";
import VectorSource from "ol/source/Vector";
import XYZ from "ol/source/XYZ";
import { transform, fromLonLat } from "ol/proj";
import { toStringXY } from "ol/coordinate";
import Text from "ol/style/Text";
import Style from "ol/style/Style";
import Zoom from "ol/control/Zoom";

import OSM from "ol/source/OSM";
import {
  adjacencyMatrixToLineFeature,
  nodesToPointsFeature,
} from "../../util/OpenLayersFeatures";
import NodesList from "../graph/NodesList";
import { Circle, Fill } from "ol/style";
import AdjacencyMatrix from "../matrix/AdjacencyMatrix";
import {
  addNodeToMatrix,
  addVertexToMatrix,
  deleteNodeFromMatrix,
} from "../../util/AdjacencyMatrix";

const itbLat = -6.890282;
const itbLng = 107.6104;

function MapWrapper(props) {
  const { setNum, numRef } = props;

  // set intial state
  const [map, setMap] = useState();
  const [featuresLayer, setFeaturesLayer, featuresLayerRef] = useState();
  const [selectedCoord, setSelectedCoord] = useState();
  const [nodes, setNodes, nodesRef] = useState([]);
  const [nodeNum, setNodeNum, nodeNumRef] = useState(0);
  const [adjMatrix, setAdjMatrix, adjMatrixRef] = useState([]);

  const [arr, setArr] = useState([]);

  // pull refs
  const mapElement = useRef();

  // create state ref that can be accessed in OpenLayers onclick callback function
  //  https://stackoverflow.com/a/60643670
  const mapRef = useRef();
  mapRef.current = map;

  // initialize map on first render - logic formerly put into componentDidMount
  useEffect(() => {
    // const style = new Style({
    //   text: new Text({
    //     placement: "point",
    //     font: 'bold 11px "Open Sans", "Arial Unicode MS", "sans-serif"',
    //     offsetY: -10,
    //   }),
    //   image: new Circle({
    //     fill: new Fill({ color: "black" }),
    //     radius: 4,
    //   }),
    // });

    // const styleFunction = (feature) => {
    //   style.getText().setText(feature.get("name"));

    //   return style;
    // };

    // create and add vector source layer
    const initalFeaturesLayer = new VectorLayer({
      source: new VectorSource(),
    });

    // create map
    const initialMap = new Map({
      target: mapElement.current,
      layers: [
        // USGS Topo
        // new TileLayer({
        //   source: new XYZ({
        //     url:
        //       "https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}",
        //   }),
        // }),

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
        zoom: 16,
      }),
      controls: [new Zoom()],
    });

    // set map onclick handler
    initialMap.on("click", handleMapClick);

    // save map and vector layer references to state
    setMap(initialMap);
    setFeaturesLayer(initalFeaturesLayer);
    console.log(featuresLayer);
  }, []);

  // update map if features prop changes - logic formerly put into componentDidUpdate
  useEffect(() => {
    if (props.features.length) {
      // may be null on first render

      // set features to map
      featuresLayer.setSource(
        new VectorSource({
          features: props.features, // make sure features is an array
        })
      );

      // fit map to feature extent (with 100px of padding)
      map.getView().fit(featuresLayer.getSource().getExtent(), {
        padding: [100, 100, 100, 100],
      });
    }
  }, [props.features]);

  // map click handler
  const handleMapClick = (event) => {
    // get clicked coordinate using mapRef to access current React state inside OpenLayers callback
    //  https://stackoverflow.com/a/60643670
    const clickedCoord = mapRef.current.getCoordinateFromPixel(event.pixel);

    // transform coord to EPSG 4326 standard Lat Long
    const transormedCoord = transform(clickedCoord, "EPSG:3857", "EPSG:4326");

    setSelectedCoord(transormedCoord);

    handleAddNode(transormedCoord[0], transormedCoord[1]);

    // console.log(nodesToPointsFeature(nodesRef.current));

    // set features to map
    featuresLayerRef.current.setSource(
      new VectorSource({
        features: nodesToPointsFeature(nodesRef.current), // make sure features is an array
      })
    );

    // add node to adjacency matrix

    const newAdjMat = addNodeToMatrix(adjMatrixRef.current);
    setAdjMatrix(newAdjMat);

    // // fit map to feature extent (with 100px of padding)
    // mapRef.current.getView().fit(featuresLayer.getSource().getExtent(), {
    //   padding: [100, 100, 100, 100],
    // });

    // console.log(transormedCoord);
  };

  const handleDeleteNode = () => {
    if (nodes.length > 0) {
      const newNodes = nodes.splice(0, nodes.length - 1);

      setNodes(newNodes);

      featuresLayerRef.current.setSource(
        new VectorSource({
          features: nodesToPointsFeature(nodesRef.current), // make sure features is an array
        })
      );
    }
  };

  const handleDeleteNodeAtIndex = (index) => {
    const newNodes = nodes.filter((_, i) => index !== i);

    setNodes(newNodes);

    featuresLayerRef.current.setSource(
      new VectorSource({
        features: nodesToPointsFeature(nodesRef.current), // make sure features is an array
      })
    );

    // delete the node from matrix
    const newAdjMat = deleteNodeFromMatrix(adjMatrix, index);
    setAdjMatrix(newAdjMat);
  };

  const handleAddNode = (longitude, latitude) => {
    const newNode = {
      longitude,
      latitude,
      name: `node-${nodeNumRef.current}`,
    };
    const newNodes = nodesRef.current.concat(newNode);
    setNodeNum(nodeNumRef.current + 1);
    setNodes(newNodes);
  };

  // const addElArr = () => {
  //   const newArr = arr.concat(nodeNum);

  //   setNodeNum(nodeNum + 1);

  //   setArr(newArr);
  // };

  // const delElArr = () => {
  //   var newArr = [...arr];

  //   newArr[0] = 1000;

  //   setArr(newArr);
  // };

  const addVertex = (i, j) => {
    setAdjMatrix(addVertexToMatrix(adjMatrix, i, j));

    const lineFeatures = adjacencyMatrixToLineFeature(adjMatrix, nodes);
    const pointFeatures = nodesToPointsFeature(nodes);
    const features = [...lineFeatures, ...pointFeatures];

    console.log(features);

    featuresLayerRef.current.setSource(
      new VectorSource({
        features: features, // make sure features is an array
      })
    );
  };

  return (
    <>
      <div ref={mapElement} className="map-container"></div>
      <h1>{numRef.current}</h1>
      {/* <button onClick={handleDeleteNode}>delete node</button> */}
      <NodesList
        nodes={nodes}
        handleDeleteNodeAtIndex={handleDeleteNodeAtIndex}
      />
      <AdjacencyMatrix adjMatrix={adjMatrix} handleToggleElement={addVertex} />
      {/* <button onClick={addElArr}>Add el arr</button>
      <button onClick={delElArr}>DEL el arr</button>
      {arr.map((el) => {
        return <p>{`element ${el}`}</p>;
      })} */}

      <style>
        {`
          .map-container {
            height: 50vh;
            width: 50%;
          }
        `}
      </style>
    </>
  );
}

export default MapWrapper;
