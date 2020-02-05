#!/usr/bin/venv python
# -*- coding: UTF-8 -*-

import cherrypy


class Home(object):
    @cherrypy.expose
    def index(self):
        return open("home/index.html")



