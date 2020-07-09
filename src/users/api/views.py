from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


@api_view(['GET'])
def get_self_profile(request):
    user = request.user
    serialized_user = UserSerializer(user).data
    return Response({'user': serialized_user })