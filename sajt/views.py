from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request,'index.html',{})


def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        telefon = request.POST['telefon']

        message = request.POST['message']
        message2 = telefon+ ' '+message
        context = {'name':name, 'telefon':telefon, 'message':message2}

        send_mail (
            name,
            message2,
            telefon,
            ['deciji.lekar.slobodanka@gmail.com',
            'mailservispedijatar@gmail.com'],
            fail_silently=False,
        )


        return render(request, 'index2.html',context)



    else:
        return render(request, 'index.html',{})
