import json
from django.shortcuts import render
from requests.auth import HTTPBasicAuth
from django.contrib import messages
from .forms import MemberForm
import requests
from django.http import HttpResponse

def member_view(request):

    if request.method == "POST":
        print("post request run !")
        form = MemberForm(request.POST)
        if form.is_valid():
            token = request.POST.get('g-recaptcha-response')
            data = {
                    'secret': '6LfMEbYZAAAAACXFyECLZnuXNg9sy7cgPDOFE3d-',
                    'response': token
                }
            print(token)
             # verify response with Google
            response = requests.post(
                    'https://www.google.com/recaptcha/api/siteverify',
                    data=data
            )

            result =  json.loads(response.text)
            print(result)
            if result['success']:
                print("valid form")
                print("Error : ",form.errors)


                return render(request, "member.html",
                                  {"form": form, "recaptcha_key": '6LfMEbYZAAAAABpAqC-jCRT1RDvHTSgR3mJ6jHNs'})
                #return HttpResponse("True !")
            else:
                print("unsuccesfully")
                error = "Document deleted"
                return render(request, "member.html",
                              {"form": form, "recaptcha_key": '6LfMEbYZAAAAABpAqC-jCRT1RDvHTSgR3mJ6jHNs', "error": error})
        else:
            print("Error : ",form.errors)
            print("invalid Captcha !")
        """
        if form.is_valid():
            token = request.POST.get('g-recaptcha-response')
            if token:
                data = {
                    'secret': '6Lff4LUZAAAAALejpyi78vCHLHOw0A-B-oZs2z72',
                    'response': token
                }
                # verify response with Google
                response = requests.post(
                    'https://www.google.com/recaptcha/api/siteverify',
                    data=data
                )
                result = response.json()
                # check results
                if result['success'] == True and result['score'] >= 0.5:
                    r = requests.post('http://localhost:8000/api/memberview', data= {
                        "name" : form.cleaned_data["name"],
                        "date" : form.cleaned_data["date"],
                        "age"  : int(form.cleaned_data["age"]),
                        "mobile_no" : form.cleaned_data["mobile_no"],

                    })

                    if r.status_code == 201:
                        response = r.json()
                        return render(request, "member.html", {"form": form, "response" : response, "recaptcha_key" : '6Lff4LUZAAAAALejpyi78vCHLHOw0A-B-oZs2z72'}, headers = {"username":"prashant", "password" : "123pra123"})
                    else:
                        print(r)
                        print(r.text)
                        return render(request, "member.html", {"form": form, "recaptcha_key" : '6Lff4LUZAAAAALejpyi78vCHLHOw0A-B-oZs2z72'})
                else:
                    print("Invalid Captcha !")
                    messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                    return render(request, "member.html", {"form" : form, "recaptcha_key" : '6Lff4LUZAAAAALejpyi78vCHLHOw0A-B-oZs2z72'})
            else:
                print("Token Not Found !")
                messages.error(request, 'You are not Enter Captcha.')
                return render(request, "member.html",
                                {"form": form, "recaptcha_key": '6Lff4LUZAAAAALejpyi78vCHLHOw0A-B-oZs2z72'})
            """
    form = MemberForm()
    return render(request, "member.html", {"form" : form, "recaptcha_key" : '6LfMEbYZAAAAABpAqC-jCRT1RDvHTSgR3mJ6jHNs'})

def member_view1(request):

    if request.method == "POST":

        print("post request run !")
        form = MemberForm(request.POST)
        if form.is_valid():
            token = request.POST.get('h-captcha-response')
            data = {
                    'secret': '0x1BB00ddC007ceFB915DD046bdA8C0065e067DA55',
                    'response': token
                }
             # verify response with Google
            response = requests.post(
                    'https://hcaptcha.com/siteverify',
                    data=data
            )

            result =  json.loads(response.text)
            print(result)
            if result['success']:
                form.is_valid()
                print("valid form")
                print("Error : ",form.errors)
                form = MemberForm()
                return render(request, "member1.html",
                                  {"form": form, "recaptcha_key": '9d50150e-028c-4759-acb1-125f2ccbe862'})
                #return HttpResponse("True !")
            else:
                print("unsuccesfully")
                error = "Document deleted"
                return render(request, "member1.html",
                              {"form": form, "recaptcha_key": '9d50150e-028c-4759-acb1-125f2ccbe862', "error": error})
        else:
            print("Form Not Valid !")
        """
        if form.is_valid():
            token = request.POST.get('g-recaptcha-response')
            if token:
                data = {
                    'secret': '6Lff4LUZAAAAALejpyi78vCHLHOw0A-B-oZs2z72',
                    'response': token
                }
                # verify response with Google
                response = requests.post(
                    'https://www.google.com/recaptcha/api/siteverify',
                    data=data
                )
                result = response.json()
                # check results
                if result['success'] == True and result['score'] >= 0.5:
                    r = requests.post('http://localhost:8000/api/memberview', data= {
                        "name" : form.cleaned_data["name"],
                        "date" : form.cleaned_data["date"],
                        "age"  : int(form.cleaned_data["age"]),
                        "mobile_no" : form.cleaned_data["mobile_no"],

                    })

                    if r.status_code == 201:
                        response = r.json()
                        return render(request, "member.html", {"form": form, "response" : response, "recaptcha_key" : '6Lff4LUZAAAAALejpyi78vCHLHOw0A-B-oZs2z72'}, headers = {"username":"prashant", "password" : "123pra123"})
                    else:
                        print(r)
                        print(r.text)
                        return render(request, "member.html", {"form": form, "recaptcha_key" : '6Lff4LUZAAAAALejpyi78vCHLHOw0A-B-oZs2z72'})
                else:
                    print("Invalid Captcha !")
                    messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                    return render(request, "member.html", {"form" : form, "recaptcha_key" : '6Lff4LUZAAAAALejpyi78vCHLHOw0A-B-oZs2z72'})
            else:
                print("Token Not Found !")
                messages.error(request, 'You are not Enter Captcha.')
                return render(request, "member.html",
                                {"form": form, "recaptcha_key": '6Lff4LUZAAAAALejpyi78vCHLHOw0A-B-oZs2z72'})
            """
    form = MemberForm()
    return render(request, "member1.html", {"form" : form, "recaptcha_key" : '9d50150e-028c-4759-acb1-125f2ccbe862'})
