# forms.py
from django import forms
from .models import *


class BlogUpdateFormOne(forms.ModelForm):
    class Meta:
        model = BlogPostOne
        fields = ['index', 'title', 'description', 'img_path_1', 'img_path_2',
                  'img_path_3', 'img_1', 'img_2', 'img_3', 'affiliate_link']


class BlogUpdateFormTwo(forms.ModelForm):
    class Meta:
        model = BlogPostTwo
        fields = ['index', 'title', 'description', 'img_path_1', 'img_path_2',
                  'img_path_3', 'img_1', 'img_2', 'img_3', 'affiliate_link']


class BlogUpdateFormThree(forms.ModelForm):
    class Meta:
        model = BlogPostThree
        fields = ['index', 'title', 'description', 'img_path_1', 'img_path_2',
                  'img_path_3', 'img_1', 'img_2', 'img_3', 'affiliate_link']


class BlogUpdateFormFour(forms.ModelForm):
    class Meta:
        model = BlogPostFour
        fields = ['index', 'title', 'description', 'img_path_1', 'img_path_2',
                  'img_path_3', 'img_1', 'img_2', 'img_3', 'affiliate_link']


class BlogUpdateFormFive(forms.ModelForm):
    class Meta:
        model = BlogPostFive
        fields = ['index', 'title', 'description', 'img_path_1', 'img_path_2',
                  'img_path_3', 'img_1', 'img_2', 'img_3', 'affiliate_link']


class BlogUpdateFormSix(forms.ModelForm):
    class Meta:
        model = BlogPostSix
        fields = ['index', 'title', 'description', 'img_path_1', 'img_path_2',
                  'img_path_3', 'img_1', 'img_2', 'img_3', 'affiliate_link']


class BlogUpdateFormSeven(forms.ModelForm):
    class Meta:
        model = BlogPostSeven
        fields = ['index', 'title', 'description', 'img_path_1', 'img_path_2',
                  'img_path_3', 'img_1', 'img_2', 'img_3', 'affiliate_link']


class BlogUpdateFormEight(forms.ModelForm):
    class Meta:
        model = BlogPostEight
        fields = ['index', 'title', 'description', 'img_path_1', 'img_path_2',
                  'img_path_3', 'img_1', 'img_2', 'img_3', 'affiliate_link']


class BlogUpdateFormNine(forms.ModelForm):
    class Meta:
        model = BlogPostNine
        fields = ['index', 'title', 'description', 'img_path_1', 'img_path_2',
                  'img_path_3', 'img_1', 'img_2', 'img_3', 'affiliate_link']
