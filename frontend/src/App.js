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
  return (
    <>
      <div className="App pt-3">
        <div className="title text-center mb-5">
          <h1>Route Finder</h1>
          <h4>Route / path finder app using the A* algorithm</h4>
        </div>

        <MapWrapper />
      </div>
      <style>
        {`
          .App {
            background: #98D2EB;
            height: 100%;          
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;
          }

          .title {
            color: #111B1E;
          }

          .title h1 {
            font-size: 5rem;
          }
          
        `}
      </style>
    </>
  );
}

export default App;
