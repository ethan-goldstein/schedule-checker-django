from django.db import models


class Course(models.Model):
    DAY_CHOICES = [
        ('MWF', 'Mon / Wed / Fri'),
        ('TR', 'Tue / Thu'),
        ('MW', 'Mon / Wed'),
        ('M', 'Mon'),
        ('T', 'Tue'),
        ('W', 'Wed'),
        ('R', 'Thu'),
        ('F', 'Fri'),
    ]

    code = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    days = models.CharField(max_length=3, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    credits = models.PositiveSmallIntegerField(default=3)

    def __str__(self):
        return f'{self.code} - {self.title}'

    def conflicts_with(self, other):
        # two classes conflict if they meet on the same day and their times overlap
        same_day = set(self.days) & set(other.days)
        overlap = self.start_time < other.end_time and other.start_time < self.end_time
        return bool(same_day) and overlap