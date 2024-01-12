from django import forms

class TeacherRegistration(forms.Form):
    first_name = forms.CharField(label='Enter Your First Name')
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput)
    Checkbox = forms.CharField(widget=forms.CheckboxInput)