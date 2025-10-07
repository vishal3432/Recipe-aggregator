from django.db import models
from django.contrib.auth.models import User


class Receipes(models.Model):
    user =models.ForeignKey(User , on_delete=models.SETNULL , null = True,blank = True)
    receipe_name = models.CharField(max_length=100)
    receipe_description =models.TextField()
    receipe_image = models.ImageField(upload_to ="receipe")
    receipe_view_count = models.IntegerField(default=1)