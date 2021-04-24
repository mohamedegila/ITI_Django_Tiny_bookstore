from rest_framework.response import Response
from rest_framework import status
from books.models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework import viewsets
@api_view(['GET'])
def index(request):
    books      = Book.objects.all()
    serializer = BookSerializer(instance=books,many=True)

    return Response(data=serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def create(request):
    serializer = BookSerializer(data=request.data)
    if serializer .is_valid():
        serializer.save()
        return Response(data={
            "success" : True,
            "message" : "Book has add successfully"
        },status=status.HTTP_201_CREATED)

    return Response(data={
            "success" : False,
            "errors"  : serializer.errors 
        },status=status.HTTP_400_REQUEST)


#======================= Class Based (generic & Viewsets) Examples =================
class IndexPost(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class RudPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#============= requires router object see the main urls.py file ===========
class PostViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer