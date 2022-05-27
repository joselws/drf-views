from django.urls import path, include
from .views import StudentList, StudentDetail, GenericStudentList, GenericStudentDetail, SuperGenericStudentList, SuperGenericStudentDetail, StudentViewSet, StudentGenericViewSet, StudentModelViewSet
from rest_framework.routers import DefaultRouter

vsrouter = DefaultRouter()
vsrouter.register('student', StudentViewSet, basename='student')

grouter = DefaultRouter()
grouter.register('student', StudentGenericViewSet, basename='student')

mrouter = DefaultRouter()
mrouter.register('student', StudentModelViewSet, basename='student')


urlpatterns = [
    path('student/', StudentList.as_view()),
    path('student/<int:pk>/', StudentDetail.as_view()),
    path('supergeneric/student/', SuperGenericStudentList.as_view()),
    path('supergeneric/student/<int:pk>', SuperGenericStudentDetail.as_view()),
    path('generic/student/', GenericStudentList.as_view()),
    path('generic/student/<int:pk>', GenericStudentDetail.as_view()),
    path('viewset/', include(vsrouter.urls)),
    path('viewset/<int:pk>', include(vsrouter.urls)),
    path('genericviewset/', include(grouter.urls)),
    path('genericviewset/<int:pk>', include(grouter.urls)),
    path('modelviewset/', include(mrouter.urls)),
    path('modelviewset/<int:pk>', include(mrouter.urls)),
]