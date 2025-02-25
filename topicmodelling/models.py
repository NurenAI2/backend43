from django.db import models
from simplecrm.models import CustomUser  # Import the necessary models
from communication.models import Conversation

class TopicModelling(models.Model):
    conversation = models.OneToOneField(
        Conversation,
        on_delete=models.CASCADE,
        unique=True,
        related_name='topic_modelling'
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='topic_modelling_entries'
    )
    topics = models.JSONField()  # Storing topics as JSON

    def __str__(self):
        return f"Topics for Conversation {self.conversation.conversation_id}"
