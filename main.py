# the import section
import webapp2
import jinja2
import os

# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
jinja_current_directory = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file

# the handler section
class MainHandler(webapp2.RequestHandler):
	def get(self):  # for a get request
		start_template=jinja_current_directory.get_template("/index.html")
		self.response.write(start_template.render())
class KidsHandler(webapp2.RequestHandler):
	def get(self):
		start_template=jinja_current_directory.get_template("/kids.html")
		self.response.write(start_template.render())
class GamingHandler(webapp2.RequestHandler):
	def get(self):
		start_template=jinja_current_directory.get_template("/game.html")
		self.response.write(start_template.render())
class JobHandler(webapp2.RequestHandler):
	def get(self):
		start_template=jinja_current_directory.get_template("/job.html")
		self.response.write(start_template.render())
class HomeHandler(webapp2.RequestHandler):
	def get(self):
		start_template=jinja_current_directory.get_template("/home.html")
		self.response.write(start_template.render())

# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ('/kids.html', KidsHandler),
  ('/game.html', GamingHandler),
  ('/job.html', JobHandler),
  ('/home.html', HomeHandler),
  ], debug=True)