from django import forms 
from django.contrib.auth.models import User
from .models import StudentRegister


#Form for  registering the  Student User .
class StudentForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields= ('first_name','last_name','email','password','username')

#Form for including the additional field during student registration.
class StudentProfileForm(forms.ModelForm):
	class Meta:
		model = StudentRegister
		fields = ('roll_no','branch')
