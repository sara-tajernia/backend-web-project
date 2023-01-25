from django.db import models
from django.db.models.deletion import CASCADE


class EndpointAdd(models.Model):
    url = models.CharField(max_length=100)
    # user_id foreign key authen.models.User
    user_id = models.ForeignKey('authen.User', on_delete=CASCADE)
    threshold = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(blank=True,null=True)
    failed_times=models.IntegerField(default=0)

    def __str__(self):
        return self.name
