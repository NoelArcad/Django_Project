from django.db import models
from django.core.exceptions import ValidationError

class Task(models.Model):
    name_task = models.CharField(null=True, max_length=255)
    des_task = models.CharField(required=False, null=True, max_length=455)
    start_date_task = models.DateField(null=True)
    start_time_task = models.TimeField(null=True)
    end_date_task = models.DateField(required=False, null=True)
    end_time_task = models.TimeField(required=False, null=True)
    statut_task = models.CharField(null=True, max_length=255)

    def validation_task(self):
        if self.start_date_task and self.end_date_task and self.start_time_task and self.end_time_task:
            if self.start_date_task < self.end_date_task or (self.start_date_task == self.end_date_task and self.start_time_task < self.end_time_task):
                return True
        return True

    def save(self, *args, **kwargs):
        if not self.validation_task():
            raise ValidationError('La validation de la tâche a échoué.')
        super().save(*args, **kwargs)

