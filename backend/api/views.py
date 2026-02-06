from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializers

@api_view(['GET'])
def register(request):
    return Response({'message':'Registered Successfully'})

@api_view(['POST'])
def register_page(request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Registered successfully'})
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)