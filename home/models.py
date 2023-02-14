from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name + ': ' + self.message[:20] + '...'


class Category(models.Model):
    name = models.CharField(max_length=30)
    rating = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Size(models.Model):
    amount = models.FloatField()
    coffee = models.ManyToManyField('Coffee', related_name='sizes')


class Coffee(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="coffee")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Coffee'


class Producer(models.Model):
    brand = models.CharField(max_length=40)
    coffee = models.OneToOneField('Coffee', related_name='producer', on_delete=models.CASCADE)

    def __str__(self):
        return self.brand
