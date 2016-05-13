from django.db import models
from django.utils import timezone

class Image(models.Model):
	slug = models.SlugField(max_length=50)
	title = models.CharField(max_length=200)
	upload = models.ImageField(upload_to='media/uploads')
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/image/%s" % (self.news_date.strftime('%Y%m%d') + '-' + str(self.id))