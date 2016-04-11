# Create your views here.
from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from tupa import models as tupa

def index(request):
    """
    Choose Kisa
    """
    kisat = tupa.Kisa.objects.all()
    return render(request, "aikalaskuri/index.html", {"kisat": kisat})


def kisa(request, kisa_nimi):
    """
    Edit calculating main page for kisa
    """
    kisa = get_object_or_404(tupa.Kisa, nimi=kisa_nimi)
    sarjat = kisa.sarja_set.all()
    return render(request, "aikalaskuri/kisa.html", {"sarjat": sarjat,
                                                     "nimi": kisa_nimi})


def sarja(request, kisa_nimi, sarja_id):
    kisa = get_object_or_404(tupa.Kisa, nimi=kisa_nimi)
    sarja = kisa.sarja_set.get(id=sarja_id)
    tehtavat = sarja.tehtava_set.all()
    return render(request, "aikalaskuri/sarja.html", {"tehtavat": tehtavat})


def maarita(request, tehtava_id, kisa_nimi=None, sarja_id=None):
    """
    Edit calculating
    """
    tehtava = get_object_or_404(tupa.Tehtava, id=tehtava_id)
    otehtavat = tehtava.osatehtava_set.all()
    maaritteet = []
    for ot in otehtavat:
        nimet = ot.syotemaarite_set.all()
        maaritteet.append({"id": ot.id,
                           "nimi": [nimi for nimi in nimet]})
    return render(request, "aikalaskuri/maarita.html", {"tehtavat": maaritteet
                                                       })


def syota(request, tehtava_id, kisa_nimi=None, sarja_id=None):
    """
    Insert times
    """
    kisa = get_object_or_404(tupa.Kisa, nimi=kisa_nimi)
    return HttpResponseNotFound(request)
