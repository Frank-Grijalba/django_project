from __future__ import unicode_literals
from django.db import models

class Registrado(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now = False)

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email
    

class Book(models.Model):

    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name
