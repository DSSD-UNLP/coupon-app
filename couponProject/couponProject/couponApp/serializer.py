from couponProject.couponApp.models import Coupon
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ('name', 'percentage', 'availability')