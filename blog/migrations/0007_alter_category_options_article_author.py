# Generated by Django 4.2.2 on 2023-06-07 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_category_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['parent__id', 'position'], 'verbose_name': 'دسته\u200cبندی', 'verbose_name_plural': 'دسته\u200cبندی ها'},
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articels', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
    ]
