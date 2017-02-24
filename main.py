import webapp2
import os
from google.appengine.ext.webapp import template


class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, {}))

class VolunteerPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'volunteer_form.html')
        self.response.out.write(template.render(path, {}))

    def post(self):
        path = os.path.join(os.path.dirname(__file__), 'thanks.html')
        self.response.out.write(template.render(path, {}))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/volunteer', VolunteerPage),
], debug=True)
