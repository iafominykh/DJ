from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'category', 'preview_image', 'specification')

    def clean_title(self):
        forbidden_words = ['эротика', 'порно', 'прон', 'porn', 'erotic', 'дурак', 'какоетослово', 'тестовоеслово',
                           'pepper']
        cleaned_title = self.cleaned_data['title']
        for word in forbidden_words:
            if word in cleaned_title.lower():
                raise forms.ValidationError('Недопустимое слово в названии продукта: {}'.format(word))
        return cleaned_title

    def clean_specification(self):
        forbidden_words = ['эротика', 'порно', 'прон', 'porn', 'erotic', 'дурак', 'какоетослово', 'тестовоеслово',
                           'pepper']
        cleaned_specification = self.cleaned_data['specification']
        for word in forbidden_words:
            if word in cleaned_specification.lower():
                raise forms.ValidationError('Недопустимое слово в описании продукта: {}'.format(word))
        return cleaned_specification


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('version_number', 'version_title',)
