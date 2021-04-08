# Generated by Django 3.1.6 on 2021-03-29 11:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default=None, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='Builder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BuilderName', models.CharField(default=None, max_length=50)),
                ('Logo', models.FileField(upload_to='media/BuilderLogo')),
                ('SolePartner', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyContact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=60)),
                ('email', models.CharField(default='', max_length=60)),
                ('phone', models.CharField(default=None, max_length=12)),
                ('property_Name', models.CharField(default='', max_length=100)),
                ('message', models.TextField(default='')),
                ('contactTime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserContactData',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=60)),
                ('email', models.CharField(default='', max_length=60)),
                ('phone', models.CharField(default=None, max_length=12)),
                ('contact_time', models.DateTimeField(default=datetime.datetime.now)),
                ('message', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='UserResumeData',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=60)),
                ('email', models.CharField(default='', max_length=60)),
                ('phone', models.CharField(default=None, max_length=12)),
                ('resumetime', models.DateTimeField(default=datetime.datetime.now)),
                ('vacancy', models.CharField(default='', max_length=100)),
                ('message', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyList',
            fields=[
                ('Prop_ID', models.AutoField(primary_key=True, serialize=False)),
                ('PropertyName', models.CharField(max_length=100, unique=True)),
                ('slug', models.CharField(default='', max_length=550, null=True)),
                ('SearchName', models.CharField(default='', max_length=100)),
                ('Property_Image', models.ImageField(upload_to='media/Property_images')),
                ('Master_Plan', models.ImageField(blank=True, default='', upload_to='media/Master_Plans')),
                ('Floor_Plan_1BHK', models.ImageField(blank=True, default='', upload_to='media/Floor_Plan_1BHK')),
                ('Floor_Plan_2BHK', models.ImageField(blank=True, default='', upload_to='media/Floor_Plan_2BHK')),
                ('Floor_Plan_3BHK', models.ImageField(blank=True, default='', upload_to='media/Floor_Plan_3BHK')),
                ('Floor_Plan_4BHK', models.ImageField(blank=True, default='', upload_to='media/Floor_Plan_4BHK')),
                ('Video', models.FileField(blank=True, default='', upload_to='media/Videos')),
                ('Property_Price', models.CharField(default='', max_length=50)),
                ('ExOneBHK', models.CharField(blank=True, default='', max_length=100)),
                ('ExTwoBHK', models.CharField(blank=True, default='', max_length=99)),
                ('ExThreeBHK', models.CharField(blank=True, default='', max_length=90)),
                ('ExFourBHK', models.CharField(blank=True, default='', max_length=80)),
                ('PossessionDate', models.CharField(blank=True, max_length=80)),
                ('NoOfUnits', models.CharField(blank=True, max_length=80)),
                ('Property_Description', models.TextField(max_length=1000)),
                ('PropertyStatus', models.CharField(choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed'), ('Ready to move', 'Ready to move')], max_length=50)),
                ('Property_Type', models.CharField(choices=[('Residential', 'Residential'), ('Commercial', 'Commercial')], default='Residential', max_length=20)),
                ('SubPropType', models.CharField(choices=[('Plot', 'Plot'), ('Villa', 'Villa'), ('Apartment', 'Apartment'), ('Rowhouse', 'Rowhouse'), ('Farmhouse', 'Farmhouse'), ('Building', 'Building')], default='', max_length=60)),
                ('Location', models.CharField(choices=[('Bangalore', 'Bangalore'), ('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Punjab', 'Punjab')], max_length=50)),
                ('PropertyAddress', models.CharField(max_length=100)),
                ('BHK', models.CharField(max_length=50)),
                ('Avaliable_For', models.CharField(default='Sale', max_length=50)),
                ('Project_Area', models.CharField(default=None, max_length=100)),
                ('PerSqftPrice', models.CharField(default=None, max_length=100)),
                ('Google_Map', models.CharField(default='', max_length=10000)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('BuilderName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SHIApp.builder')),
                ('Property_Amenities', models.ManyToManyField(to='SHIApp.Amenities')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Images', models.ImageField(upload_to='media/IndividualPropImgs')),
                ('Image_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SHIApp.propertylist')),
            ],
        ),
        migrations.CreateModel(
            name='HotPropertyList',
            fields=[
                ('Prop_ID', models.AutoField(primary_key=True, serialize=False)),
                ('PropertyName', models.CharField(max_length=100, unique=True)),
                ('slug', models.CharField(default='', max_length=550, null=True)),
                ('SearchName', models.CharField(default='', max_length=100)),
                ('Property_Image', models.ImageField(upload_to='media/HotProperty_images')),
                ('Master_Plan', models.ImageField(blank=True, default='', upload_to='media/HotMaster_Plans')),
                ('Floor_Plan_1BHK', models.ImageField(blank=True, default='', upload_to='media/Hot_Prop_Floor_Plan_1BHK')),
                ('Floor_Plan_2BHK', models.ImageField(blank=True, default='', upload_to='media/Hot_Prop_Floor_Plan_2BHK')),
                ('Floor_Plan_3BHK', models.ImageField(blank=True, default='', upload_to='media/Hot_Prop_Floor_Plan_3BHK')),
                ('Floor_Plan_4BHK', models.ImageField(blank=True, default='', upload_to='media/Hot_Prop_Floor_Plan_4BHK')),
                ('ExOneBHK', models.CharField(blank=True, max_length=100)),
                ('ExTwoBHK', models.CharField(blank=True, max_length=99)),
                ('ExThreeBHK', models.CharField(blank=True, max_length=90)),
                ('ExFourBHK', models.CharField(blank=True, max_length=80)),
                ('PossessionDate', models.CharField(blank=True, max_length=80)),
                ('NoOfUnits', models.CharField(blank=True, max_length=80)),
                ('Video', models.FileField(blank=True, default='', upload_to='media/HotPropVideos')),
                ('Property_Price', models.CharField(default='', max_length=50)),
                ('Property_Description', models.TextField(max_length=1000)),
                ('PropertyStatus', models.CharField(choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed'), ('Ready to move', 'Ready to move')], max_length=50)),
                ('Property_Type', models.CharField(choices=[('Residential', 'Residentail'), ('Commercial', 'Commercial')], default='Residential', max_length=20)),
                ('SubPropType', models.CharField(choices=[('Plot', 'Plot'), ('Villa', 'Villa'), ('Apartment', 'Apartment'), ('Rowhouse', 'Rowhouse'), ('Farmhouse', 'Farmhouse')], default='', max_length=60)),
                ('Location', models.CharField(choices=[('Bangalore', 'Bangalore'), ('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Punjab', 'Punjab')], max_length=50)),
                ('PropertyAddress', models.CharField(max_length=100)),
                ('BHK', models.CharField(max_length=50)),
                ('Avaliable_For', models.CharField(default='Sale', max_length=50)),
                ('Project_Area', models.CharField(default=None, max_length=100)),
                ('PerSqftPrice', models.CharField(default=None, max_length=100)),
                ('Google_Map', models.CharField(default='', max_length=10000)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('BuilderName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SHIApp.builder')),
                ('Property_Amenities', models.ManyToManyField(to='SHIApp.Amenities')),
            ],
        ),
        migrations.CreateModel(
            name='HotPropertyImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Images', models.ImageField(upload_to='media/HotIndividualPropImgs')),
                ('Image_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SHIApp.hotpropertylist')),
            ],
        ),
    ]
