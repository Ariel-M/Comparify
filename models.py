from google.appengine.ext import ndb

class SearchTerms(ndb.Model):
    search_term = ndb.StringProperty(required=True)
    search_frequency = ndb.IntegerProperty(required=True)
