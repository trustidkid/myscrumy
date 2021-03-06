from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from websocket.models import ChatMessage, Connection
import json
import boto3
from . import views

# Create your views here.
@csrf_exempt #to ignore csrf token
def test(request):
    return JsonResponse({'message': 'hello Daud'}, status=200) 

#create helper function to help pass request body binary object to dictionary
def _parse_body(body):
    #decoding to utf-8 make it easy to convert body object to json
    body_unicode = body.decode('utf-8')
    return json.loads(str(body_unicode))

@csrf_exempt
def connect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId'] 
    savecon = Connection(connection_id=connection_id)
    savecon.save()
    return JsonResponse({'message':'connect successfully'}, status=200)

@csrf_exempt
def disconnect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId'] 
    deletecon = Connection(connection_id=connection_id)
    deletecon.delete()
    return JsonResponse({'message':'disconnect successfully'}, status=200)
    
def _send_to_connection(connection_id, data):
    gatewayapi = boto3.client("apigatewaymanagementapi", endpoint_url=" https://a4et72j0xh.execute-api.us-east-1.amazonaws.com/testStage/",region_name="us-east-1", aws_access_key_id="AKIARNPOO5EVSWEQ5VFV", aws_secret_access_key="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")
    
    #Using boto3 to make post request to api gateway
    return gatewayapi.post_to_connection(ConnectionId=connection_id, data=json.dumps(data).encode('utf-8'))

#sending message

def send_message(request):
    """
    * passed the request body to a new variable called body * save the content, username and timestamp from the body dictionary to database using the ChatMessage model * get all the conection_id from the database using Connection model and assign it to a new variable called connections * prepare body as a list of messages, then assign it to a data variable(data = {‘messages’:[body]}) * loop over connections and use _send_to_connection function to send data to all connected client """
    body = _parse_body(request.body)
    username = body['username']
    timestamps = body['timestamp']
    message = body['message']
    save_to_db = ChatMessage(username=username, message = message, timestamp=timestamps)
    save_to_db.save()        
    connections = Connection.objects.all()
    data = {'messages':[body]}
    for con in connections:
        _send_to_connection(con.id, data)
    

def getRecentMessages(request):
    recent_msg = ChatMessage.objects.all()
    return JsonResponse({'messages': recent_msg})
    
    
    