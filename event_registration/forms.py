from django.forms import ModelForm
from .models import Registrant
from bootstrap_modal_forms.forms import BSModalModelForm

class RegistrationForm(BSModalModelForm):
    class Meta:
        model = Registrant
        fields = '__all__'