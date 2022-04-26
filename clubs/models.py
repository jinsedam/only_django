from django.db import models
from core import models as core_models
from users import models as users_models

class Category(core_models.AbstractItemModel):
    pass

class Tag(core_models.AbstractItemModel):
    pass

class City(core_models.AbstractItemModel):
    pass

class Club(core_models.AbstractTimeStampedModel):
    """ Club Model """
    master = models.ForeignKey(users_models.User, on_delete=models.CASCADE, related_name="created_clubs")
    members = models.ManyToManyField(users_models.User, blank=True, related_name="joined_clubs")
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=50)
    meeting_start = models.TimeField()
    meeting_end = models.TimeField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def count_members(self):
        return self.members.count()

    def __str__(self):
        return f'name : {self.name} / master : {self.master} / members : {self.count_members()}'

class Photo(core_models.AbstractTimeStampedModel):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(upload_to="clubs/photo", blank=True, null=True)
    caption = models.CharField(max_length=100)

