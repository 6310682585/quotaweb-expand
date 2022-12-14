# Generated by Django 4.1 on 2022-09-09 18:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('coursename', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Coursename', to='course.id')),
                ('username', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.PROTECT, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveIntegerField(choices=[(1, 'Semester One'), (2, 'Semester Two'), (3, 'Summer')])),
                ('year', models.CharField(help_text='Use format: YYYY', max_length=4)),
                ('seat', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
                ('coursestatus', models.IntegerField(choices=[(1, 'Open'), (0, 'Close')])),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CourseCode', to='course.id')),
            ],
        ),
    ]
