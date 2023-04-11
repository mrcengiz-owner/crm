from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.


def home(request):
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
            messages.success(request, "Bilgileriniz hatalı lütfen kontrol sağlayarak tekrardan deneyiniz.")
            return redirect('home')
    else:
        #return render(request, 'home.html', {})
        return render(request, 'home.html', {'messages': messages.get_messages(request)})

    



def logout_user(request):
    # Oturumu sonlandırma
    logout(request)
    # Başarılı bir şekilde çıkış yapıldığını kullanıcıya bildirme
    messages.success(request, "Çıkış Başarıyla Gerçekleştirildi.!")
    return redirect('home')

#kayıt Bölümü
def register_user(request):
    return render(request,"register.html",{})