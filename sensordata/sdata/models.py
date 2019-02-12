from django.db import models

class labdata(models.Model):
    temp = models.IntegerField(default=200)
    gas = models.IntegerField(default=200)
    mois = models.IntegerField(default=200)
    fire = models.IntegerField(default=200)
    light = models.IntegerField(default=200)

    def __str__(self):
        return str(self.temp)

# class userdata(models.Model):
#     mname = models.CharField(max_length=20,default='xxx')
#     memail = models.CharField(max_length=50,default='xxx')
#     mpswd = models.CharField(max_length=20,default='xxx')
#
#     def __str__(self):
#         return self.mname

