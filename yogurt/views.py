from django.http import HttpResponse
from pagesManager.views import *
from yogurt.models import *
import email, smtplib, ssl
from yogurt.providers import PROVIDERS
import re


def format_tel(tel):
    tel = str(tel)
    tel = tel.removeprefix("+")
    tel = tel.removeprefix("1")     # remove leading +1 or 1
    tel = re.sub("[ ()-]", '', tel) # remove space, (), -

    #assert(len(tel) == 10)
    #tel = f"{tel[:3]}-{tel[3:6]}-{tel[6:]}"

    return tel


def yogurt_view(request):
    if not check_authenticate(request):
        return redirect('/login_view/')
    profile = Profile.objects.get(user_name=request.user)

    context = {'posts': profile, }
    return render(request, 'yogurt_view.html', context)


def yogurt_index(request):
    if not check_authenticate(request):
        return redirect('/login_view/')
    profile = Profile.objects.get(user_name=request.user)

    context = {'posts': profile, }
    return render(request, 'index.html', context)


def yogurt_set_checkIn(request):
    if not check_authenticate(request):
        return redirect('/login_view/')
    inputCheckInPhone = request.POST.get('inputCheckInPhone')
    inputRegPhone = request.POST.get('inputRegPhone')
    inputRegProvider = request.POST.get('inputRegProvider')
    inputRegName = request.POST.get('inputRegName')
    inputRegEmail = request.POST.get('inputRegEmail')
    inputRegDateOfBirth = request.POST.get('inputRegDateOfBirth')
    now = datetime.now()
    Res = ""
    CusName = ""
    if 'action' in request.POST:
        if request.POST['action'] == 'CheckIn':
            #checkInCus = CusData.objects.filter(id=id)
            try:
                checkInCus = CusData.objects.get(phone=inputCheckInPhone)
                #checkInCus = CusData.objects.filter(phone=inputCheckInPhone).first()
                checkInCus.last_check_in = now.strftime('%H:%M:%S %d/%B/%Y') 
                checkInCus.save()
                Res = "CheckInSuccess"
                CusName = checkInCus.name
                CheckInD = CheckInData.objects.create(phone=inputCheckInPhone)
                CheckInD.checkInTime = now.strftime('%H:%M:%S %d/%B/%Y')
                CheckInD.idCus = checkInCus.id
                CheckInD.name = checkInCus.name
                CheckInD.save()
            except CusData.DoesNotExist:
                Res = "CheckInFail"            
            #messages.success(request, 'Wellcome '+ checkInCus.name)
        else:
            if (CusData.objects.filter(phone=inputRegPhone).first()) or (inputRegProvider == "") or (inputRegPhone == "") :
                Res = "RegisterFail" 
            else:
                regCus = CusData.objects.create(name=inputRegName, phone=inputRegPhone)
                regCus.email = inputRegEmail
                regCus.dateOfbirth = inputRegDateOfBirth
                regCus.provider = inputRegProvider
                regCus.save()
                Res = "RegisterSuccess" 
    request.session['Result'] = Res
    request.session['CusName'] = CusName
    return redirect('/yogurt_checkIn/')
    #return render(request, 'yogurt_checkIn.html', context)


def yogurt_checkIn(request):
    if not check_authenticate(request):
        return redirect('/login_view/')
    context = {
               'Res': request.session['Result'],
               'CusName': request.session['CusName'],
            }
    return render(request, 'yogurt_checkIn.html', context)


def yogurt_cus_view(request):
    if not check_authenticate(request):
        return redirect('/login_view/')
    posts = CusData.objects.all()
    all_cus_list =  []
    for cus in posts:
        add = ["", cus.id, cus.name, str(cus.phone), cus.email, cus.dateOfbirth, cus.point, cus.coupon, cus.last_check_in]
        all_cus_list.append(add)
    context = {'posts': posts, 
                'all_cus_list': all_cus_list, 
                }
    return render(request, 'yogurt_cus_view.html', context)


def yogurt_sent_sms(request):
    if not check_authenticate(request):
        return redirect('/login_view/')
    if 'action' in request.POST:
        sms_sent_list = request.POST.get('sms_sent_list')
        sms_content = request.POST.get('sms_content')
        sms_subject = request.POST.get('sms_subject')       
        try:
            arr_sent_list = sms_sent_list.split(',')
            for id_cus in arr_sent_list:
                Cus_obj = CusData.objects.get(id=id_cus)             
                number = format_tel(Cus_obj.phone)
                message = sms_content
                provider = Cus_obj.provider
                sender_credentials = ("dogananguyen@gmail.com", "xalkapvjfdmmfsfg")
                try:
                    send_sms_via_email(number, message, provider, sender_credentials, sms_subject)
                except Exception as e: 
                    print(e)
        except Exception as e: 
            print(e)
    return redirect('/yogurt_cus_view/')


def send_sms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    subject: str ,
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
    ):
    sender_email, email_password = sender_credentials
    receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'

    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(
        smtp_server, smtp_port, context=ssl.create_default_context()
    ) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)
    return 1


def yogurt_cus_edit(request, id):
    if not check_authenticate(request):
        return redirect('/login_view/')
    if 'action' in request.POST:
        inputPoint = int(request.POST.get('inputPoint') or 0)
        inputCoupon = int(request.POST.get('inputCoupon')or 0)
        number = divmod(inputPoint, 30)
        if number[0] > 0:
            inputCoupon = inputCoupon + number[0]*3
            inputPoint = number[1]
        editCus = CusData.objects.get(id=id)
        editCus.name = request.POST.get('inputName')
        editCus.phone = request.POST.get('inputPhone')
        editCus.email = request.POST.get('inputEmail')
        editCus.dateOfbirth = request.POST.get('inputDateofBirth')
        editCus.point = inputPoint
        editCus.coupon = inputCoupon
        editCus.last_check_in = request.POST.get('inputLastCheckIn')
        editCus.save()
        posts = CusData.objects.all()
        context = {'posts': editCus, }
        return render(request, 'yogurt_cus_edit.html', context)
    else:
        editCus = CusData.objects.get(id=id)
        context = {'posts': editCus, }
        return render(request, 'yogurt_cus_edit.html', context)


def yogurt_checkin_mannager(request):
    if not check_authenticate(request):
        return redirect('/login_view/')
    posts = CheckInData.objects.filter(flag=0)
    context = {'posts': posts, }
    return render(request, 'yogurt_checkin_mannager.html', context)


def yogurt_setPrice(request):
    if not check_authenticate(request):
        return redirect('/login_view/')
    orderId = int(request.POST.get('orderId') or 0)
    orderPrice = int(request.POST.get('orderPrice')or 0)
    orderPhone = request.POST.get('orderPhone')
    editCheckInD = CheckInData.objects.get(id=orderId)
    editCheckInD.orderPrice = orderPrice
    editCheckInD.flag = 1
    editCheckInD.save()
    editCus = CusData.objects.filter(phone=orderPhone).first()
    editCus.point = editCus.point + editCheckInD.orderPrice
    number = divmod(editCus.point, 30)
    if number[0] > 0:
        editCus.coupon = editCus.coupon + number[0]*3
        editCus.point = number[1]
    editCus.save()

    return redirect('/yogurt_checkin_mannager/')



def yogurt_order_view(request):
    if not check_authenticate(request):
        return redirect('/login_view/')
    posts = CheckInData.objects.filter(flag=1)
    context = {'posts': posts, }
    return render(request, 'yogurt_order_view.html', context)