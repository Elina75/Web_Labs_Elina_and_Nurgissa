from django.db import models


# class Categories(models.Model):
#     name = models.CharField(max_length=30)
#     def __str__(self):
#         return self.name


# class Articles(models.Model):
#     name = models.CharField(max_length=30)
#     amount = models.IntegerField
#     weight = models.IntegerField
#     price = models.IntegerField
#     category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)

class Cakes(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.CharField(max_length=50)



