from django.db import models

# Create your models here.

class Usuarios(models.Model):
    usuario_id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    email = models.CharField(max_length=50)
    profile_img = models.CharField(max_length=10000)

    def __str__(self) -> str:
        return self.full_name
