from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .add_view import member_view, member_view1
from .views import UserViewSet, snippet_detail, snippet_list, snippet_list_d, \
    snippet_detail_d, member_list, member_detail, MyRegisterView, grid_view, get_image
from .forms import MemberForm
router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('image-viewer/<str:type>', get_image, name = "member"),
    path('member', member_view, name = "member"),
    path('grid', grid_view, name = "grid"),
    path('add', MyRegisterView.as_view(template_name="member.html", form_class=MemberForm), name = "Add Record"),
    path('member1', member_view1, name = "member"),
    path('memberview', member_list, name = "member_view"),
    path('member-detail/<int:pk>', member_detail, name = "member_details"),
    path('snippets', snippet_list),
    path('snippets/<int:pk>/', snippet_detail),
    path('snippets1', snippet_list_d),
    path('snippets1/<int:pk>/', snippet_detail_d),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]