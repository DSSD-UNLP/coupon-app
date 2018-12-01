from rest_framework.views               import APIView
from django.contrib.auth.hashers        import check_password
from couponProject.couponApp.models     import Coupon
from couponProject.couponApp.serializer import CouponSerializer
from django.shortcuts                   import get_list_or_404, get_object_or_404
from django.http                        import Http404
from rest_framework.response            import Response
from rest_framework                     import status

import code

class CouponCreate(APIView):
    
    def post(self, request):
        serializer = CouponSerializer(data = request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class CouponDetail(APIView):

    def get(self, request, name):
        try:
                coupon = Coupon.objects.get(name = name)
        except Coupon.DoesNotExist:
            response_message = {
                "status":"error", 
                "message":"Coupon not exists"
            }
            response_status = status.HTTP_200_OK

            return Response(response_message, status=response_status)
        serializer = CouponSerializer(coupon)

        return Response(serializer.data, status = status.HTTP_200_OK)
        
    def delete(self, request, name):
        coupon     = get_object_or_404(Coupon, name = name)
        serializer = CouponSerializer(coupon)
        coupon.delete()

        return Response(serializer.data, status = status.HTTP_200_OK)

    def patch(self,request,name):
        coupon = get_object_or_404(Coupon, name = name)
        if coupon.availability > 0:
            coupon.availability = (coupon.availability - 1)
            coupon.save()
            status_code    = status.HTTP_200_OK
            status_message = "ok"
            message        = "Se decremento en uno la cantidad"
        else:
            status_code    = status.HTTP_400_BAD_REQUEST
            status_message = "error"
            message        = "Este cupon ya fue usado"

        response_message   = {
            "status": status_message, 
            "message":message
        }

        return Response(response_message, status = status_code)
