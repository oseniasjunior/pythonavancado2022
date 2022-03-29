from rest_framework.routers import DefaultRouter
from basic import viewsets

router = DefaultRouter()
router.register('course', viewsets.CourseViewSet)
# router.register('student', viewsets.StudentViewSet)

urlpatterns = router.urls
