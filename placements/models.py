__author__ = 'rresol'
__email__  = 'shashank.kumar.apc13@itbhu.ac.in'

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
																																																																																																																																																																																																																																																																																																																	
#This model is to register students.
@python_2_unicode_compatible
class StudentRegister(models.Model):
	user = models.OneToOneField(User)

	roll_no = models.CharField(max_length=20)
	branch  = models.CharField(max_length=50)

	
	def __str__(self):
		return self.user.username


