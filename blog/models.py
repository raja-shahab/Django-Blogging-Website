from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def edit(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image
        self.save()

    def short_description(self):
        words = self.description.split()

        if len(words) > 50:
            return ''.join(words[:30]) + '...'
        else:
            return self.description
