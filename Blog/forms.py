from django import forms
from .models import Comment
class new_comment (forms.ModelForm):
    class Meta :
        model = Comment
        fields = ('name' ,'email','body')