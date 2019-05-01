# Generated by Django 2.2.1 on 2019-05-01 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationAgency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfTravel', models.DateField()),
                ('days', models.IntegerField()),
                ('price', models.IntegerField()),
                ('contract', models.CharField(choices=[(2, 'نعم'), (0, 'لا')], max_length=10)),
                ('insurance', models.CharField(choices=[(2, 'نعم'), (0, 'لا')], max_length=10)),
                ('thedate', models.CharField(choices=[(2, 'نعم'), (0, 'لا')], max_length=10)),
                ('hotelRate', models.CharField(choices=[(2, 'نعم'), (0, 'لا')], max_length=10)),
                ('commitmentDistance', models.CharField(choices=[(2, 'نعم'), (0, 'لا')], max_length=10)),
                ('president', models.CharField(choices=[(2, 'كامل الرحلة'), (1, 'جزء من الرحلة فقط'), (0, 'لا')], max_length=10)),
                ('presidentrate', models.CharField(choices=[(4, 'جيد'), (2, 'متوسطة'), (0, 'سيء')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationHotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streetbus', models.CharField(choices=[(1, 'نعم'), (0, 'لا')], max_length=10)),
                ('servicesOutside', models.CharField(choices=[(1, 'مطاعم'), (1, 'مواد غذائيّة'), (1, 'تسوّق')], max_length=10)),
                ('distancehotel', models.CharField(choices=[(6, 'قريبة'), (2, 'متوسطة'), (0, 'بعيدة')], max_length=10)),
                ('furniture', models.CharField(choices=[(4, 'جيد'), (2, 'متوسطة'), (0, 'سيء')], max_length=10)),
                ('conditioning', models.CharField(choices=[(4, 'نعم'), (0, 'لا')], max_length=10)),
                ('bathroom', models.CharField(choices=[(2, 'نعم'), (0, 'لا')], max_length=10)),
                ('towel', models.CharField(choices=[(5, 'نعم'), (0, 'لا')], max_length=10)),
                ('roomclean', models.CharField(choices=[(5, 'نعم'), (0, 'لا')], max_length=10)),
                ('wifi', models.CharField(choices=[(2, 'نعم'), (0, 'لا')], max_length=10)),
                ('elevator', models.CharField(choices=[(5, 'نعم'), (0, 'لا')], max_length=10)),
                ('food', models.CharField(choices=[(3, 'نعم'), (0, 'لا'), (2, 'لا أعلم')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(choices=[('Mecca', 'مكّة'), ('Madina', 'المدينة')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agencyid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eval.EvaluationAgency')),
                ('hotelMadina', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Madina', to='eval.EvaluationHotel')),
                ('hotelMecca', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Mecca', to='eval.EvaluationHotel')),
            ],
        ),
    ]