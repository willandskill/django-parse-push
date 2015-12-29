
from django.db import models


class DeviceManager(models.Manager):

    def latest(self):
        """ Returns latest Device instance """
        return self.latest('created_at')

