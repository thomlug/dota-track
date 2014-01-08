from django.conf.urls import patterns, url


urlpatterns = patterns('',
	url(r'^$', 'dotatrack.views.index', name='index'),
	)

# INITIAL DEFAULT CODE FOLLOWS:

# from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'dotatrack.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# )