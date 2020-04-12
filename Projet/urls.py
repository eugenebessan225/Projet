from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pro_it.urls')),
    path('', auth_views.LoginView.as_view(template_name="connexion.html"),
         name='connexion'),
    path('changer-mot-de-passe/', auth_views.PasswordChangeView.as_view(template_name="compte/password_change_form.html"),
         name='password_change'),
    path('changer-mot-de-passe-terminer/', auth_views.PasswordChangeDoneView.as_view(template_name="compte/password_change_done.html"),
         name='password_change_done'),
    path('reinitialiser-mot-de-passe/', auth_views.PasswordResetView.as_view(
        template_name='compte/password_reset.html'), name='password_reset'),
    path('reinitialiser-mot-de-passe/terminer/', auth_views.PasswordResetDoneView.as_view(
        template_name='compte/password_reset_done.html'), name='password_reset_done'),
    path('reinitialiser-mot-de-passe/confirmer/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='compte/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reinitialiser-mot-de-passe/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='compte/password_reset_complete.html'), name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
