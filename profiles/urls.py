from django.urls import path
from .views import my_profile_view, invites_received_view, profiles_list_view, to_invite_profiles_list_view, \
    ProfileListView, send_invitation, remove_from_friends, accept_invitation, reject_invitation, ProfileDetailView

app_name = 'profiles'

urlpatterns = [
    path('', ProfileListView.as_view(), name='all_profiles_view'),
    path('myprofile/', my_profile_view, name='my_profile_view'),
    path('my-invites/', invites_received_view, name='my_invites_view'),
    path('to-invite/', to_invite_profiles_list_view, name='to_invite_profiles_view'),
    path('send-invite/', send_invitation, name='send_invite'),
    path('remove-friend/', remove_from_friends, name='remove_friend'),
    path('<slug>/', ProfileDetailView.as_view(), name='profile_detail_view'),
    path('my-invites/accept/', accept_invitation, name='accept_invite'),
    path('my-invites/reject/', reject_invitation, name='reject_invite'),
]
