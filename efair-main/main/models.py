from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils import timezone
from .managers import CustomUserManager
from django.core.validators import RegexValidator


class CustomUser(AbstractBaseUser, PermissionsMixin):
    iin = models.CharField(max_length=12, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    home_number = models.CharField(max_length=64)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{11}$',
        message='Номер телефона должен быть в международном формате: +77011234567'
    )
    phone = models.CharField(validators=[phone_regex], max_length=12)
    avatar = models.ImageField(upload_to='profile_photo', default='img/default_avatar.jpg')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name 
    
    USERNAME_FIELD = 'iin'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
    
    def __str__(self):
        return self.name


class OfferModel(models.Model):
    name = models.CharField(max_length=128)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
    
    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=64)
    
    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'
    
    def __str__(self):
        return self.name


class OfferSale(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to='img/offer_image', default='img/no_item_image.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    offer_model = models.ForeignKey(OfferModel, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    condition_new = models.BooleanField(default=True)
    price = models.PositiveIntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
    in_active = models.BooleanField(default=True)
    salesman = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    home_number = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Предложение на продажу'
        verbose_name_plural = 'Предложения на продажу'    
    
    def __str__(self):
        return self.title


class OfferBuy(models.Model):
    sale = models.ForeignKey(OfferSale, on_delete=models.CASCADE)
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    in_active = models.BooleanField(default=True)
    datetime = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Предложение на покупку'
        verbose_name_plural = 'Предложения на покупку'    
    
    def __str__(self):
        return self.sale.title

class News(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='img/news_image', default='img/default_news.jpg')
    datetime = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'    
    
    def __str__(self):
        return self.title
