from django.shortcuts import render
from .models import PDF


def root(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def products(request):
    return render(request, 'products.html')


def compressors(request):
    return render(request, 'compressors.html')


def fittings(request):
    return render(request, 'fittings.html')


def gaskets(request):
    return render(request, 'gaskets.html')


def flanges(request):
    return render(request, 'flanges.html')


def valves2(request):
    return render(request, 'valves2.html')


def pipes(request):
    return render(request, 'pipes.html')


def instrumentation(request):
    return render(request, 'instrumentation.html')


def electricals(request):
    return render(request, 'electricals.html')


def valves(request):
    return render(request, 'valves.html')


def checkout(request):
    return render(request, 'checkout.html')


def contacto(request):
    return render(request, 'contacto.html')


def attachment(request):
    pdf = PDF.objects.first()
    return render(request, 'attachment.html', {'pdf': pdf})


def news(request):
    return render(request, 'news.html')


def user_registration(request):
    return render(request, 'user-registration.html')


def client(request):
    return render(request, 'client.html')


def cart(request):
    return render(request, 'cart.html')


def online_store(request):
    return render(request, 'online-store.html')


def terms_and_conditions(request):
    return render(request, 'terms-and-conditions.html')


def privacy_policy(request):
    return render(request, 'privacy-policy.html')
