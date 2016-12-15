from __future__ import unicode_literals
from django.db import models
import re, bcrypt

passRegex = re.compile(r'^(?=.{8,15}$)(?=.*[A-Z])(?=.*[0-9]).*$')
emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
nameRegex = re.compile(r'^(?=.{2,})([a-zA-z]*)$')

class UserManager(models.Manager):

	def register(self, first_name, last_name, email, password, confirm_password ):
		errors = []
		if (len(first_name) == 0) or (len(last_name) == 0)  or (len(email) == 0) or (len(password) == 0):
			errors.append("Cannot be blank")

		elif (not emailRegex.match(email)) or (not nameRegex.match(first_name)) or (not nameRegex.match(last_name)) or (not passRegex.match(password)):
		# elif (not emailRegex.match(email)) or (not nameRegex.match(first_name)) or (not nameRegex.match(last_name)):
			errors.append("Invalid input")

		elif (not (password == confirm_password)):
			errors.append("Password don't match")


		if len(errors) is not 0:
			return (False, errors)
		else:
			pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			print pw_hash, "888888888888888"
			new_user = User.userMgr.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash)

		return (True, new_user)

	def login(self, email, password):
		errors =[]

		user = User.userMgr.filter(email=email)
		# This query returns as an array, should always be unwrapped/unzipped in order to access the objects in the array!

		if user:
			print user,"user exist"
			compare_password = password.encode()
			if bcrypt.hashpw(compare_password, user[0].password.encode()) == user[0].password:
			# if (user[0].password == password):
				print user[0].password,"That is your password"

				return (True, user)
			else:
				errors.append("password didnt match")
				print "password didnt match"
				return (False, errors)
		else:
			print "no email found"
			errors.append("No email found in our system, please register dude!!!")
			return (False, errors)

class User(models.Model):
	first_name = models.CharField(max_length=45, blank=True, null=True)
	last_name = models.CharField(max_length=45, blank=True, null=True)
	email = models.EmailField(max_length = 255)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userMgr = UserManager()


# class BookManager(models.Manager):


class Book(models.Model):
	book_title = models.CharField(max_length=255, null=True)
	author = models.CharField(max_length=45, null=True)
	review = models.TextField(max_length=1000, null=True)
	rating = models.TextField(max_length=5, null=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# user = models.ForeignKey(User)
	# objects = BookManager()

# class ReviewManager(models.Manager):


# class Review(models.Model):
# 	book = models.ForeignKey(Book)
# 	user = models.ForeignKey(User)
# 	created_at = models.DateTimeField(auto_now_add = True)
# 	updated_at = models.DateTimeField(auto_now = True)
# 	objects = ReviewManager()
