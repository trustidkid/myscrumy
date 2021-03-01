from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from websocket.models import ChatMessage, Connection
import json

# Create your views here.
@csrf_exempt #to ignore csrf token
def test(request):
    return JsonResponse({"message": "hello Daud"}, status=200) 

#create helper function to help pass request body binary object to dictionary
def _parse_body(body):
    #decoding to utf-8 make it easy to convert body object to json
    body_unicode = body.decode('utf-8')
    return json.loads(body_unicode)

@csrf_exempt
def connect(request):
    body = _parse_body(request.body)
    connection_id = body["connectionId"] 
    savecon = Connection(connection_id=connection_id)
    savecon.save()
    JsonResponse({"message":"connect successfully"}, status=200)

@csrf_exempt
def disconnect(request):
    body = _parse_body(request.body)
    connection_id = body["connectionId"] 
    savecon = Connection(connection_id=connection_id)
    savecon.delete()
    JsonResponse({"message":"disconnect successfully"}, status=200)
    
    