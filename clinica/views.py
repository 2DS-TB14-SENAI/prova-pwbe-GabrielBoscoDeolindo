from django.shortcuts import render
from .models import Medico, Consulta
from .serializers import MedicoSerializer, ConsultaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def listar_medicos(request):
        medicos = Medico.objects.all()
        serializer = MedicoSerializer(medicos, many=True)
        return render(request, 'listar_medicos.html', {'medicos': medicos})

@api_view(["POST"])
def criar_consulta(request):
        serializer = MedicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET"])
# def detalhes_consulta(request):
       