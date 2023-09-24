from django.db import models
from datetime import date


class Restaurant(models.Model):

    restaurant_title = models.CharField(max_length=100)

    def get_menu_for_date(self):
        today_date = date.today()
        day_of_week = today_date.isoweekday()
        try:
            matching_menus = self.menu_set.filter(day_of_week=day_of_week)
            return matching_menus
        except Menu.DoesNotExist:
            return None

    def get_total_votes(self):
        total_votes = 0
        menus = self.menu_set.all()

        for menu in menus:
            total_votes += menu.votes

        return total_votes


class Menu(models.Model):

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    DAY_CHOICES = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )

    menu_name = models.CharField(max_length=50)
    menu_price = models.FloatField()
    day_of_week = models.IntegerField(choices=DAY_CHOICES)
    votes = models.IntegerField(default=0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_set')

    def has_discount(self):

        discount_dates = [
            date(year=2023, month=12, day=25),
            date(year=2023, month=10, day=31),
            date(year=2023, month=10, day=1),
            date(year=2023, month=8, day=24),
            date(year=2023, month=12, day=31),
        ]
        today_date = date.today()

        return today_date in discount_dates

    def apply_discount(self):
        if self.has_discount():
            self.menu_price *= 0.85


class MenuItem(models.Model):

    menu_item_name = models.CharField(max_length=50)
    menu_item_description = models.TextField()
    is_vegan = models.BooleanField(default=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')


class Allergen(models.Model):

    allergen_name = models.CharField(max_length=30)
    menu_item = models.ManyToManyField(MenuItem, related_name="allergens")
