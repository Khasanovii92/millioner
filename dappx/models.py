from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
	user           = models.OneToOneField(User,on_delete=models.CASCADE)
	portfolio_site = models.URLField(blank=True)
	pack           = models.CharField(max_length=254)
	profit         = models.CharField(max_length=254)	
	# profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
	def __str__(self):
		return self.user.username