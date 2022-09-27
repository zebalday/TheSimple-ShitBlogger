from .models import SocialMedia, MiscLinks

""" Obtenemos datos necesarios para el funcionamiento de la página """

def getSocialMedia(request):

    social_media = SocialMedia.objects.filter(public=True)
    return {'SocialMedia':social_media}


def getMiscellaneus(request):

    miscellaneus = MiscLinks.objects.filter(public=True)
    return {'MiscLinks':miscellaneus}