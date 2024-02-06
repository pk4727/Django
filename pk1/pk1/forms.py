from django import forms
    
class d_forms(forms.Form):
    input=forms.CharField(label="input1",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
    input2=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    input3=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    email=forms.EmailField(required=False)
    bool=forms.BooleanField()

class user_inputss(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    subject = forms.CharField(widget=forms.TextInput)
    date = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)