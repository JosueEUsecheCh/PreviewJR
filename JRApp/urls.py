from django.urls import path
from JRApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns= [
    path('', views.index, name='index'),
    path('account/', include('django.contrib.auth.urls')),
    path('registration/', views.user_register, name="registration"),
    path('success/', TemplateView.as_view(template_name='registration/success_registration.html'), name='success'),
    path('login/',views.login,name='login'),
    path('exit/',views.exit,name='exit'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)