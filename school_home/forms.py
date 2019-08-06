from django import forms

class AddAccessForm():
	acc_type = forms.CharField()

	class Meta():
		model = Access
		fiels = ['acc_type']
			
