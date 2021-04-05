var map;
// Koordinat ITB
var mapLat = -6.890282;
var mapLng = 107.610400;
var mapDefaultZoom = 18;

function initialize_map() {
    map = new ol.Map({
        target: "map",
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM()
            })
        ],
        view: new ol.View({
            center: ol.proj.fromLonLat([mapLng, mapLat]),
            zoom: mapDefaultZoom
        })
    });

    map.on('click', function (evt) {
        var coor = ol.proj.toLonLat(evt.coordinate);
        console.log(coor[1]);
        console.log(coor[0]);
        // point(coor[1], coor[0]);
        // getGeocode(coor);
    });
}

function point(lat, lng) {
  var vectorLayer = new ol.layer.Vector({
    style: new ol.style.Style({
      image: new ol.style.Icon({
        src: "https://upload.wikimedia.org/wikipedia/commons/d/d1/Google_Maps_pin.svg"
      })
    })
  });
  map.addLayer(vectorLayer); 
}

// dikerjain lagi kalau ada waktu
function getGeocode(coords) {
    fetch('http://nominatim.openstreetmap.org/reverse?format=json&lon=' + coords[0] + '&lat=' + coords[1])
      .then(function(response) {
             return response.json();
         }).then(function(json) {
             console.log(json);
         });
 }
