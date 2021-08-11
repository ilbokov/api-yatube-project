from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)

from .views import CommentsViewSet, FollowViewSet, GroupViewSet, PostsViewSet

router_v1 = DefaultRouter()
router_v1.register(r'v1/posts', PostsViewSet, 'posts')
router_v1.register(
    r'v1/posts/(?P<id_post>[0-9]+)/comments',
    CommentsViewSet,
    'post_comments')
router_v1.register(r'v1/follow', FollowViewSet, 'follow')
router_v1.register(r'v1/group', GroupViewSet, 'group')

urlpatterns = [
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(
        'v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
    path('', include(router_v1.urls)),
]
