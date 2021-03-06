# Generated by Django 2.2.1 on 2019-05-02 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eval', '0007_evaluation_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='status',
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='bathroom',
            field=models.IntegerField(choices=[(2, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='bathroomMadina',
            field=models.IntegerField(choices=[(2, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='commitmentDistance',
            field=models.IntegerField(choices=[(2, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='conditioning',
            field=models.IntegerField(choices=[(4, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='conditioningMadina',
            field=models.IntegerField(choices=[(4, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='contract',
            field=models.IntegerField(choices=[(2, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='distanceHotel',
            field=models.IntegerField(choices=[(6, 'قريبة'), (2, 'متوسطة'), (0, 'بعيدة')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='distanceHotelMadina',
            field=models.IntegerField(choices=[(6, 'قريبة'), (2, 'متوسطة'), (0, 'بعيدة')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='elevator',
            field=models.IntegerField(choices=[(5, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='elevatorMadina',
            field=models.IntegerField(choices=[(5, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='food',
            field=models.IntegerField(choices=[(3, 'نعم'), (0, 'لا'), (2, 'لا أعلم')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='foodMadina',
            field=models.IntegerField(choices=[(3, 'نعم'), (0, 'لا'), (2, 'لا أعلم')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='furniture',
            field=models.IntegerField(choices=[(4, 'جيد'), (2, 'متوسطة'), (0, 'سيء')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='furnitureMadina',
            field=models.IntegerField(choices=[(4, 'جيد'), (2, 'متوسطة'), (0, 'سيء')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='hotelRate',
            field=models.IntegerField(choices=[(2, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='insurance',
            field=models.IntegerField(choices=[(2, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='president',
            field=models.IntegerField(choices=[(2, 'كامل الرحلة'), (1, 'جزء من الرحلة فقط'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='presidentRate',
            field=models.IntegerField(choices=[(4, 'جيد'), (2, 'متوسطة'), (0, 'سيء')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='roomClean',
            field=models.IntegerField(choices=[(5, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='roomCleanMadina',
            field=models.IntegerField(choices=[(5, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='servicesOutside',
            field=models.IntegerField(choices=[(1, 'مطاعم'), (1, 'مواد غذائيّة'), (1, 'تسوّق')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='servicesOutsideMadina',
            field=models.IntegerField(choices=[(1, 'مطاعم'), (1, 'مواد غذائيّة'), (1, 'تسوّق')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='streetbus',
            field=models.IntegerField(choices=[(1, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='streetbusMadina',
            field=models.IntegerField(choices=[(1, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='theDate',
            field=models.IntegerField(choices=[(2, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='towel',
            field=models.IntegerField(choices=[(5, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='towelMadina',
            field=models.IntegerField(choices=[(5, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='wifi',
            field=models.IntegerField(choices=[(2, 'نعم'), (0, 'لا')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='wifiMadina',
            field=models.IntegerField(choices=[(2, 'نعم'), (0, 'لا')], default=1),
        ),
    ]
