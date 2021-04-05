var map;
// Koordinat ITB
var mapLng = 107.610400;
var mapLat = -6.890282;
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

    // format (lng, lat)
    map.on('click', function (evt) {
        var coor = ol.proj.toLonLat(evt.coordinate);
        console.log(coor[0]);
        console.log(coor[1]);
        //console.log(coor);
        // var coor1 = [107.60969191789626, -6.8896571064314855];
        // var coor2 = [107.61146217584607, -6.890908639963897];
        // drawLine(coor1,coor2);
        point(coor[0], coor[1]);
        // getGeocode(coor);
    });
}

// add point to map
function point(lng, lat) {
  var vectorLayer = new ol.layer.Vector({
    source:new ol.source.Vector({
      features: [new ol.Feature({
            geometry: new ol.geom.Point(ol.proj.transform([parseFloat(lng), parseFloat(lat)], 'EPSG:4326', 'EPSG:3857')),
        })]
    }),
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

// draw line between coord in map
function drawLine(coor1, coor2)
{
  var posisiAwal = ol.proj.fromLonLat(coor1);
  var posisiTujuan = ol.proj.fromLonLat(coor2);

  var style = [
    new ol.style.Style({
      stroke: new ol.style.Stroke({
      color: 'red',
      width: 3
      })
    })
    ];
          
  var lineDraw = new ol.layer.Vector({
      source: new ol.source.Vector({
      features: [new ol.Feature({
        geometry: new ol.geom.LineString([posisiAwal, posisiTujuan]),
        name: 'Line',
      })]
    })
  });
  
  lineDraw.setStyle(style);
  map.addLayer(lineDraw);
}
