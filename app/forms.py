from django import forms





def validate(data):
    if data.lower().startswith('g'):
        raise forms.ValidationError('starts with g')
    

def validate1(data):
    if len(data)<4:
        raise forms.ValidationError('length lessthan 4')




class Schoolform(forms.Form):
    Sname=forms.CharField(validators=[validate1,validate])
    Sprincipal=forms.CharField()
    Slocation=forms.CharField(validators=[validate1])
    Email=forms.CharField()
    Remail=forms.CharField()

    def validate2(self):
        em=self.cleaned_data['Email']
        rem=self.cleaned_data['Remail']
        if em!=rem:
            raise forms.ValidationError('email not matched')