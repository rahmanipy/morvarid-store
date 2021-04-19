# Generated by Django 3.1.5 on 2021-02-12 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_shop', '0005_auto_20210209_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryproducts', to='store_shop.category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='feature',
            field=models.ManyToManyField(blank=True, related_name='featureproducts', to='store_shop.Feature'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gallery',
            field=models.ManyToManyField(related_name='galleryproducts', to='store_shop.Gallery', verbose_name='گالری تصاویر'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tagproducts', to='store_shop.Tag'),
        ),
    ]