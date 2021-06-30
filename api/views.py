from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse

from .models import Etudiant, Fiche
from .serializers import EtudiantSerializer, FicheSerializer

# Create your views here.
def etudiantApiGETAll(request):
    if request.method=='GET':
        etudiant = Etudiant.objects.all()
        etudiant_serializer = EtudiantSerializer(etudiant, many=True)
        return JsonResponse(etudiant_serializer.data, safe=False)

@csrf_exempt
def etudiantApi(request, id=''):
    if request.method=='GET':
        etudiant = Etudiant.objects.get(pk=id)
        etudiant_serializer = EtudiantSerializer(etudiant, many=True)
        return JsonResponse(etudiant_serializer.data, safe=False)
    elif request.method=='POST':
        etudiant_data=JSONParser().parse(request)
        etudiant_serializer=EtudiantSerializer(data=etudiant_data)
        if etudiant_serializer.is_valid():
            etudiant_serializer.save()
            HttpResponse(etudiant_data)
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        etudiant_data = JSONParser().parse(request)
        etudiant=Etudiant.objects.get(id=etudiant_data['IDetudiant'])
        etudiant_serializer=EtudiantSerializer(etudiant, data=etudiant_data)
        if etudiant_serializer.is_valid():
            etudiant_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.methos=='DELETE':
        etudiant=Etudiant.objects.get(IDetudiant=id)
        etudiant.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)
    return JsonResponse("Failed to Delete", safe=False)

