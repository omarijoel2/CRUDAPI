# Generated by Django 3.1.3 on 2020-11-22 09:56

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('Country_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Country', django_countries.fields.CountryField(max_length=2, verbose_name='Country Name')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ImpelementingOffice', models.CharField(max_length=225, verbose_name='Impelementing Office')),
            ],
        ),
        migrations.CreateModel(
            name='Readiness',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('TypeOfReadiness', models.CharField(max_length=225, verbose_name='Type of Readiness')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('ProjectRef', models.CharField(help_text='Enter field documentation', max_length=20)),
                ('ProjectTitle', models.TextField()),
                ('DateFromGcf', models.DateField()),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('Disbursement', models.IntegerField()),
                ('GrantAmount', models.IntegerField()),
                ('Status', models.CharField(max_length=20)),
                ('Country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.country', verbose_name='Country')),
                ('ImplementingOffice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.office')),
                ('TypeOfReadiness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.readiness')),
            ],
        ),
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.IntegerField()),
                ('project_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projects')),
            ],
        ),
    ]
