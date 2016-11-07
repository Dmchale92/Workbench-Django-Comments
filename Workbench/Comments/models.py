from django.db import models

class Comment(models.Model):
	comment = models.TextField(unique_for_date="created")
	content_url = models.SlugField()
	created = models.DateTimeField(auto_now_add=True)
	ip_address = models.GenericIPAddressField()
	username = models.CharField(max_length=100)

	class Meta:
		ordering = ('created',)