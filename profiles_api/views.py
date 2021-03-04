from rest_framework.views import APIView, Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """
    Test api view
    """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ 
        Return list of api view characteristics 
        """
        
        api_view = [
            'http methods',
            'similar to django traditional view'
        ]
        
        return Response({'message':"Hello", "api_view":api_view})
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                #serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        return Response({'method':'patch'})

    def delete(self, delete, pk=None):
        return Response({'method':'delete'})