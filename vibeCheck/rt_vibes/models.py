from datetime import datetime as dt
from django.db import models


class RecordedVibe(models.Model):
    raw_sound = models.CharField(max_length=10)
    recording_date = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    recording_title = models.CharField(max_length=50)

    def __str__(self):
        return "{} recorded on {}".format(self.recording_title,
                                          self.recording_date.isoformat("/"))

