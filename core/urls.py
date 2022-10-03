from django.urls import path, include

#esto son los routers
from hec_api.routers.userRouter import router_user 
from hec_api.routers.medicoRouter import router_medico
from hec_api.routers.familiarRouter import router_familiar
from hec_api.routers.enfermeroRouter import router_enfermero
from hec_api.routers.pacienteRouter import router_paciente
from hec_api.routers.signosvitalesRouter import router_signos
from hec_api.routers.sugerenciascuidadoRouter import router_sugerencias
from hec_api.routers.diagnosticoRouter import router_diagnostico


#no los estamos utilzando
from django.contrib import admin


#Esto es para el token
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)



urlpatterns = [

    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),



    path('admin/', admin.site.urls),

    path('api/users/', include(router_user.urls)),
    path('api/familiares/', include(router_familiar.urls)),
    path('api/enfermeros/', include(router_enfermero.urls)),
    path('api/pacientes/', include(router_paciente.urls)),

    path('api/signos-vitales/', include(router_signos.urls)),
    path('api/sugerencias/', include(router_sugerencias.urls)),
    path('api/diagnostico/', include(router_diagnostico.urls)),

    path('api/medicos/', include(router_medico.urls)),


    
]

# URL pattern: ^api/users/$ Name: 'user-list'
# URL pattern: ^api/users/{pk}/$ Name: 'user-detail'