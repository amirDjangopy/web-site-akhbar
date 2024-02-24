from django.db import models
from django.urls import reverse
from account.models import User
from django.utils.html import format_html
from django.utils import timezone
from extensions.utils import jalali_converter

#your Manager ArticleManager

class ArticleManager(models.Manager):
	def published(self):
		return self.filter(status="p")


#your Manager CategoryManager
class CategoryManager(models.Manager):
	def active(self):
		return self.filter(status=True)

# Category Models

class Category(models.Model):
	parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name="children", verbose_name="زیر دسته")
	title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
	slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
	status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
	position = models.IntegerField(verbose_name="پوزیشن")
	class Meta:
		verbose_name = "دسته‌بندی"
		verbose_name_plural = "دسته‌بندی ها"
		ordering = ['parent__id', 'position']


	def __str__(self):
		return self.title


	objects = CategoryManager()



# Article Models

class Article(models.Model):
	STATUS_CHOICES = (
		('d', 'پیش‌نویس'),		 # draft
		('p', "منتشر شده"),		 # publish
	)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="articels", verbose_name="نویسنده")
	title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
	slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
	category = models.ManyToManyField(Category, verbose_name="دسته‌بندی", related_name="articels")
	description = models.TextField(verbose_name="محتوا")
	thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر مقاله")
	publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d', verbose_name="وضعیت")

	class Meta:
		verbose_name = "مقاله" 
		verbose_name_plural = "مقالات"
		ordering = ['-publish']


# your function me

	def __str__(self):
		return self.title
	

	def get_absolute_url(self):
		return reverse("account:home")


	def jpublish(self):
		return jalali_converter(self.publish)
	jpublish.short_description = "زمان انتشار"



	def thumbnail_tags(self):
		return format_html("<img width=100  style= 'border-radius: 6px' src='{}'>".format(self.thumbnail.url))
	thumbnail_tags.short_description = "عکس مقاله"
	
	

	def category_to_str(self):
		return ", ".join([category.title for category in self.category.active()])
	category_to_str.short_description = "دسته بندی"
	


	objects = ArticleManager()


