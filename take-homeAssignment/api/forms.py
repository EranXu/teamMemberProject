from django.forms import ModelForm
from .models import TeamMember
from phonenumber_field.modelfields import PhoneNumberField


class MemberForm(ModelForm):
	class Meta:
		model = TeamMember
		fields = ['fullName', 'phone', 'email','canDelete']
