from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_save
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='images/',default='v1638348565/owuk4syvculcljuzdron.jpg')
    bio = models.TextField(default="your bio here!")
    updated_at = models.DateTimeField(auto_now=True)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    sitename = models.CharField(max_length=50)
    desc = HTMLField()
    post_date = models.DateTimeField(default=timezone.now)
    image1 = models.ImageField(upload_to='projects/')
    link = models.CharField(max_length=70)


    def __str__(self):
        return self.sitename

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def search_by_name(cls, search_term):
        got_projects = Post.objects.filter(name__icontains=search_term)
        return got_projects    

class Rating(models.Model):
    RATINGS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    usability_rating = models.IntegerField(default=0, choices=RATINGS, null=True)
    design_rating = models.IntegerField(default=0, choices=RATINGS, null=True)
    content_rating = models.IntegerField(default=0, choices=RATINGS, null=True)
    review = models.CharField(max_length=200)

    def __str__(self):
        return self.review

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()
