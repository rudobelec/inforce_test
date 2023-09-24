from rest_framework import serializers
from .models import Restaurant, Menu, MenuItem, Allergen
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']


class AllergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergen
        fields = ['allergen_name']


class MenuItemSerializer(serializers.ModelSerializer):
    allergens = AllergenSerializer(many=True)

    class Meta:
        model = MenuItem
        fields = ['menu_item_name', 'menu_item_description', 'is_vegan', 'allergens']


class MenuSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True)

    class Meta:
        model = Menu
        fields = ['menu_name', 'menu_price', 'menu_items']


class RestaurantSerializer(serializers.ModelSerializer):
    today_menu = serializers.SerializerMethodField()
    total_votes = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['restaurant_title', 'today_menu', 'total_votes']

    def get_total_votes(self, obj):
        return obj.get_total_votes()

    def get_today_menu(self, obj):
        matching_menus = obj.get_menu_for_date()
        menu_serializer = MenuSerializer(matching_menus, many=True)
        return menu_serializer.data
