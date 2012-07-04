from django.conf.urls.defaults import *

from views import group_list, group_info, group_member_operations, \
    group_members, msg_reply, msg_reply_new

urlpatterns = patterns('',
    url(r'^(?P<group_id>[\d]+)/$', group_info, name='group_info'),
    url(r'^reply/(?P<msg_id>[\d]+)/$', msg_reply, name='msg_reply'),
    url(r'^reply/new/$', msg_reply_new, name='msg_reply_new'),
    url(r'^(?P<group_id>[\d]+)/members/$', group_members, name='group_members'),
    (r'^(?P<group_id>[\d]+)/member/(?P<user_name>[^/]+)/$', group_member_operations),
)