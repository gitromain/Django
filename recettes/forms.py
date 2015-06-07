from django import forms
from .models import Recette, Ingredient, Etape, Note, Commentaire
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RecetteForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Recette

class EtapeCustomForm(forms.ModelForm):
    required_css_class = 'required'
    libelle = forms.CharField(required = True, widget=forms.Textarea(attrs={'cols': 50, 'rows': 4}))
    class Meta:
        model = Etape

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['valeur']


class CommentaireForm(forms.ModelForm):
    libelle = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 4}))
    class Meta:
        model = Commentaire
        fields = ['libelle']


IngredientFormset = inlineformset_factory(Recette, Ingredient, can_delete=False)
EtapeFormset = inlineformset_factory(Recette, Etape,form=EtapeCustomForm, can_delete=False)


class RegistrationForm(UserCreationForm):
    required_css_class = 'required'
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True, label="Prénom")
    last_name = forms.CharField(required = True, label="Nom")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self,commit = True):
        user = super(RegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user