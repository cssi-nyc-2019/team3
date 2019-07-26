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

from google.appengine.ext import ndb 

	
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

class SurveyHandler(webapp2.RequestHandler):
	def get(self):
		start_template=jinja_current_directory.get_template("/survey.html")
		self.response.write(start_template.render())

class ResultsHandler(webapp2.RequestHandler):
	def post(self):
		results_template = jinja_current_directory.get_template("/results.html")
		#survey results 
		ans1 = self.request.get('q1')
		ans2 = self.request.get('q2')
		ans3 = self.request.get('q3')
		imput = "empty"

		if ans1 == "Home" and ans2 == "Home" and ans3 == "Home":
			imput = "Check out the home section!"
		elif ans1 == "Home" and ans2 == "Kids" and ans3 == "Jobs":
			imput = "Check out the jobs section!"
		elif ans1 == "Kids" and ans2 == "Home" and ans3 == "Kids":
			imput = "Check out the Kids section!"
		elif ans1 == "Gaming" and ans2 == "Jobs" and ans3 == "Jobs":
			imput = "Check out the gaming section!"
		elif ans1 == "Home" and ans2 == "Jobs" and ans3 == "Jobs":
			imput = "Check out the gaming section!"
		elif ans1 == "Home" and ans2 == "Gaming" and ans3 == "Jobs":
			imput = "Check out the jobs section!"
		elif ans1 == "Home" and ans2 == "Gaming" and ans3 == "Jobs":
			imput = "Check out the gaming section!"
		elif ans1 == "Kids" and ans2 == "Jobs" and ans3 == "Kids":
			imput = "Check out the Kids section!"
		elif ans1 == "Home" and ans2 == "Gaming" and ans3 == "Jobs":
			imput = "Check out the gaming section!"
		elif ans1 == "Jobs" and ans2 == "Jobs" and ans3 == "Jobs":
			imput = "Check out the job section!"
		elif ans1 == "Gaming" and ans2 == "Gaming"and ans3 == "Gaming":
			imput ="Check out the gaming section!"
		elif ans1 == "Kids" and ans2 == "Kids" and ans3 == "Kids":
			imput = "Check out the kids section!"
		else:
			imput="Other conditions didn't match"
		self.response.write(results_template.render({"return":imput}))

# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ('/kids', KidsHandler),
  ('/game', GamingHandler),
  ('/jobs', JobHandler),
  ('/home', HomeHandler),
  ('/survey', SurveyHandler),
  ('/results', ResultsHandler),
  ], debug=True)
