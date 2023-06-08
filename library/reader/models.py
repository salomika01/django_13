from django.db import models

class Reader(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    favorite_book = models.ForeignKey('book.Book', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
