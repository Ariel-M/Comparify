import os
import jinja2
import webapp2
import requests
import requests_toolbelt.adapters.appengine

requests_toolbelt.adapters.appengine.monkeypatch()


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)




class WalmartApi(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_env.get_template('index.html')
        call_walmart_api = requests.get('http://api.walmartlabs.com/v1/search?apiKey={t29nkcuug33kqst5r2b53d9z}&query=ipod')
        return call_walmart_api

app = webapp2.WSGIApplication([
    ('/', WalmartApi)
   
], debug=True)