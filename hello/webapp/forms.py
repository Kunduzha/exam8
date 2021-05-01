from django import forms
from webapp.models import Goods, Review


class Goodform(forms.ModelForm):
    class Meta:
        model=Goods
        fields=('name', 'description', 'category', 'image')


class GoodDeleteForm(forms.Form):
    name=forms.CharField(max_length=100, required=True, label='Введите название товара чтобы удалить его')



class SimpleSearchForm(forms.Form):

    search = forms.CharField(max_length=100, required=False, label="Найти")

class ReviewForms(forms.ModelForm):

    class Meta:
        model=Review
        fields = ['user', 'text_review', 'rating', 'moderation']