from django.db import models

# Create your models here.

class CategoryBlog(models.Model):
    class Meta:
        verbose_name_plural = "Category Blog"

    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    class Meta:
        verbose_name_plural = "Blog Model"

    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    category = models.ForeignKey(CategoryBlog, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save_slug(self):
        self.slug = self.title.replace(" ","-").lower()
    
    def save(self, *args, **kwargs):
        self.save_slug()
        super(Blog, self).save(*args, **kwargs)