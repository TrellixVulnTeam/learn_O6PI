from django import forms
from .models import  Member, Author, TITLE_CHOICES, Choice, Question

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)

class UserUpdate(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class MemberForm(forms.ModelForm):
    class Meta:
          model = Member
          fields = "__all__"
class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    title = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=TITLE_CHOICES),
    )
    birth_date = forms.DateField(required=False)

class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(),widget=forms.CheckboxSelectMultiple, label="Author Name ")

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"

class ChoiceForm(forms.ModelForm):
    question = forms.ModelChoiceField(queryset=Question.objects.all(), empty_label=None)
    date = forms.DateField(widget=forms.DateInput, help_text="M/D/Y Fromat Add Value")
    CHOICES = [('M', 'Male'), ('F', 'Female')]
    Gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    file = forms.FileField()

    class Meta:
        model = Choice
        fields = "__all__"
