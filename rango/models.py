from django.db import models
from django.template.defaultfilters import slugify


# # Create your models here.
# 
class Dish(models.Model):
    # NAME_MAX_LENGTH = 128

    dishid = models.AutoField(primary_key=True)
    dishname = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    picture = models.CharField(max_length=500)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.dishname)
        self.picture = '/static/images/' + slugify(self.dishname).upper() + '.jpg'
        super(Dish, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.dishname


class User(models.Model):
    # TITLE_MAX_LENGTH = 128
    # URL_MAX_LENGTH = 200

    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.username


class Comment(models.Model):
    commentid = models.AutoField(primary_key=True)
    dish = models.ForeignKey("Dish", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commentid


class Contactus(models.Model):
    # TITLE_MAX_LENGTH = 128
    # URL_MAX_LENGTH = 200

    contactid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=1000)
    email = models.EmailField()

    def __str__(self):
        return self.name



