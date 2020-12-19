from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	image = models.ImageField(upload_to='blog/images/', blank=True)
	date = models.DateField()

	def __str__(self):
		return self.title
