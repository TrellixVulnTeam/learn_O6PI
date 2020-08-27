from bootstrap_datepicker_plus import DatePickerInput
#from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from captcha.fields import ReCaptchaField
from django import forms
from .models import  Member

class MemberForm(forms.ModelForm):
    #captcha = ReCaptchaField()
    class Meta:
          model = Member
          fields = '__all__'

          date = forms.DateField(
              localize=True,
              widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}),
          )


    def clean(self):

        # data from the form is fetched using super function
        super(MemberForm, self).clean()

        # extract the username and text field from the data
        mobile_len = self.cleaned_data.get('mobile_no')
        age = self.cleaned_data.get('age')
        # conditions to be met for the username length
        if len(mobile_len) != 10:
            self._errors['mobile_no'] = self.error_class([
                'Mobile Number in Only 10 Digit !'])

        if age <= 0:
            self._errors['age'] = self.error_class([
                'Age is Positive'])



        return self.cleaned_data