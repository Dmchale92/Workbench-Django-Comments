"""
Workbench URL Configuration

Register URL for viewing all comments, as well as URLs for viewing comments from each content URL
"""
from django.conf.urls import url, include
from rest_framework import routers
from Comments import views

router = routers.DefaultRouter()
router.register(r'low-altitude-launch', views.LowAltitudeViewSet)
router.register(r'planetary-motion', views.PlanetaryMotionViewSet)
router.register(r'pop-quiz', views.PopQuizViewSet)
router.register(r'comments', views.CommentViewSet)

# Wire up API using automatic URL routing.
# Additionally, include login URLs for the browsable API (authentication not required).
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]