from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse


class TodoList(models.Model):
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)

    # FK
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo-update', args=[self.title])
