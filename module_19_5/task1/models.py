from django.db import models

# Create your models here.


class Buyer (models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Flowers (models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='flowers')

    def __str__(self):
        return self.title


class Good(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default='Не определена')
    price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.product_name


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


# использование созданных моделей для работы с данными.
# Например, для получения всех товаров определённой категории вы можете выполнить:
# all_goods_in_category = Good.objects.filter(category__category_name='Название категории')
# for good in all_goods_in_category:
#     print(good.product_name)
