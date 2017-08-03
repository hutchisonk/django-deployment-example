from django.conf.urls import url
from basic_app import views

# TEMPLATE TAGGING
app_name = "basic_app"
# THIS APPLICATION NAME IS WHAT NEEDS TO MATCH IN YOUR HTML RELATIVE LINKS

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    # THESE NAME ATTRIBUTES ARE WHAT YOU REFERENCE AFTER THE APP NAME IN HTML REL LINKS
    # AS IN: href="{% url 'basic_app:other'% }"
    url(r'^other/$', views.otherhtmlpage, name='other'),
]
