import json
import click
import cligj

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        name = "YEEEEEE"
        self.write("""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset='utf-8' />
            <title></title>
            <meta name='viewport' content='initial-scale=1,maximum-scale=1,user-scalable=no' />
            <script src='https://api.tiles.mapbox.com/mapbox-gl-js/v0.53.0/mapbox-gl.js'></script>
            <link href='https://api.tiles.mapbox.com/mapbox-gl-js/v0.53.0/mapbox-gl.css' rel='stylesheet' />
            <style>
                body { margin:0; padding:0; }
                #map { position:absolute; top:0; bottom:0; width:100%; }
            </style>
        </head>
        <body>

        <div id='map'></div>
        <script>
        mapboxgl.accessToken = 'pk.eyJ1IjoiZG5vbWFkYiIsImEiOiJjaW16aXFsZzUwNHJmdjdra3h0Nmd2cjY1In0.SqzkaKalXxQaPhQLjodQcQ';
        const map = new mapboxgl.Map({
            container: 'map', // container id
            style: 'mapbox://styles/mapbox/streets-v9', // stylesheet location
            center: [-74.50, 40], // starting position [lng, lat]
            zoom: 9 // starting zoom
        });
        map.on('load', () => {
            map.addLayer({
                'id': 'data',
                'type': 'fill',
                'source': {
                    'type': 'geojson',
                    'data': "data.geojson"
                },
                'layout': {},
                'paint': {
                    'fill-color': '#088',
                    'fill-opacity': 0.8
                }
            });
            })
        </script>

        </body>
        </html>
        """)

class DataHandler(tornado.web.RequestHandler):
    def initialize(self, geojson):
        self.geojson = geojson

    def get(self):
        print("HI")
        self.write(json.dumps(self.geojson))

# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()


# class MapboxGLGeoJSONServer:
#     """"""
#     def __init__(self, features):
#         self.features = {
#             "type": "FeatureCollection",
#             "features": features
#         }
#     @app.route("/data.geojson")
#     def get_features(self):
#         return json.dumps(self.features)



@click.command('fio mbxgl')
@click.pass_context
@cligj.features_in_arg
def cli(ctx, features):
    """Pipe in and preview GeoJSON"""
    app = tornado.web.Application([
            tornado.web.url(r"/", MainHandler),
            tornado.web.url(r"/data.geojson", DataHandler, dict(geojson={
                  "type": "FeatureCollection",
                  "features": list(features)}))
    ])

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    # MBXGL = MapboxGLGeoJSONServer(list(features))
    # app.run()

if __name__ == '__main__':
    cli()
