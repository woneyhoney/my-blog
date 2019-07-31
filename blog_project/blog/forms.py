from django import forms
from .models import Blog # 모델 기반 입력 공간

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog # Blog 모델 기반
        fields = ['title', 'body'] # 입력 받을 수 있는 공간

#class BlogPost(forms.Form):
#    email = forms.EmailField()
#    files = forms.FileField()
#    url = forms.URLField()
#    words = forms.CharField(max_length=200)
#    max_number = forms.ChoiceField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three')])