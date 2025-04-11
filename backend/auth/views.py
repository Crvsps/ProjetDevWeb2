from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate, login


class CreateAccount(APIView):
    """
    Crée un compte utilisateur et génère un token d'authentification.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email', '')  # Vous pouvez ajouter l'email si nécessaire

        # Vérifier si l'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Ce nom d’utilisateur existe déjà'}, status=400)

        # Créer l'utilisateur
        user = User.objects.create_user(username=username, password=password, email=email)
        
        # Générer un token pour l'utilisateur
        token = Token.objects.create(user=user)
        
        return Response({'token': token.key}, status=201)


class LoginPage(APIView):
    """
    Authentifie l'utilisateur avec son nom d'utilisateur et son mot de passe,
    puis retourne un token d'authentification.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authentifier l'utilisateur
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Créer un token pour l'utilisateur s'il n'existe pas déjà
            token, created = Token.objects.get_or_create(user=user)

            # Se connecter l'utilisateur (enregistrer la session)
            login(request, user)

            return Response({'token': token.key}, status=200)
        else:
            return Response({'error': 'Identifiants incorrects'}, status=400)


class LogoutPage(APIView):
    """
    Déconnecte l'utilisateur en supprimant son token d'authentification.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Supprimer le token de l'utilisateur
        request.user.auth_token.delete()
        return Response({"success": "Déconnecté avec succès"}, status=200)