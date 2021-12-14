from django.http.response import HttpResponse
from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .iteganya import *
# Create your views here.
def  welcome(request):
    return render(request, 'index.html')

#  python3 -m pip install africastalking
AfricasUsername='bukusenge@gmail.com'
api_key ='673524a8196c675fc322308124f25d1daf370b6faa5bb923b556ff1898939637'
africastalking.initialize(AfricasUsername,api_key)

@csrf_exempt
def ussdApp(request):

    if request.method == 'POST':

        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST['text']
        level = text.split('*')
        category = text[:3]

        if text == '':
            response =  "  CON Murakaza neza kuri Home Needs USSD app \n"
            response += "1. GUSABA DELIVERY \n"
            response += "2. KWISHYURA \n"
        elif text == '1':
            response= "CON HITAMO ISOKO  :\n"
            response += "1. NYARUGENGE \n"
            response += " 2. NYAMIRAMBO\n"
        elif text =='1*1':
            response="CON HITAMO IBYO UKENEYE\n"
            response +="1. IBIKORESHO BY'ISUKU\n"
            response +="2. IBYOKURYA\n"
            response +="3. IBYOKUNYWA\n"
        elif text == '1*1*1':
            response = "CON HITAMO IBIKORESHO BY'ISUKU\n"
            response += "1. ISABUNE\n"
            response += "2. UMUTI WOKOZA UBWIHERERO\n"
        elif text == '1*1*2':
            response ="CON HITAMO IBYOKURYA\n"
            response += "1. IMBOGA\n"
            response += "2. IMBUTO\n"
        elif text == '1*1*3':
            response =  " 1.CON HITAMO IBYOKUNYWA\n"
            response +="1. AMAZI YOKUNYWA\n"
            response +="2. UMUTOBE\n"

        else:
            response = "END Ukanze ibitaribyo, ongera mukanya"
        return HttpResponse(response)
    else:
        return HttpResponse('we are on ussd app')
