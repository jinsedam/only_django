from django.db import models
from core import models as core_models
from users import models as users_models
from clubs import models as clubs_models
from posts import models as posts_models


class InterestingClubList(core_models.AbstractTimeStampedModel):
    user = models.ForeignKey(users_models.User, on_delete=models.CASCADE, related_name="InterestingClubList")
    interested = models.ManyToManyField(users_models.User, blank=True)
    clubs = models.ManyToManyField(clubs_models.Club, blank=True)

    def count_interested(self):
        return self.interested.count()


class InterestingPostList(core_models.AbstractTimeStampedModel):
    user = models.ForeignKey(users_models.User, on_delete=models.CASCADE, related_name="InterestingPostList")
    interested = models.ManyToManyField(users_models.User, blank=True)
    posts = models.ManyToManyField(posts_models.Post, blank=True)

    def count_interested(self):
        return self.interested.count()
