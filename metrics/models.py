from django.db import models


class UserVideoMetric(models.Model):
    media_id = models.IntegerField(blank=False)
    user_id = models.IntegerField(blank=False)
    date = models.DateField(blank=False, auto_now_add=True)
    last_ping = models.DateTimeField(auto_now=True)
    seconds_played = models.IntegerField(default=0)
    play_count = models.IntegerField(default=1)  # it gets created on the first play

    class Meta:
        unique_together = ('media_id', 'user_id', 'date')
