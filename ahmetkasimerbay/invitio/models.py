from django.db import models

# Create your models here.

class Persons(models.Model):
    def __str__(self):
        return "Persons Table"

    STATUS = (
        (1, "Katılılyorum"),
        (2, "Katılamıyorum"),
        (3, "Belli Değil")
    )

    p_name = models.CharField(max_length=30)
    p_surname = models.CharField(max_length=20)
    p_is_alone = models.BooleanField()
    p_adult = models.BooleanField()
    p_num_guests = models.IntegerField()
    p_attandance_status = models.PositiveSmallIntegerField(
        choices=STATUS,
        default=0,
    )
    p_phone = models.CharField(max_length=13)
    p_message = models.TextField()
    p_register_date = models.DateTimeField(auto_now_add=True)


class Guest(models.Model):
    g_p_id = models.IntegerField() # p_id
    g_name = models.CharField(max_length=30)
    g_surname = models.CharField(max_length=20)
    g_adult = models.BooleanField() 
