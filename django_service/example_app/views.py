import time

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ExampleView(APIView):

    def get(self, request, product_id):
        time.sleep(3)
        return Response({"Status": "Good!", "Message": "Hello world", "Product_id": product_id},
                        status=status.HTTP_200_OK)