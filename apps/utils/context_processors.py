from apps.models import User


def socials(request):
    return {
        "socials": User.objects.values_list('social', flat=True),
    }
