from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record



class KayitFormu(UserCreationForm):
    email=forms.forms.EmailField(Label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Adresiniz'}))
    isim=forms.CharField(Label="", max_length=150, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'İsminiz'}))
    soyisim=forms.CharField(Label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Soyadınız'}))

    class Meta:
        model=User
        fields=('username', 
                'first_name', 
                'Last_name',
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
