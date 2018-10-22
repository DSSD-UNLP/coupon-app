from couponProject.couponApp.models import Coupon
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password


class CouponSerializer(serializers.ModelSerializer):
    availability = serializers.SerializerMethodField()

    class Meta:
        model  = Coupon
        fields = ('name', 'percentage', 'availability')

    def get_availability(self, obj):
        return obj.availability != 0