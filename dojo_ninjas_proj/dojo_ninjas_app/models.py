from django.db import models

# Create your models here.
class Dojo(models.Model):
    loc_name = models.CharField(max_length = 40)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 30)
    desc = models.TextField(null=True)
    # ninjas (related_name)

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)