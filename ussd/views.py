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
        # 1*1*1 
        level = text.split('*')
        category = text[:3]
        response =""
        #  main menu for our application
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
        elif text == '1*2':
            response = "CON HITAMO IBYO UKENEYE\n"
            response += "1. IBIKORESHO BY'ISUKU\n"
            response += "2. IBYOKURYA\n"
            response += "3. IBYOKUNYWA\n"




        # SELECT * FROM PRODUCTMODEL where title="" ORDER BY ID DESC LIMIT 5
        #     fetchProducts = ProductsModel.objects.all()
        #     response = "CON ANDIKA IMYIRONDORO YAWE \n"
        #     for  products in fetchProducts:
        #         response += ""+str(products.id)+"."+str(products.title)+ "\n"
        #
        # elif text == '1*1':
        #     product="AMAZINA"
        #     response = "CON shyiramo ubuso bw'ubutaka bwawe bw' "+str(product)+"\n"
        # elif category =='1*1' and int(len(level)) == 3 and str(level[2]) in  str(level):
        #     response = "CON Uwo mubufatanyije \n"
        # elif category =='1*1' and int(len(level)) == 4 and str(level[3]) in  str(level):
        #     response = "CON Shyiramo nimero y'irangamuntu yuwo mufatanyije \n"
        # elif category =='1*1' and int(len(level)) == 5 and str(level[4]) in  str(level):
        #     # save the data into the database
        #     category='Ibinyomoro'
        #     sizeOfland=level[2]
        #     names= level[3]
        #     idnumber = level[4]
        #     insert = Idafarmuser(sessiondId=session_id,
        #     serviceCode = service_code,
        #     phoneNumber=phone_number,
        #     level=level,
        #     category=category,
        #     sizeOfland=sizeOfland,
        #     names=names,
        #     idnumber=idnumber,
        #     )
        #     insert.save()
        #     response = "END Murakoze kwiyandikisha kuri Ida farm \n"
        #
        #
        # elif text == '1*2':
        #     product ="Indimu"
        #     response ="CON shyiramo ubuso bw'ubutaka bwawe bw' "+str(product)+"\n"
        # elif category =='1*2' and int(len(level)) == 3 and str(level[2]) in  str(level):
        #     response = "CON Uwo mubufatanyije \n"
        # elif category =='1*2' and int(len(level)) == 4 and str(level[3]) in  str(level):
        #     response = "CON Shyiramo nimero y'irangamuntu yuwo mufatanyije \n"
        # elif category =='1*2' and int(len(level)) == 5 and str(level[4]) in  str(level):
        #     category='Indimu'
        #     sizeOfland=level[2]
        #     names= level[3]
        #     idnumber = level[4]
        #     insert = Idafarmuser(sessiondId=session_id,
        #     serviceCode = service_code,
        #     phoneNumber=phone_number,
        #     level=level,
        #     category=category,
        #     sizeOfland=sizeOfland,
        #     names=names,
        #     idnumber=idnumber,
        #     )
        #     insert.save()
        #     response = "END Murakoze kwiyandikisha kuri Ida farm \n"
        #
        # #  ======================== INGENGABIHE==================
        # elif text == '2':
        #     response = "CON Hitamo igihe \n "
        #     response += "1. Rimwe mukwezi \n"
        #     response += "2. Kabiri Mukwezi \n"
        #     response += "3. Buri gihe"
        # elif text == '2*1':
        #     # save the data
        #     insertData(
        #         category='Rimwe',
        #         sessionID=session_id,
        #         phoneNumber=phone_number
        #     )
        #     response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe rimwe mukwezi"
        # elif text == '2*2':
        #     insertData(
        #         category='Kabiri',
        #         sessionID=session_id,
        #         phoneNumber=phone_number
        #     )
        #     response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe kabiri mukwezi"
        # elif text == '2*3':
        #     insertData(
        #         category='Burigihe',
        #         sessionID=session_id,
        #         phoneNumber=phone_number
        #     )
        #     response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe Buri munsi"

        else:
            response = "END Ukanze ibitaribyo, ongera mukanya"
        return HttpResponse(response)
    else:
        return HttpResponse('we are on ussd app')
