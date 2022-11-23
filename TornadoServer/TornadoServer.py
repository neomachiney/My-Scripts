import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define('port', default=8888, help="run on given port")

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        get_data = self.get_argument('data')
        headers = self.request.headers
        self.set_cookie('bug-bounty', get_data)
        self.set_header('X-Requested-With', get_data)
        self.write("Hello Index: " + get_data)

    def post(self):
        pass

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        pass

tornado.options.parse_command_line()
app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(options.port)
tornado.ioloop.IOLoop.current().start()
