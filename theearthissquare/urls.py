from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import views as auth_views
from website import views as website
from dashboard import views as dashboard
from django.contrib.auth import logout
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings

urlpatterns = [

    path('', website.home, name='home'),

    path('', include('registration.backends.simple.urls')), # Figure out why this is needed to use the auth_logout link.

    path('admin/', admin.site.urls),

    path('team/', website.team, name='team'),

    path('services/', website.services, name='services'),

    path('services/<parsed_name>/', website.service, name='service'),

    path('portfolio/', website.portfolio, name='portfolio'),

    path('portfolio/<parsed_client>/', website.project, name='project'),

    path('contact/', website.contact, name='contact'),

    path('dashboard/', dashboard.dashboard, name='dashboard'),

    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),

    url(r'^s3direct/', include('s3direct.urls')),

    url(r'^tinymce/', include('tinymce.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
