from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.translation import ugettext_lazy as _

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken

from users.services import AuthenticationService
from users.models import Profile
from .serializers import UserSerializer, ProfileSerializer


@api_view(['GET'])
def get_self_profile(request: Request) -> Response:
    """Gets self profile"""
    profile = Profile.objects.get(user=request.user)
    serialized_profile = ProfileSerializer(profile)
    return Response(serialized_profile.data)


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login(request: Request) -> Response:
    """Gets a user model along with access and refresh tokens"""
    try:
        password = request.data['password']
        email = request.data["email"]
    except KeyError:
        return Response({"detail": _('both email and password are required')}, status=400)
    try:
        user = AuthenticationService.login_user(email, password)
    except PermissionError as e:
        return Response({"detail": e})
    refresh = RefreshToken.for_user(user)
    serializer = UserSerializer(user)
    return Response({
        'user': serializer.data,
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }, status=200)


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def register(request: Request) -> Response:
    """Registers a new user"""
    try:
        email = request.data["email"]
        password = request.data['password']
    except KeyError:
        return Response({"detail": _('both email and password are required')}, status=400)
    try:
        AuthenticationService.register_new_user(email, password)
    except ValueError as e:
        return Response({"detail": e}, status=403)
    return Response({"detail": "created"}, status=201)
