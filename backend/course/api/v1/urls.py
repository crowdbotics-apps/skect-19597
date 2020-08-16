from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    RecordingViewSet,
    EventViewSet,
    SubscriptionViewSet,
    CourseViewSet,
    GroupViewSet,
    ModuleViewSet,
    PaymentMethodViewSet,
    SubscriptionTypeViewSet,
    EnrollmentViewSet,
    LessonViewSet,
    CategoryViewSet,
)

router = DefaultRouter()
router.register("lesson", LessonViewSet)
router.register("recording", RecordingViewSet)
router.register("event", EventViewSet)
router.register("enrollment", EnrollmentViewSet)
router.register("module", ModuleViewSet)
router.register("group", GroupViewSet)
router.register("subscriptiontype", SubscriptionTypeViewSet)
router.register("category", CategoryViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("course", CourseViewSet)
router.register("subscription", SubscriptionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
