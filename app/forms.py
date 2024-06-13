from django import forms

#Admin
class adminloginform(forms.Form):
    email = forms.EmailField(max_length=50)
    pwd = forms.CharField(max_length=20)

class addtrainerform(forms.Form):
    tname = forms.CharField(max_length=20)
    tage = forms.IntegerField()
    tphone = forms.CharField(max_length=10)
    temail = forms.EmailField(max_length=25)
    tadm = forms.CharField(max_length=34)


#trainer

class trainerloginform(forms.Form):
    email = forms.EmailField(max_length=50)
    pwd = forms.CharField(max_length=20)

