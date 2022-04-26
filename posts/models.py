from pydoc import describe
from django.db import models
from core import models as core_models
from clubs import models as clubs_models
from users import models as users_models 

class Post(core_models.AbstractTimeStampedModel):
    editer = models.ForeignKey(users_models.User, on_delete=models.CASCADE, related_name="posts")
    club = models.ForeignKey(clubs_models.Club, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=150)
    review = models.TextField()
    stars = models.ManyToManyField(users_models.User, blank=True, related_name="stars")

    def count_stars(self):
        return self.stars.count()

    def __str__(self):
        return f'title : {self.title} / editer : {self.editer} / stars : {self.count_stars()}'


class Photo(core_models.AbstractTimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(upload_to="posts/photo", blank=True, null=True)
    caption = models.CharField(max_length=100)
