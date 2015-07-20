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

    def __str__(self):
        return "V{0} U{1} D{2.year}/{2.month}/{2.day} C{3}".format(
            self.media_id, self.user_id, self.date, self.seconds_played)
