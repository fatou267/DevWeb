from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
#ce modele enregistre les donnees des utilisateurs
#class Inscription():



#ce modele enregistre les informations de connexion login et mdp
#class Connexion(object):

#ce modele enregistre les differentes articles crees
class Publication(models.Model):
	"""docstring for Articles"""
	acteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	titre = models.CharField(max_length=200)
	texte = models.TextField()
	date_creation = models.DateTimeField(default=timezone.now)
	date_publication = models.DateTimeField(blank=True, null=True)
	archive = models.BooleanField(default=False)
	def publication(self):
		date_publication = timezone.now
		self.save()
	def __str__(self):
		return self.titre
	
class Profile(models.Model):
	"""docstring for Profile"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)


		

		