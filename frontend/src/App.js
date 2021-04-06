import React, { useEffect } from "react";
import useState from "react-usestateref";

// openlayers
import GeoJSON from "ol/format/GeoJSON";
import Feature from "ol/Feature";
import MapWrapper from "./components/maps/MapWrapper";
import NodesList from "./components/graph/NodesList";
import { nodesToPointsFeature } from "./util/OpenLayersFeatures";

// components

function App() {
  // set intial state
  const [features, setFeatures] = useState([]);

  const [num, setNum, numRef] = useState(0);

  const [nodes, setNodes, nodesRef] = useState([]);

  // // initialization - retrieve GeoJSON features from Mock JSON API get features from mock
  // //  GeoJson API (read from flat .json file in public directory)
  // useEffect(() => {
  //   fetch("/mock-geojson-api.json")
  //     .then((response) => response.json())
  //     .then((fetchedFeatures) => {
  //       // parse fetched geojson into OpenLayers features
  //       //  use options to convert feature from EPSG:4326 to EPSG:3857
  //       const wktOptions = {
  //         dataProjection: "EPSG:4326",
  //         featureProjection: "EPSG:3857",
  //       };
  //       const parsedFeatures = new GeoJSON().readFeatures(
  //         fetchedFeatures,
  //         wktOptions
  //       );

  //       // set features into state (which will be passed into OpenLayers
  //       //  map component as props)
  //       setFeatures(parsedFeatures);
  //     });
  // }, []);

  const handleAddNodeWithRef = (longitude, latitude) => {
    const newNode = {
      longitude,
      latitude,
    };
    const newNodes = nodesRef.current.concat(newNode);
    setNodes(newNodes);
  };

  const handleOnClickAdd = () => {
    setNum(num + 1);
  };

  const handleDeleteNode = () => {
    if (nodes.length > 0) {
      var newNodes = nodes;

      newNodes.pop();

      setNodes(newNodes);
    }
  };

  return (
    <div className="App">
      {/* {console.log(nodes)} */}
      <div className="app-label">
        <p>React Functional Components with OpenLayers Example</p>
        <p>Click the map to reveal location coordinate via React State</p>
      </div>
      {/* <p>{num}</p>
      <button onClick={handleOnClickAdd}>ADDDDDD</button>
      <button onClick={handleDeleteNode}>Delete node</button> */}
      {/* {console.log(nodesToPointsFeature(nodes))} */}

      <MapWrapper features={features} setNum={setNum} numRef={numRef} />
      {/* <NodesList nodes={nodes} /> */}
    </div>
  );
}

export default App;
