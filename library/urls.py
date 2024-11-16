from django.urls import path, include
from library import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('users', views.viewsets_user)
router.register('books', views.viewsets_book)
router.register('orders', views.viewsets_order)
router.register('authors', views.viewsets_author)

urlpatterns = [
    path('first', views.no_rest_no_model),
    path('second', views.no_rest_with_model),
    path('fbv/', views.FBV_List),
    path('fbv/<int:pk>', views.FBV_PK),
    path('cbv/', views.CBV_List.as_view()),
    path('cbvorder/', views.CBV_BookList.as_view()),
    path('cbv/<int:pk>', views.CBV_pk.as_view()),
    path('vs/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token ),
]