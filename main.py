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




class ApiHandler(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_env.get_template('index.html')
        call_walmart_api = requests.get('http://api.walmartlabs.com/v1/search?apiKey=t29nkcuug33kqst5r2b53d9z&query=ipod')
        walmart_json = call_walmart_api.json()
        walmart_upc = int(walmart_json[u'items'][1][u'upc'])
        
        walmart_item_api = requests.get('http://api.walmartlabs.com/v1/items?apiKey=t29nkcuug33kqst5r2b53d9z&upc=%s' % (walmart_upc))
        walmart_item_json = walmart_item_api.json()
         

        ebay_item_api = requests.get('http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByProduct&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=ScottMos-Comparif-PRD-1ed499e41-3b97c9fb&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&paginationInput.entriesPerPage=2&productId.@type=UPC&productId=%s' % (walmart_upc))
        ebay_item_json = ebay_item_api.json()
        self.response.write(ebay_item_json)

        

app = webapp2.WSGIApplication([
    ('/', ApiHandler)
   
], debug=True)