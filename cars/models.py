from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

class Car(models.Model):

    state_choice = (
        ('AB', 'Abia'),
        ('AD', 'Adamawa'),
        ('AK', 'Akwaimbo'),
        ('AN', 'Anambra'),
        ('BA', 'Bauchi'),
        ('BA', 'Bayelsa'),
        ('BE', 'Benue'),
        ('BO', 'Borno'),
        ('CR', 'Cross River'),
        ('DE', 'Delta'),
        ('EB', 'Ebonyi'),
        ('ED', 'Edo'),
        ('EK', 'Ekiti'),
        ('EN', 'Enugu'),
        ('GO', 'Gombe'),
        ('IM', 'Imo'),
        ('JI', 'Jigawa'),
        ('KA', 'Kaduna'),
        ('KA', 'Kano'),
        ('KA', 'Kastina'),
        ('KE', 'Kebbi'),
        ('KO', 'Kogi'),
        ('KW', 'Kwara'),
        ('LA', 'Lagos'),
        ('NA', 'Nasawara'),
        ('NI', 'Niger'),
        ('OG', 'Ogun'),
        ('ON', 'Ondo'),
        ('OS', 'Osun'),
        ('OY', 'Oyo'),
        ('PL', 'Plateu'),
        ('RI', 'Rivers'),
        ('SO', 'Sokoto'),
        ('TR', 'Taraba'),
        ('YO', 'Yobe'),
        ('ZA', 'Zamfarawa'),
        ('AB', 'Abuja'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r, r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )
    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=250)
    state = models.CharField(choices=state_choice, max_length=250)
    city = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=200)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=150)
    engine = models.CharField(max_length=150)
    transmission = models.CharField(max_length=150)
    interior = models.CharField(max_length=150)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passenger = models.IntegerField()
    vin_no = models.CharField(max_length=150)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=150)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

