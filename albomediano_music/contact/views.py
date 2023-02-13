from django.http import HttpResponse


def index(request):
    return HttpResponse('email: al.bomediano@obf.ateneo.edu')
