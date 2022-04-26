from django.db import models
from core import models as core_models
from users import models as users_models
from posts import models as posts_models

class Comment(core_models.AbstractTimeStampedModel):
    post = models.ForeignKey(posts_models.Post, on_delete=models.CASCADE, related_name="comments")
    editer = models.ForeignKey(users_models.User, on_delete=models.CASCADE, related_name="commnets")
    comment = models.TextField()

    def __str__(self):
        return f'{self.editer} : {self.comment}'

