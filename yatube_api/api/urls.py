from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet

router_v1 = DefaultRouter()

router_v1.register("posts", PostViewSet, basename="posts")
router_v1.register("groups", GroupViewSet)
router_v1.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)


urlpatterns = [
    path("v1/api-token-auth/", views.obtain_auth_token),
    path("v1/", include(router_v1.urls)),
]
