from django.urls import path
from .views import my_profile_view, invites_received_view, profiles_list_view, to_invite_profiles_list_view, \
    ProfileListView, send_invatation, remove_from_friends

app_name = 'profiles'

urlpatterns = [
    path('myprofile/', my_profile_view, name='my_profile_view'),
    path('my-invites/', invites_received_view, name='my_invites_view'),
    path('all-profiles/', ProfileListView.as_view(), name='all_profiles_view'),
    path('to-invite/', to_invite_profiles_list_view, name='to_invite_profiles_view'),
    path('send-invite/', send_invatation, name='send_invite'),
    path('remove-friend/', remove_from_friends, name='remove_friend'),
]
