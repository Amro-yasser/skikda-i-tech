from django import forms
from tinymce import TinyMCE
from .models import Event


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Event
        fields = ('__all__')


#class SignupForm(forms.Form):
#    first_name = forms.CharField(max_length=30, label='First name')
#    last_name = forms.CharField(max_length=30, label='Last Name')
#
#    def signup(self, request, user):
#        user.first_name = self.cleaned_data['first_name']
#        user.last_name = self.cleaned_data['last_name']
#        user.save()