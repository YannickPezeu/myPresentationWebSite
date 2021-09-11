from djongo import models
from django.utils.timezone import now
import json
# Create your models here.




# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class User(models.Model):
    Name = models.CharField(max_length = 100)
    Image = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.Name}"

class Comment(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Text = models.TextField()

    def __str__(self):
        return f"{self.Text}"

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

# class CarModel(models.Model):
#     CarMake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
#     DealerId = models.IntegerField()
#     Name = models.CharField(max_length = 100)
#     Type = models.TextField(choices = [("Sedan", "Sedan"), ("SUV", "SUV"), ("WAGON", "WAGON")])
#     Year = models.DateField()
#
#     def __str__(self):
#         return f"{self.Name}"

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
# class CarDealer:
#
#     def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
#         # Dealer address
#         self.address = address
#         # Dealer city
#         self.city = city
#         # Dealer Full Name
#         self.full_name = full_name
#         # Dealer id
#         self.id = id
#         # Location lat
#         self.lat = lat
#         # Location long
#         self.long = long
#         # Dealer short name
#         self.short_name = short_name
#         # Dealer state
#         self.st = st
#         # Dealer zip
#         self.zip = zip
#
#     def __str__(self):
#         return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data

# class DealerReview:
#
#     def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
#         self.dealership = dealership
#         self.name = name
#         self.purchase = purchase
#         self.review = review
#         self.purchase_date = purchase_date
#         self.car_make = car_make
#         self.car_model = car_model
#         self.car_year = car_year
#         self.sentiment = sentiment
#         self.id = id
#
#     def __str__(self):
#         return "Dealer name: " + self.name


# class Certificate:
#     def __init__(self, id, title, school, topics, skills, link, link2="" ):
#         self.id = id,
#         self.title = title,
#         self.school = school,
#         self.topics = topics,
#         self.skills = skills,
#         self.link = link,
#         self.link2 = link2
#
#     def __str__(self):
#         return self.title

class Certificate(models.Model):
    title = models.CharField(max_length=250)
    school = models.CharField(max_length=250)
    topics = models.CharField(max_length=2000)
    skills = models.CharField(max_length=2000)
    flags = models.CharField(max_length=2000, null=True)
    link = models.CharField(max_length=500)
    link2 = models.CharField(max_length=500)

    def set_topics(self, x):
        self.foo = json.dumps(x)

    def get_topics(self):
        return json.loads(self.topics)

    def set_skills(self, x):
        self.foo = json.dumps(x)

    def get_skills(self):
        return json.loads(self.skills)

    def set_flags(self, x):
        self.foo = json.dumps(x)

    def get_flags(self):
        return json.loads(self.flags)

    def __str__(self):
        return self.title


