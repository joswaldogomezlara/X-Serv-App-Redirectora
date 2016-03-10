#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp

class redirectionApp(webapp.webApp):

    Counter = 0

    def parse(self, request):

        header = request.split(" ")[0]
        resource = request.split(" ")[1]

        return [header, resource]

    def process(self, parsedRequest):

        if parsedRequest[0] == 'GET' and parsedRequest[1] == '/favicon.ico':

            returnCode = '200 OK'
            htmlAnswer = ''

        elif parsedRequest[0] == 'GET' and parsedRequest[1] != '/':

            returnCode = '301 Moved Permanently\r\nLocation: http://localhost:1234'
            htmlAnswer = ''

        else:

            self.Counter = self.Counter + 1;

            returnCode = '200 OK'
            htmlAnswer = (  '<html><body><p>' +
                            'Las veces que has pasado por la pagina principal son:' +
                            '</p>' +
                            str(self.Counter) +
                            '</body></html>')                      

        return (returnCode, htmlAnswer)

if __name__ == "__main__":
    testWebApp = redirectionApp("localhost", 1234)
