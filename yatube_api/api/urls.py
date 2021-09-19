from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(
    'groups',
    GroupViewSet,
    basename='group'
)
router.register(
    'follow',
    FollowViewSet,
    basename='follow'
)


urlpatterns = [
    path('v1/api-token-auth/', obtain_auth_token),
    path('v1/', include(router.urls)),
]
