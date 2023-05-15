from django.http import HttpResponse
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import KayitFormu , Muskayitform
from .models import kayit
from django.core.paginator import Paginator




# Create your views here.


def home(request):
    #Kayıtları Anasayfaya çekme
    Records=kayit.objects.all()

    # Giriş sağlama kontrolü
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Kimlik Doğrulama
        user = authenticate(request, username=username, password=password)
        # bilgiler Doğru değil /Giriş yapılmadıysa
        if user is not None:
            login(request, user)
            messages.success(request, "Giriş Başarıyla gerçekleştirildi.!")
            return redirect('home')
        else:
            messages.success(
                request, "Bilgileriniz hatalı lütfen kontrol sağlayarak tekrardan deneyiniz.")
            return redirect('home')
    else:
        # return render(request, 'home.html', {})
        return render(request, 'home.html', {'kayitlar' : Records})


def logout_user(request):
    # Oturumu sonlandırma
    logout(request)
    # Başarılı bir şekilde çıkış yapıldığını kullanıcıya bildirme
    messages.success(request, "Çıkış Başarıyla Gerçekleştirildi.!")
    return redirect('home')

# kayıt Bölümü

def register_user(request):
	if request.method == 'POST':
		form = KayitFormu(request.POST)
		if form.is_valid():
			form.save()
			# Yetkilendirme ve giriş
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Kayıt Başarılı bir şekilde gerçekleştirildi Hoş Geldiniz.!!")
			return redirect('home')
	else:
		form = KayitFormu()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


        

def success(request):
    return render(request, 'home.html')


def customer_rec(request, pk):
    if request.user.is_authenticated:
        customer_rec=kayit.objects.get(id=pk)
        return render(request, 'record.html', {'customer_rec':customer_rec})
    else:
        messages.success(request, "Sayfayı görüntüleyebilmek için öncelikle giriş sağlamanız gerekmektedir..!")
        return redirect('home')
    

def delete_customer_rec(request, pk):
    if request.user.is_authenticated:
        sil=kayit.objects.get(id=pk)
        sil.delete()
        messages.success(request, "Kayıt başarılı bir şekilde silinmiştir...")
        return redirect('home')
    else:
        messages.success(request, "İşlemi tamamlayabilmek için giriş sağlayın")
        return redirect('home')

        
def mus_ekle(request):
    form= Muskayitform(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                mus_ekle=form.save()
                messages.success(request ,"Kayıt Eklendi...")
                return redirect('home')
        return render(request ,'mus_ekle.html',{'form':form})
    else:
        messages.success(request ,"HATA..! Lütfen giriş sağladıktan sonra tekrar deneyiniz.")
        return redirect('home')
    
    
def update_mus(request, pk):
    if request.user.is_authenticated:
        mevcutkayit = kayit.objects.get(id=pk)
        form = Muskayitform(request.POST or None, instance=mevcutkayit)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Kayıt başarılı bir şekilde güncellendi...")
            return redirect('home')
        return render(request, 'update_musteri.html', {'form': form})
    else:
        messages.success(
            request, "HATA..! Lütfen giriş sağladıktan sonra tekrar deneyiniz.")
        return redirect('home')


    
    

