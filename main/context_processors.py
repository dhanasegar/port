from .models import SocialMediaLink

def social_links(request):
    social_media = SocialMediaLink.objects.first()
    return {'social_media': social_media}
    