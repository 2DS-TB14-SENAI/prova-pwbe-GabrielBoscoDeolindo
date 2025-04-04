from django.shortcuts import render
from .models import Servico, Agendamento
from .serializers import ServicoSerializer, AgendamentoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def listar_servicos(request):
    servicos = Servico.objects.all()
    serializer = ServicoSerializer(servicos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def servico_especifico(request, pk):
    try:
        servicos = Servico.objects.get(pk=pk)
    except servicos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ServicoSerializer(servicos)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def criar_servico(request):
    serializer = ServicoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def listar_agendamento(request):
    agendamento = Agendamento.objects.all()
    serializer = AgendamentoSerializer(agendamento, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def agendamento_especifico(request, pk):
    try:
        agendamentos = Agendamento.objects.get(pk=pk)
    except agendamentos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AgendamentoSerializer(agendamentos)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def criar_agendamento(request):
    serializer = AgendamentoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)