from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Create a DefaultRouter instance
router = DefaultRouter()

# Register your viewsets with the router
router.register(r'datapointList', views.DataPointViewSet)


# # Include the router-generated URL patterns
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/datapoints-filtered/', views.DataPointFilterViewSet.as_view({'get': 'list'}), name='datapoints-filtered'),

]

# You can also add format suffix patterns if needed
# urlpatterns = format_suffix_patterns(urlpatterns)
