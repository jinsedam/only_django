from django.db import models
from core import models as core_models
from users import models as users_models

class Conversation(core_models.AbstractTimeStampedModel):
    members = models.ManyToManyField(users_models.User, blank=True, related_name="conversations")

    def __str__(self):
        return f"{self.updated}"
    
class Message(core_models.AbstractTimeStampedModel):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(users_models.User, on_delete=models.CASCADE, related_name="messages")
    message = models.TextField()

    def __str__(self):
        return f"{self.user} : {self.message}"