import cherrypy
from api.v1.sensors import Sensor_api
from api.v1.switchers import Switchers


class ApiV1(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def state(self):
        switcher = Switchers()
        return switcher.create_random_data()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def sens(self):
        sensors = Sensor_api()
        return sensors.create_random_data()