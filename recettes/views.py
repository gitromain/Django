from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, RecetteForm, IngredientFormset, EtapeFormset, NoteForm, CommentaireForm
from .models import Recette, Ingredient, Etape, Note, Commentaire
from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import inlineformset_factory
from django.forms.formsets import formset_factory
from django.db.models import Avg
from recettes.views import Recette
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_list_or_404, get_object_or_404
from django.forms.models import modelformset_factory

def index(request):
    return render(request, 'recettes/index.html')

# RECETTE PART
def afficher(request):
    recettes = Recette.objects.all();
    typeObjet=None
    paginator = Paginator(recettes, 10)
    page = request.GET.get('page')
    try:
        recettes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        recettes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        recettes = paginator.page(paginator.num_pages)
    contexte = {
        'typeObjet': typeObjet,
        'recettes': recettes,
    }
    return render(request, 'recettes/afficher.html', contexte)

def consulter(request, id):

    if (request.method == 'POST'):
        note_form = NoteForm(request.POST)
        commentaire_form = CommentaireForm(request.POST)

        if note_form.is_valid():
            note = note_form.save()
            note.id_recette = Recette.objects.get(id=id)
            note.user = request.user
            note.save()

        if commentaire_form.is_valid():
            commentaire = commentaire_form.save()
            commentaire.id_recette = Recette.objects.get(id=id)
            commentaire.user = request.user
            commentaire.save()

    recette = Recette.objects.get(id=id)
    etapes = Etape.objects.filter(id_recette=id)
    ingredients = Ingredient.objects.filter(id_recette=id)
    note = Note.objects.filter(id_recette=id).aggregate(Avg('valeur'))
    noted = 0
    if(request.user.is_authenticated()):
        noted = Note.objects.filter(id_recette=id, user=request.user).count()
    form_note = ''
    if noted == 0:
        form_note = NoteForm();
    commentaires = Commentaire.objects.filter(id_recette=id)
    form_com = CommentaireForm();

    contexte = {
        'recette'    : recette,
        'etapes'     : etapes,
        'ingredients': ingredients,
        'notes'     : note,
        'commentaires'     : commentaires,
        'form_note': form_note,
        'form_com': form_com,
    }
    return render(request, 'recettes/consulter.html', contexte)

def ajouter(request):

    MainForm = RecetteForm()
    IngredientForm = IngredientFormset()
    EtapeForm = EtapeFormset()

    if request.method == 'POST':
        MainForm = RecetteForm(request.POST)
        if MainForm.is_valid():
            recette = MainForm.save()
            recette.user = request.user
            recette.save()
            IngredientForm = IngredientFormset(request.POST,instance=recette)
            if IngredientForm.is_valid():
                IngredientForm.save()
                if EtapeForm.is_valid():
                    EtapeForm.save()
                    return render(request, "recettes/ajouter.html", {
                        'MainForm': MainForm,
                        'IngredientForm': IngredientForm,
                        'EtapeForm': EtapeForm,
                        'create_success':'success'
                    })

    return render(request, "recettes/ajouter.html", {
        'MainForm': MainForm,
        'IngredientForm': IngredientForm,
        'EtapeForm': EtapeForm,
    })


# USER PART
def auth(request):
    if (request.method == 'POST'):
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password1'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            contexte = {
                'form': AuthenticationForm,
                'auth_success':'success'
            }
            return render(request, 'registration/login.html', contexte)
    else:
        user_form = RegistrationForm()
    contexte = {
        'formulaire_user': user_form,
    }
    return render(request, 'registration/auth.html', contexte)
