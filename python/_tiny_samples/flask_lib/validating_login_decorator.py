# validating_login_decorator.py
# --------------------------
# Updated: cramos 14/oct/2022
# This is a simple example to shows how to use decorators and *args 
# to validate whether a user is logged in or not

# For testing:
#   1. Comment / uncomment line 31
#   2. Call using:
#         python validationg_login_decorator.py

class User:
	def __init__(self, name):
		self.name = name
		self.is_logged_in = False

def is_authenticated_decorator(function):
	def wrapper(*args, **kargs):
		if args[0].is_logged_in == True:
			function(args[0])
		else:
			print(f"Error: User is not logged in...")

	return wrapper

@is_authenticated_decorator
def create_blog_post(user):
	print(f"This is {user.name}'s new blog post.")

new_user = User("maria")
# Comment/uncomment next line for see how result changes
#new_user.is_logged_in = True

# Note that invoking "create_blog_post" now performs an "aggregated"
# validation function (thanks to decorator wrapper)
create_blog_post(new_user)
