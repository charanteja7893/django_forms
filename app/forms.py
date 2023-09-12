from django import forms
from django.core import validators
def check_for_a(value):
    if value[0]=='c':
        raise forms.ValidationError('start with c')

def check_for_age(value):
    if value <20:
        raise forms.ValidationError('age must and should be >20')
def check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('length must be >5')
    

class student_forms(forms.Form):
    sname=forms.CharField(max_length=100,validators=[check_for_a,check_for_len])
    sid=forms.IntegerField()
    sage=forms.IntegerField(validators=[check_for_age])
    semail=forms.EmailField()
    srenteremail=forms.EmailField()
    mobile=forms.CharField(min_length=10,max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)


    def __str__(self):
        return self.sname
    
    def clean(self):
        e=self.cleaned_data['semail']
        r=self.cleaned_data['srenteremail']

        if e!=r:
            raise forms.ValidationError('inncorect')

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot')
    