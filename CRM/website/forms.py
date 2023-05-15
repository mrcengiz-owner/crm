from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import kayit


class KayitFormu(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Adresiniz'}))
    first_name = forms.CharField(label="", max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'İsminiz'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Soyadınız'}))

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')

    def __init__(self, *args, **kwargs):

        super(KayitFormu, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Kullanıcı Adınız..'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Gereksinim. Karakter sayısı 150 den az olmalıdır. Sadece harfler, rakamlar ve @/./+/-/_ karakterleri kullanılabilir.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Şifreniz'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Şifreniz diğer kişisel bilgilerinize çok benzer olamaz.</li><li>Şifreniz en az 8 karakter içermelidir.</li><li>Şifreniz sık kullanılan bir şifre olamaz.</li><li>Şifreniz tamamen sayılardan oluşamaz.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Şifrenizi tekrarlayın..'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Öncekiyle aynı şifreyi teyit etmek için girin</small></span>'

# müşteri kayıt formu


class Muskayitform(forms.ModelForm):
    isim = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Müşteri İsmi", "class": "form-control"}), label="")
    soyisim = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Müşteri Soyadı", "class": "form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Email Adresi", "class": "form-control"}), label="")
    telefon = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Telefon Numarası", "class": "form-control"}), label="")
    adres = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Adresi", "class": "form-control"}), label="")
    il = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "İli", "class": "form-control"}), label="")
    ilce = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "İlçesi", "class": "form-control"}), label="")
    postakod = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Posta Kodu", "class": "form-control"}), label="")

    class Meta:
        model = kayit
        exclude = ("user",)
