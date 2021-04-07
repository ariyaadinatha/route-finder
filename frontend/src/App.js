import React from "react";
import MapWrapper from "./components/maps/MapWrapper";

// components

function App() {
  return (
    <>
      <div className="App pt-3 container">
        <div className="title text-center mb-5">
          <h1>Route Finder</h1>
          <h4>Route / path finder app using the A* algorithm</h4>
          <h5>
            Route Finder dapat menerima input dari file ataupun langsung dari
            map-nya. Anda dapat mengclick titik di map untuk mengambil
            koordinat. Anda juga dapat menghapus koordinat yang sudah ambil pada
            nodes list. Aturlah rute dengan menggunakan adjacency matrix
          </h5>
          <br />
          <h5>
            Tugas ini dibuat oleh Nathaniel Jason (13519108) dan Ariya Adinatha
            (13519048)
          </h5>
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
