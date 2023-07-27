from django import forms
from loan.models import Loan


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ["dni", "first_name", "last_name", "gender", "email", "amount"]

    GENDER_CHOICES_ES = [("M", "Masculino"), ("F", "Femenino"), ("O", "Otro")]
    gender = forms.ChoiceField(choices=GENDER_CHOICES_ES, label="Género")


class UpdateLeanForm(LoanForm):
    def save(self, commit=True):
        loan = super().save(commit=False)
        loan.dni = self.instance.dni
        if commit:
            loan.save()
        return loan
