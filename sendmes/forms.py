from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': "form-control form-control-lg", 'placeholder': "Имя отправителя"}))
    to = forms.EmailField(widget=forms.TextInput(attrs={'class': "form-control form-control-lg", 'placeholder': "Email получателя"}))
    comments = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control form-control-lg", 'placeholder': "Комментарий к письму" }))
    timer = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control form-control-lg", 'placeholder': "Время через которое письмо будет отправлено" }))