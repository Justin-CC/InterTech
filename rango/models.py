from django.db import models
from django.template.defaultfilters import slugify
from django.template.defaultfilters import truncatechars

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
    dish = models.ForeignKey("Dish", related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey("User", related_name="comments", on_delete=models.CASCADE)
    content = models.TextField(max_length=500)

    def __str__(self):
        return truncatechars(self.content, 30)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"



class Receive(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=500)
    email = models.EmailField()

    class Meta:
        verbose_name = "Receive"
        verbose_name_plural = "Receives"


    def __str__(self):
        return truncatechars(self.content, 30)


