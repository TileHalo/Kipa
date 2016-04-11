from django.conf.urls.defaults import patterns

SARJA = "(?P<sarja_id>[^/]+)/"
KISA = "(?P<kisa_nimi>[^/]+)/"
urlpatterns = patterns('aikalaskuri.views',
    (r'^$', 'index'),
    (r'^(?P<kisa_nimi>[^/]+)/$', 'kisa'),
    (r'^' + KISA + SARJA + 'syota/(?P<tehtava_id>\d+)', 'syota'),
    (r'^' + KISA + SARJA + 'maarita/(?P<tehtava_id>\d+)', 'maarita'),
    (r'^' + KISA + SARJA, 'sarja'),
)
