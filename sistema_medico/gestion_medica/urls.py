from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet, MedicoViewSet, CitaViewSet, PacientesAdultosAPIView

router = DefaultRouter()
router.register('pacientes', PacienteViewSet)
router.register('medicos', MedicoViewSet)
router.register('citas', CitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('adultos/', PacientesAdultosAPIView.as_view(), name='adultos-api'),
]
