from django.urls import path
from .views import AllShitPosts, Index, Login, Logout

urlpatterns = [
    path('', Index.as_view(), name='Inicio'),
    path('index', Index.as_view(), name='Index'),
    path('login', Login.as_view(), name='Login'),
    path('logout', Logout.as_view(), name='Logout'),
    path('all-shit-posts', AllShitPosts.as_view(), name='AllPosts')
]
