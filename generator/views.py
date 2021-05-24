import datetime
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UuidPairs
# Create your views here.

class UuidPairView(APIView):

    def get(self, request, *args, **kwargs):
        data = {str(datetime.datetime.now()):str(uuid.uuid1())}
        if UuidPairs.objects.exists():
            pairs = UuidPairs.objects.first()
            update_pair = pairs.pair
            data.update(update_pair)
            pairs.pair = data
            pairs.save()
        else:
            UuidPairs.objects.create(pair=data)
        get_data = UuidPairs.objects.first().pair
        return Response(get_data, status=status.HTTP_200_OK)
    
