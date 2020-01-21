from .models import *
import re
from smtplib import SMTP
import random


def list_college():
    colleges = college.objects.all()
    college_list = []
    count = 1
    for col in colleges:
        college_list.append(tuple(list([str(count), str(col.college_name)])))
        count += 1
    return tuple(college_list)


def generate_password():
    get = 'abcdefghijklmnopqrstuvwxyz1234567890!@#&'
    password = ''
    for i in range(10):
        password += get[random.randint(0, len(get) - 1)]
    return str(password)


def sendmail(email, otp):
    connect = SMTP('smtp.gmail.com', 587)
    connect.ehlo()
    connect.starttls()
    connect.login(str('rrohitanand3336@gmail.com'), str('qbkpstvmwfgswlec'))
    content = 'Subject: ' + str('OTP for login portal') + '\n\n' + str('Your six digit OTP is ') + str(
        otp) + '\n\n' + 'Regards\nAlumni\'s Call'
    connect.sendmail(str('rrohitanand3336@gmail.com'), str(email), content)
    connect.quit()


def generate_otp(email):
    otp = random.randrange(111111, 999999)
    sendmail(email, otp)
    return otp


def recover_mail(email, password):
    connect = SMTP('smtp.gmail.com', 587)
    connect.ehlo()
    connect.starttls()
    connect.login(str('rrohitanand3336@gmail.com'), str('qbkpstvmwfgswlec'))
    content = 'Subject: ' + str('Change Password') + '\n\n' + str('Your Temporary password is ') + str(
        password) + '\n\n' + str('Please login and change your temporary password') + '\n\n' + 'Regards\nAlumni\'s Call'
    connect.sendmail(str('rrohitanand3336@gmail.com'), str(email), content)
    connect.quit()


def object_collector(request):
    try:
        profile = alumni.objects.get(user=request.user)
    except alumni.DoesNotExist:
        try:
            profile = student.objects.get(user=request.user)
        except student.DoesNotExist:
            request.session.flush()
    return profile


def post_collector(request):

    return blog.objects.filter(author__college_id=object_collector(request).college_id).order_by('-views', '-like')[:5]


def internships_collector(request):

    return internships.objects.filter(author__college_id=object_collector(request).college_id).order_by('-added')[:5]


def event_collector(request):
    return Event.objects.filter(college_id__exact=object_collector(request).college_id).order_by('-event_on')[:5]
