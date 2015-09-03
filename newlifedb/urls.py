from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .settings import MEDIA_ROOT, DEBUG

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newlifedb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'newlife.views.children.children_list', name='home'),
	url(r'^children/(?P<sid>\d)/edit/$','newlife.views.children.children_edit', name = 'children_edit'),
	url(r'^children/(?P<sid>\d)/delete/$','newlife.views.children.children_delete', name = 'children_delete'),
    # url(r'^blog/', include('blog.urls')),
    #Student urls
    # url(r'^students/add/$', StudentCreateView.as_view(),name='students_add'),

    # url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(),name='students_edit'),

    url(r'^admin/', include(admin.site.urls)),

    #Group urls
    url(r'^supporters/$', 'newlife.views.supporters.supporters_list',name='supporters_list'),

    # url(r'^groups/add/$', 'students.views.groups.groups_add',name='groups_add'),

    # url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups.groups_edit',name='groups_edit'),


    url(r'^admin/', include(admin.site.urls)),

)


urlpatterns += staticfiles_urlpatterns()

if DEBUG:
# serve files from media folder 
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT}))