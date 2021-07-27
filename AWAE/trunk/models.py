from django.db import models
from ordered_model.models import OrderedModel

# Create your models here.
TRUNK_MAX_LENGTH = 100


class Trunk(models.Model):
    name = models.CharField(blank=True, max_length=TRUNK_MAX_LENGTH)
    sub_title = models.CharField(blank=True, max_length=TRUNK_MAX_LENGTH)
    cols = models.IntegerField(default=4)

    def __str__(self):
        return self.name

class EyeKey(OrderedModel):
    name = models.CharField(blank=True, max_length=TRUNK_MAX_LENGTH)
    label = models.CharField(blank=True, max_length=3)
    trunk = models.ForeignKey(Trunk, on_delete=models.CASCADE, null=True, related_name="eye_keys")
    row = models.IntegerField(default=1)
    col = models.IntegerField(default=1)
    col_size = models.IntegerField(default=1)

    order_with_respect_to = 'trunk'

    def __str__(self):
        output = self.name
        if self.trunk:
            output += " | " + self.trunk.name
        return output
