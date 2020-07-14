from django.core.exceptions import ValidationError
from django.core.validators import validate_email
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
        return Response({"detail": _('Both email and password are required')}, status=400)
    try:
        user = AuthenticationService.login_user(email, password)
    except PermissionError as e:
        return Response({"detail": e.args[0]}, status=403)
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
        return Response({"detail": _('Both email and password are required')}, status=400)
    try:
        validate_email(email)
    except ValidationError:
        return Response({"detail": _('Bad email address')}, status=400)
    try:
        AuthenticationService.register_new_user(email, password)
    except ValueError as e:
        return Response({"detail": e.args[0]}, status=400)
    return Response({"detail": "created"}, status=201)


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def change_password(request: Request) -> Response:
    """Changes a password if user exists and old password is ok"""
    try:
        email = request.data["email"]
        old_password = request.data['old_password']
        new_password = request.data['new_password']
    except KeyError:
        return Response({"detail": _('Email, new_password and old_password, are required')}, status=400)
    if old_password == new_password:
        return Response({"detail": _("""New password can't be the same as the old one""")}, status=400)
    try:
        validate_email(email)
    except ValidationError:
        return Response({"detail": _('Bad email address')}, status=400)
    try:
        AuthenticationService.change_password(email, old_password, new_password)
    except PermissionError as e:
        return Response({"detail": e.args[0]}, status=400)
    return Response({"detail": "changed"}, status=200)