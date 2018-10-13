from couponProject.couponApp.models import Coupon
from couponProject.couponApp.serializer import CouponSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.hashers import check_password
import code

class CouponList(APIView):
    
    def post(self, request, format=None):
        serializer = CouponSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CouponDetail(APIView):

    def makeResponse(self,serializer):
        if(serializer.data['availability']!=0):
            availability = True
        else:
            availability = False
        response_message = {"name":serializer.data['name'], "availability": availability, "percentage":serializer.data['percentage']}
        return response_message

    def get(self, request, name):
        coupon = get_object_or_404(Coupon, name=name)
        serializer = CouponSerializer(coupon)
        response_message = self.makeResponse(serializer)
        return Response(response_message)

    def delete(self, request, pk, format=None):
        coupon = get_object_or_404(Coupon, pk=pk)
        serializer = CouponSerializer(coupon)
        coupon.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def patch(self,request,name):
        coupon = get_object_or_404(Coupon,name=name)
        if coupon.availability > 0:
            coupon.availability = coupon.availability-1
            coupon.save()
            message = "Updated successfully"
        else:
            message="Este cupon ya fue usado"
        #serializer = CouponSerializer(coupon, data=request.data)
        #if serializer.is_valid():
        #    serializer.save()
        response_message = {"status":"ok", "message":message}
        return Response(response_message, status=status.HTTP_400_BAD_REQUEST)



