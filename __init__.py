import os
import cherrypy

from api.v1.interface import ApiV1
from home import Home

PATH = os.path.abspath(os.path.dirname(__file__))
config = {
    'global': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': PATH,
        # 'server.socket_host' : '192.168.1.154',
        # 'server.socket_host' : '192.168.90.52',
        'server.socket_host' : '127.0.0.1',
        'server.socket_port' : 9090,
        'log.screen': True,
        'log.error_file': "/tmp/cherrypy.error",
        'log.access_file': "/tmp/cherrypy.access"
    },
}
api_config = {
    '/': {
        # 'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tools.json_out.on' : True,
    },
}
conf = {
    '/': {
        "tools.staticdir.on": True,
        "tools.staticdir.dir": PATH,
    },
}

# http://192.168.1.154:9090/api/v1/sensor?id=1
cherrypy.tree.mount(Home(), '/', conf)
cherrypy.tree.mount(ApiV1(), '/api/v1', api_config)

cherrypy.config.update(config)

cherrypy.engine.start()
cherrypy.engine.block()
