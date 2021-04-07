import React from "react";
import MapWrapper from "./components/maps/MapWrapper";

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
