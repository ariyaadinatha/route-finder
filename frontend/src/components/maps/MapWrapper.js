// source : https://taylor.callsen.me/using-openlayers-with-react-functional-components/
// accessed on April 4 2021, 22:26 WIB

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
  adjacencyMatrixToLineFeature,
  nodesToPointsFeature,
} from "../../util/OpenLayersFeatures";
import NodesList from "../graph/NodesList";
import AdjacencyMatrix from "../matrix/AdjacencyMatrix";
import {
  addNodeToMatrix,
  addVertexToMatrix,
  deleteNodeFromMatrix,
} from "../../util/AdjacencyMatrix";
import SelectNode from "../graph/SelectNode";
import Submit from "./Submit";
import Result from "./Result";
import FileInput from "./FIleInput";

const itbLat = -6.890282;
const itbLng = 107.6104;

function MapWrapper(props) {
  const [map, setMap] = useState();
  const [featuresLayer, setFeaturesLayer, featuresLayerRef] = useState();
  const [selectedCoord, setSelectedCoord] = useState();
  const [nodes, setNodes, nodesRef] = useState([]);
  const [nodeNum, setNodeNum, nodeNumRef] = useState(0);
  const [adjMatrix, setAdjMatrix, adjMatrixRef] = useState([]);

  const [nodeStart, setNodeStart, nodeStartRef] = useState("");
  const [nodeDestination, setNodeDestination, nodeDestinationtRef] = useState(
    ""
  );

  const [result, setResult] = useState({});

  const mapElement = useRef();

  const mapRef = useRef();
  mapRef.current = map;

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
        zoom: 16,
      }),
      controls: [new Zoom()],
    });

    // set map onclick handler
    initialMap.on("click", handleMapClick);

    // save map and vector layer references to state
    setMap(initialMap);
    setFeaturesLayer(initalFeaturesLayer);
  }, []);

  // map click handler
  const handleMapClick = (event) => {
    // get clicked coordinate using mapRef to access current React state inside OpenLayers callback
    //  https://stackoverflow.com/a/60643670
    const clickedCoord = mapRef.current.getCoordinateFromPixel(event.pixel);

    // transform coord to EPSG 4326 standard Lat Long
    const transormedCoord = transform(clickedCoord, "EPSG:3857", "EPSG:4326");
    setSelectedCoord(transormedCoord);
    handleAddNode(transormedCoord[0], transormedCoord[1]);

    // add node to adjacency matrix
    const newAdjMat = addNodeToMatrix(adjMatrixRef.current);
    setAdjMatrix(newAdjMat);

    // set features to map
    const lineFeatures = adjacencyMatrixToLineFeature(
      adjMatrixRef.current,
      nodesRef.current
    );
    const pointFeatures = nodesToPointsFeature(nodesRef.current);
    const features = [...lineFeatures, ...pointFeatures];

    featuresLayerRef.current.setSource(
      new VectorSource({
        features: features,
      })
    );

    // reset selected nodes
    setNodeStart("");
    setNodeDestination("");
  };

  const handleDeleteNodeAtIndex = (index) => {
    const newNodes = nodes.filter((_, i) => index !== i);
    setNodes(newNodes);

    // delete the node from matrix
    const newAdjMat = deleteNodeFromMatrix(adjMatrix, index);
    setAdjMatrix(newAdjMat);

    // set features to map
    const lineFeatures = adjacencyMatrixToLineFeature(
      adjMatrixRef.current,
      nodesRef.current
    );
    const pointFeatures = nodesToPointsFeature(nodesRef.current);
    const features = [...lineFeatures, ...pointFeatures];

    featuresLayerRef.current.setSource(
      new VectorSource({
        features: features,
      })
    );

    // reset selected nodes
    setNodeStart("");
    setNodeDestination("");
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

  const addVertex = (i, j) => {
    setAdjMatrix(addVertexToMatrix(adjMatrix, i, j));

    const lineFeatures = adjacencyMatrixToLineFeature(adjMatrix, nodes);
    const pointFeatures = nodesToPointsFeature(nodes);
    const features = [...lineFeatures, ...pointFeatures];

    featuresLayerRef.current.setSource(
      new VectorSource({
        features: features,
      })
    );
  };

  return (
    <>
      <div className="container">
        <div className="mb-5">
          <FileInput
            setAdjMatrix={setAdjMatrix}
            setNodes={setNodes}
            featuresLayerRef={featuresLayerRef}
          />
        </div>
        <div className="map-top d-flex mb-5">
          <div ref={mapElement} className="map-container"></div>
          <div className="adj-container w-50 ml-5">
            <AdjacencyMatrix
              adjMatrix={adjMatrix}
              handleToggleElement={addVertex}
            />
          </div>
        </div>

        <div className="mb-5">
          <NodesList
            nodes={nodes}
            handleDeleteNodeAtIndex={handleDeleteNodeAtIndex}
          />
        </div>
        <div className="mb-5">
          <SelectNode
            nodes={nodes}
            setNodeStart={setNodeStart}
            setNodeDestination={setNodeDestination}
          />
        </div>

        <div className="mb-5">
          <Submit
            nodeStart={nodeStart}
            nodeDestination={nodeDestination}
            nodes={nodes}
            adj={adjMatrix}
            setResult={setResult}
          />
        </div>

        {result?.error === true || result?.error === false ? (
          <div className="mb-5">
            <Result result={result} nodes={nodes} />
          </div>
        ) : (
          <div></div>
        )}
      </div>

      <style>
        {`
          .map-container {
            height: 65vh;
            width: 50%;
          }
        `}
      </style>
    </>
  );
}

export default MapWrapper;
