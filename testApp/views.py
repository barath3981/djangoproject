from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.core import serializers
from django.template import response

from services import *
from rest_framework.renderers import JSONRenderer
from serializers import EventSerializer
from rest_framework import status
from rest_framework.response import Response
from userDetails import *


class JSONResponse(HttpResponse):
    """
	An HttpResponse that renders its content into JSON.
	"""

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def addition(request, num1, num2):
    result = int(num2) + int(num1)
    return HttpResponse("Hello, world. You're at the polls index. %s " % result)


# return redirect('https://www.inviter.com/')


def subTraction(request, num1, num2):
    result = int(num1) - int(num2)
    return HttpResponse("Hello: %s" % result)


def crm_login(request):
    # if key not in request.session:
    if request.COOKIES.has_key('cookie_name'):
        print request.session
        return redirect('dashboard/')
    else:
        body = render(request, 'index.html', {'view': 'static/templates/loginView.html'})
        return HttpResponse(body)

    '''if request.session.get('email') != 'barathbaisetty@inviter.com':
		body = render(request, 'index.html', {'view': 'static/templates/loginView.html'})
		return HttpResponse(body)
	else:
		print request.session
		return redirect('dashboard/')'''


def crmLoginRequest(request):
    response_data = {}
    email = request.POST.get("emailID")
    password = request.POST.get("password")
    login_result = get_login(email, password)
    print "Printed: %s" % login_result
    if login_result:
        response = HttpResponse('Bharath')
        print "Response: %s" % response

        setData(request, email)
        statusCode = 200
        response_data = {'message': 'Data received successfully', 'data': {}, 'status': 'success', 'code': 200}
        response.set_cookie("cookie_name", "cookie_value")
    else:
        statusCode = 401
        response_data = {'message': 'Invalid email or password', 'data': {'email': email, 'password': password},
                         'status': 'error', 'code': 'ERROR'}

    return HttpResponse(JSONResponse(response_data), status=statusCode)


def loadDashboard(request):
    if request.COOKIES.has_key('cookie_name'):
        print request.session.get('email')
        body = render(request, 'index.html', {'view': 'static/templates/dashboardView.html'})
        return HttpResponse(body)
    else:
        print "ERROR: %s"%request.COOKIES.get("cookie_name")
        return redirect('/')
    '''if request.session.get('email') == 'barathbaisetty@inviter.com':
		print request.session.get('email')
		body = render(request, 'index.html', {'view': 'static/templates/dashboardView.html'})
		return HttpResponse(body)
	else:
		return redirect('/')'''


def crm_logout_request(request):
    if validate_headders(request):
        if request.session.get('email') == 'barathbaisetty@inviter.com':
            del request.session['email']
            logout_response = {"status": "success", "description": "Logout successfully"}
        else:
            logout_response = {"status": "success", "description": "Logout successfully"}
        return HttpResponse(JSONResponse(logout_response), status=200)
    else:
        response = {"status": "error", "description": "Invalid request", "data": {}}
    return HttpResponse(JSONResponse(response), status=401)


def setData(request, email):
    request.session['email'] = email
    request.session['userID'] = getUserID(email)
    request.session['accessToken'] = getAccessToken(request.session['userID']).access_token
    request.session['appID'] = getAppIDAndSecret(request.session['userID']).appid
    request.session['appSecret'] = getAppIDAndSecret(request.session['userID']).app_secret


def validate_headders(request):
    print "Request meta: %s" % request.META.get('HTTP_ACCESSTOKEN')
    if request.META.get('HTTP_ACCESSTOKEN') == request.session['accessToken'] and \
                    request.META.get('HTTP_APPID') == request.session['appID'] and \
                    request.META.get('HTTP_APPSECRET') == request.session['appSecret']:
        return True
    else:
        return False


def getUserData(request):
    if request.method == 'POST':
        email = request.POST.get("emailID")
        response_data = {"userid": request.session['userID'], "email": request.session['email'],
                         "accessToken": request.session['accessToken'], "appID": request.session['appID'],
                         "appSecret": request.session['appSecret']}
        response = {"status": "success", "description": "Data retrieved successfully", "data": response_data}
        return HttpResponse(JSONResponse(response), status=200)
    else:
        response = {"status": "error", "description": "Invalid request", "data": {}}
        return HttpResponse(JSONResponse(response), status=400)


def get_all_events_request(request):
    if validate_headders(request):
        if request.method == 'POST':
            event = getAllEvents(request.session['email'])
            event_serializer = EventSerializer(event, many=True)
            event_json = event_serializer.data
            response = {"status": "success", "description": "Data retrieved successfully", "data": event_json}
            return HttpResponse(JSONResponse(response), status=200)
        else:
            response = {"status": "error", "description": "Invalid request", "data": {}}
            return HttpResponse(JSONResponse(response), status=400)
    else:
        response = {"status": "error", "description": "Invalid request", "data": {}}
        return HttpResponse(JSONResponse(response), status=401)
