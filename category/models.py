from django.db import models
from model_utils.models import TimeStampedModel


class Categories(TimeStampedModel):
    category_name = models.CharField('Category Name', max_length=250, null=True, blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SubCategories(TimeStampedModel):
    sub_category_name = models.CharField('Sub-Category Name', max_length=250, null=True, blank=True)
    category = models.ForeignKey("Categories", blank=True, null=True,
                                 on_delete=models.CASCADE, related_name='sub_categories_categories')

    def __str__(self):
        return self.sub_category_name

    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"


class Products(TimeStampedModel):
    product_name = models.CharField('Product Name', max_length=250, null=True, blank=True)
    sub_category = models.ForeignKey("SubCategories", blank=True, null=True,
                                     on_delete=models.CASCADE, related_name='sub_categories_categories')
    category = models.ForeignKey("Categories", blank=True, null=True,
                                 on_delete=models.CASCADE, related_name='products_categories_categories')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
