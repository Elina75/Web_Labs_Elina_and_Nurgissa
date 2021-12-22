from django.db import models


class Categories(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Cakes(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)



# CATEGORIES = (
#         ('Birthday', 'Birthday'),
#         ('Aesthetic', 'Aesthetic'),
#         ('Wedding', 'Wedding'),
#         ('Kids', 'Kids'),
#         ('Corporative', 'Corporative'),
#     )


