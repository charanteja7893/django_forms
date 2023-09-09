from django import forms
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

    def __str__(self):
        return self.sname