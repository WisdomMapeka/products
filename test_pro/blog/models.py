from django.db import models

# Create your models here.
class Categories(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		db_table="cats"

class Products(models.Model):
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
	product_name = models.CharField(max_length=200, null=True, blank=True)
	price = models.CharField(max_length=200, blank=True, null=True)
	description = models.TextField()

	def __str__(self):
		return "{} {}".format(self.product_name, self.price)

	class Meta:
		db_table="prods"
