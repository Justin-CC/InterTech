from django.db import models
from django.template.defaultfilters import slugify

# # Create your models here.
# 
class Dish(models.Model):
    NAME_MAX_LENGTH = 128

    dishid = models.IntegerField(primary_key = True )
    dishname = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=500)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Category, self).save(*args, **kwargs)
    #
    # class Meta:
    #     verbose_name_plural = 'Categories'

    def __str__(self):
        return self.dishname

class User(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    userid = models.IntegerField(primary_key = True )
    username = models.CharField(max_length=10, unique=True)
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.username

class Comment(models.Model):


    commentid = models.IntegerField(primary_key = True )
    dish = models.ForeignKey("Dish", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.commentid


