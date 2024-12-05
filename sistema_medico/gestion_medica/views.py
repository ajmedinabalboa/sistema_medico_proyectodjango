from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Paciente, Medico, Cita
from .serializers import PacienteSerializer, MedicoSerializer, CitaSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class PacientesAdultosAPIView(APIView):
    def get(self, request):
        pacientes_adultos = Paciente.objects.filter(fecha_nacimiento__year__lte=2006)
        return Response({"adultos": [f"{p.nombre} {p.apellido}" for p in pacientes_adultos]})

