from django.forms import ModelForm, TextInput, Textarea, NumberInput, CheckboxInput, FileInput, ValidationError
from .models import Advertisement

class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ('title', 'description', 'price', 'auction', 'image')
        widgets = {
            'title': TextInput(attrs={'class':'form-control form-control-lg'}),
            'description': Textarea(attrs={'class':'form-control form-control-lg'}),
            'price': NumberInput(attrs={'class':'form-control form-control-lg'}),
            'auction': CheckboxInput(attrs={'class':'form-check-input'}),
            'image': FileInput(attrs={'class':'form-control form-control-lg'})
        }
    def clean_title(self):
        data = self.cleaned_data['title']
        if data.startswith('?'):
            raise ValidationError('Название не может начинаться с "?"')
        return data
