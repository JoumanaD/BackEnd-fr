from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Adresse, Date, Etudiant, Fiche, Etablissement, Accueilservice, Gratification, RHservice, Stage, Tuteur
from .serializers import AdresseSerializer, DateSerializer, EtudiantSerializer, FicheSerializer, EtablissementSerializer, AccueilserviceSerializer, GratificationSerializer, RHserviceSerializer, StageSerializer, TuteurSerializer
from rest_framework.decorators import api_view

#GET list of Etudiants, POST new Etudiant, DELETE all Etudiants
@api_view(['GET', 'POST'])
def etudiant_list(request):
    if request.method == 'GET':
        etudiant = Etudiant.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            etudiant = etudiant.filter(title__icontains=title)
        
        etudiant_serializer = EtudiantSerializer(etudiant, many=True)
        return JsonResponse(etudiant_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        etudiant_data = JSONParser().parse(request)
        etudiant_serializer = EtudiantSerializer(data=etudiant_data)
        if etudiant_serializer.is_valid():
            etudiant_serializer.save()
            return JsonResponse(etudiant_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(etudiant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET / PUT / DELETE etudiant by ‘numero etudiant’
@api_view(['GET', 'PUT', 'DELETE'])
def etudiant_detail(request, pk):
    try: 
        etudiant = Etudiant.objects.get(pk=pk) 
    except Etudiant.DoesNotExist: 
        return JsonResponse({'message': 'etudiant does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        etudiant_serializer = EtudiantSerializer(etudiant) 
        return JsonResponse(etudiant_serializer.data) 
 
    elif request.method == 'PUT': 
        etudiant_data = JSONParser().parse(request) 
        etudiant_serializer = EtudiantSerializer(etudiant, data=etudiant_data) 
        if etudiant_serializer.is_valid(): 
            etudiant_serializer.save() 
            return JsonResponse(etudiant_serializer.data) 
        return JsonResponse(etudiant_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        etudiant.delete() 
        return JsonResponse({'message': 'etudiant was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

#FICHES  
#GET list of Fiches, POST new Etudiant, DELETE all Fiches
@api_view(['GET', 'POST'])
def fiche_list(request):
    if request.method == 'GET':
        fiche = Fiche.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            fiche = fiche.filter(title__icontains=title)
        
        fiche_serializer = FicheSerializer(fiche, many=True)
        return JsonResponse(fiche_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        fiche_data = JSONParser().parse(request)
        fiche_serializer = FicheSerializer(data=fiche_data)
        if fiche_serializer.is_valid():
            fiche_serializer.save()
            return JsonResponse(fiche_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(fiche_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET / PUT / DELETE fiche by ‘numero fiche'
@api_view(['GET', 'PUT', 'DELETE'])
def fiche_detail(request, pk):
    try: 
        fiche = Fiche.objects.get(pk=pk) 
    except Fiche.DoesNotExist: 
        return JsonResponse({'message': 'fiche does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        fiche_serializer = FicheSerializer(fiche) 
        return JsonResponse(fiche_serializer.data) 
 
    elif request.method == 'PUT': 
        fiche_data = JSONParser().parse(request) 
        fiche_serializer = FicheSerializer(fiche, data=fiche_data) 
        if fiche_serializer.is_valid(): 
            fiche_serializer.save() 
            return JsonResponse(fiche_serializer.data) 
        return JsonResponse(fiche_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        fiche.delete() 
        return JsonResponse({'message': 'fiche was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

#Adresse  
@api_view(['GET', 'POST'])
def adresse_list(request):
    if request.method == 'GET':
        adresse = Adresse.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            adresse = adresse.filter(title__icontains=title)
        
        adresse_serializer = AdresseSerializer(adresse, many=True)
        return JsonResponse(adresse_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        adresse_data = JSONParser().parse(request)
        adresse_serializer = AdresseSerializer(data=adresse_data)
        if adresse_serializer.is_valid():
            adresse_serializer.save()
            return JsonResponse(adresse_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(adresse_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def adresse_detail(request, pk):
    try: 
        adresse = Adresse.objects.get(pk=pk) 
    except Adresse.DoesNotExist: 
        return JsonResponse({'message': 'adresse does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        adresse_serializer = AdresseSerializer(adresse) 
        return JsonResponse(adresse_serializer.data) 
 
    elif request.method == 'PUT': 
        adresse_data = JSONParser().parse(request) 
        adresse_serializer = AdresseSerializer(adresse, data=adresse_data) 
        if adresse_serializer.is_valid(): 
            adresse_serializer.save() 
            return JsonResponse(adresse_serializer.data) 
        return JsonResponse(adresse_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        adresse.delete() 
        return JsonResponse({'message': 'adresse was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


#Etablissement
@api_view(['GET', 'POST'])
def etablissement_list(request):
    if request.method == 'GET':
        etablissement = Etablissement.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            etablissement = etablissement.filter(title__icontains=title)
        
        etablissement_serializer = EtablissementSerializer(etablissement, many=True)
        return JsonResponse(etablissement_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        etablissement_data = JSONParser().parse(request)
        etablissement_serializer = EtablissementSerializer(data=etablissement_data)
        if etablissement_serializer.is_valid():
            etablissement_serializer.save()
            return JsonResponse(etablissement_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(etablissement_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def etablissement_detail(request, pk):
    try: 
        etablissement = Etablissement.objects.get(pk=pk) 
    except Etablissement.DoesNotExist: 
        return JsonResponse({'message': 'etablissement does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        etablissement_serializer = EtablissementSerializer(etablissement) 
        return JsonResponse(etablissement_serializer.data) 
 
    elif request.method == 'PUT': 
        etablissement_data = JSONParser().parse(request) 
        etablissement_serializer = EtablissementSerializer(etablissement, data=etablissement_data) 
        if etablissement_serializer.is_valid(): 
            etablissement_serializer.save() 
            return JsonResponse(etablissement_serializer.data) 
        return JsonResponse(etablissement_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        etablissement.delete() 
        return JsonResponse({'message': 'etablissement was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    
#RHservicee  
@api_view(['GET', 'POST'])
def rhservice_list(request):
    if request.method == 'GET':
        rhservice = RHservice.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            rhservice = rhservice.filter(title__icontains=title)
        
        rhservice_serializer = RHserviceSerializer(rhservice, many=True)
        return JsonResponse(rhservice_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        rhservice_data = JSONParser().parse(request)
        rhservice_serializer = RHserviceSerializer(data=rhservice_data)
        if rhservice_serializer.is_valid():
            rhservice_serializer.save()
            return JsonResponse(rhservice_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(rhservice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def rhservice_detail(request, pk):
    try: 
        rhservice = RHservice.objects.get(pk=pk) 
    except RHservice.DoesNotExist: 
        return JsonResponse({'message': 'rhservice does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        rhservice_serializer = RHserviceSerializer(rhservice) 
        return JsonResponse(rhservice_serializer.data) 
 
    elif request.method == 'PUT': 
        rhservice_data = JSONParser().parse(request) 
        rhservice_serializer = RHserviceSerializer(rhservice, data=rhservice_data) 
        if rhservice_serializer.is_valid(): 
            rhservice_serializer.save() 
            return JsonResponse(rhservice_serializer.data) 
        return JsonResponse(rhservice_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        rhservice.delete() 
        return JsonResponse({'message': 'rhservice was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
 
#Accueilservice
@api_view(['GET', 'POST'])
def accueilservice_list(request):
    if request.method == 'GET':
        accueilservice = Accueilservice.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            accueilservice = accueilservice.filter(title__icontains=title)
        
        accueilservice_serializer = AccueilserviceSerializer(accueilservice, many=True)
        return JsonResponse(accueilservice_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        accueilservice_data = JSONParser().parse(request)
        accueilservice_serializer = AccueilserviceSerializer(data=accueilservice_data)
        if accueilservice_serializer.is_valid():
            accueilservice_serializer.save()
            return JsonResponse(accueilservice_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(accueilservice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def accueilservice_detail(request, pk):
    try: 
        accueilservice = Accueilservice.objects.get(pk=pk) 
    except Accueilservice.DoesNotExist: 
        return JsonResponse({'message': 'accueilservice does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        accueilservice_serializer = AccueilserviceSerializer(accueilservice) 
        return JsonResponse(accueilservice_serializer.data) 
 
    elif request.method == 'PUT': 
        accueilservice_data = JSONParser().parse(request) 
        accueilservice_serializer = AccueilserviceSerializer(accueilservice, data=accueilservice_data) 
        if accueilservice_serializer.is_valid(): 
            accueilservice_serializer.save() 
            return JsonResponse(accueilservice_serializer.data) 
        return JsonResponse(accueilservice_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        accueilservice.delete() 
        return JsonResponse({'message': 'accueilservice was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

#FICHES
@api_view(['GET', 'POST'])
def date_list(request):
    if request.method == 'GET':
        date = Date.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            date = date.filter(title__icontains=title)
        
        date_serializer = DateSerializer(date, many=True)
        return JsonResponse(date_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        date_data = JSONParser().parse(request)
        date_serializer = DateSerializer(data=date_data)
        if date_serializer.is_valid():
            date_serializer.save()
            return JsonResponse(date_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(date_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET / PUT / DELETE date by ‘numero date’
@api_view(['GET', 'PUT', 'DELETE'])
def date_detail(request, pk):
    try: 
        date = Date.objects.get(pk=pk) 
    except Date.DoesNotExist: 
        return JsonResponse({'message': 'date does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        date_serializer = DateSerializer(date) 
        return JsonResponse(date_serializer.data) 
 
    elif request.method == 'PUT': 
        date_data = JSONParser().parse(request) 
        date_serializer = DateSerializer(date, data=date_data) 
        if date_serializer.is_valid(): 
            date_serializer.save() 
            return JsonResponse(date_serializer.data) 
        return JsonResponse(date_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        date.delete() 
        return JsonResponse({'message': 'date was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

#Gratification
@api_view(['GET', 'POST'])
def gratification_list(request):
    if request.method == 'GET':
        gratification = Gratification.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            gratification = gratification.filter(title__icontains=title)
        
        gratification_serializer = GratificationSerializer(gratification, many=True)
        return JsonResponse(gratification_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        gratification_data = JSONParser().parse(request)
        gratification_serializer = GratificationSerializer(data=gratification_data)
        if gratification_serializer.is_valid():
            gratification_serializer.save()
            return JsonResponse(gratification_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(gratification_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET / PUT / DELETE gratification by ‘numero gratification’
@api_view(['GET', 'PUT', 'DELETE'])
def gratification_detail(request, pk):
    try: 
        gratification = Gratification.objects.get(pk=pk) 
    except Gratification.DoesNotExist: 
        return JsonResponse({'message': 'gratification does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        gratification_serializer = GratificationSerializer(gratification) 
        return JsonResponse(gratification_serializer.data) 
 
    elif request.method == 'PUT': 
        gratification_data = JSONParser().parse(request) 
        gratification_serializer = GratificationSerializer(gratification, data=gratification_data) 
        if gratification_serializer.is_valid(): 
            gratification_serializer.save() 
            return JsonResponse(gratification_serializer.data) 
        return JsonResponse(gratification_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        gratification.delete() 
        return JsonResponse({'message': 'gratification was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

#Stage
@api_view(['GET', 'POST'])
def stage_list(request):
    if request.method == 'GET':
        stage = Stage.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            stage = stage.filter(title__icontains=title)
        
        stage_serializer = StageSerializer(stage, many=True)
        return JsonResponse(stage_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        stage_data = JSONParser().parse(request)
        stage_serializer = StageSerializer(data=stage_data)
        if stage_serializer.is_valid():
            stage_serializer.save()
            return JsonResponse(stage_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(stage_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET / PUT / DELETE stage by ‘numero stage’
@api_view(['GET', 'PUT', 'DELETE'])
def stage_detail(request, pk):
    try: 
        stage = Stage.objects.get(pk=pk) 
    except Stage.DoesNotExist: 
        return JsonResponse({'message': 'stage does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        stage_serializer = StageSerializer(stage) 
        return JsonResponse(stage_serializer.data) 
 
    elif request.method == 'PUT': 
        stage_data = JSONParser().parse(request) 
        stage_serializer = StageSerializer(stage, data=stage_data) 
        if stage_serializer.is_valid(): 
            stage_serializer.save() 
            return JsonResponse(stage_serializer.data) 
        return JsonResponse(stage_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        stage.delete() 
        return JsonResponse({'message': 'stage was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


#Tuteur
@api_view(['GET', 'POST'])
def tuteur_list(request):
    if request.method == 'GET':
        tuteur = Tuteur.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tuteur = tuteur.filter(title__icontains=title)
        
        tuteur_serializer = TuteurSerializer(tuteur, many=True)
        return JsonResponse(tuteur_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tuteur_data = JSONParser().parse(request)
        tuteur_serializer = TuteurSerializer(data=tuteur_data)
        if tuteur_serializer.is_valid():
            tuteur_serializer.save()
            return JsonResponse(tuteur_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tuteur_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET / PUT / DELETE tuteur by ‘numero tuteur’
@api_view(['GET', 'PUT', 'DELETE'])
def tuteur_detail(request, pk):
    try: 
        tuteur = Tuteur.objects.get(pk=pk) 
    except Tuteur.DoesNotExist: 
        return JsonResponse({'message': 'tuteur does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tuteur_serializer = TuteurSerializer(tuteur) 
        return JsonResponse(tuteur_serializer.data) 
 
    elif request.method == 'PUT': 
        tuteur_data = JSONParser().parse(request) 
        tuteur_serializer = TuteurSerializer(tuteur, data=tuteur_data) 
        if tuteur_serializer.is_valid(): 
            tuteur_serializer.save() 
            return JsonResponse(tuteur_serializer.data) 
        return JsonResponse(tuteur_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tuteur.delete() 
        return JsonResponse({'message': 'tuteur was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)