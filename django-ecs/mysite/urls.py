from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin

from django.contrib.auth import views as auth_views

from mysite.core import views as core_views

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),



    url(r'^all/', core_views.index, name='index'),
    path('admin/', admin.site.urls),

    path('add/', core_views.add, name='add'),
    path('<int:event_id>/', core_views.detail, name='detail'),
    path('<int:event_id>/delete/', core_views.delete, name='delete'),
    path('<int:event_id>/edit/', core_views.edit, name='edit'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
