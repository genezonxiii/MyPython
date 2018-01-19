# -*- coding: utf-8 -*-
# __author__ = '10507001'
#! /usr/bin/env python

import web

urls = ("/sample/(.*)", "SFSample")

app = web.application(urls, globals())


class SFSample():

    def POST(self, data):
        return """Hello World! (POST)"""

    def GET(self, data):
        return """Hello World! (GET)"""


if __name__ == "__main__":
    app.run()
