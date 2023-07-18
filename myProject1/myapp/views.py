from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('''Bismillah, 
    <html>
    <head>
    <title>Bismillah</title>
    </head>
    <body>
    <h1>Bismillah</h1>
    <marquee>Assalamualaikum</marquee>
    </body>
    </html>
        
    Assalamualaikum''')