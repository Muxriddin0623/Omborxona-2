from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('m_nomi', 'turi', 'ogirligi',)
        labels = {
            'm_nomi': 'Mahsulot nomi',
            'turi': 'Turi',
            'ogirligi': 'Ogirligi KG da'
        }

    def __int__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['ogirligi'].empty_label = ""
        self.fields['turi'].required = False
