from .models import Profile, Relationship


def profile_pic(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        pic = profile_obj.avatar
        return {'picture': pic}
    return {}


def invitation_received_number(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        qs_count = Relationship.objects.invatations_received(profile_obj).count()
        return {'invitesNumber': qs_count}
    return {}
