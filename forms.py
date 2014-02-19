from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CrispyForm(ModelForm):

    SUBMIT_LABEL = 'Submit'
    HTTP_METHOD = 'post'

    def __init__(self, *args, **kwargs):
        super(CrispyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(Submit('submit', self.SUBMIT_LABEL))
        self.helper.form_method =  self.HTTP_METHOD