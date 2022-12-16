from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('position', )


class Dish(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes/', filename)

    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_special = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    ingredients = models.CharField(max_length=300)
    desc = models.TextField(max_length=1_000, blank=True)
    photo = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category.name}: {self.name}: {self.position}'

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'
        ordering = ('position', )
