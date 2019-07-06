import urllib
import urllib2
import json
import logging
import threading
import uuid
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
""" --- Lex part handler --- """


def dispatch(intent_request):
        
    raise Exception('Intent with name ' + intent_name + ' not supported')


#Main handler

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    try:
        

        if event['request']['type'] == "LaunchRequest":
            return on_launch(event['request'], event['session'])
        elif event['request']['type'] == "IntentRequest":
            return on_intent(event['request'], event['session'])
        elif event['request']['type'] == "SessionEndedRequest":
            return on_session_ended(event['request'], event['session'])
    except:
        
        #logger.debug('event.bot.name={}'.format(event['bot']['name']))
        return dispatch(event)
        

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers

#***************************************************
#first change is here(add the intent name)
#****************************************************

    if intent_name == "kitchenenglishon":
        return run_kitchenenglishon(intent, session)
    elif intent_name == "kitchenenglishoff":
        return run_kitchenenglishoff(intent, session)
    elif intent_name == "kitchenmarathion":
        return run_kitchenmarathion(intent, session)
    elif intent_name == "kitchenmarathioff":
        return run_kitchenmarathioff(intent, session)
    elif intent_name == "kitchenhindion":
        return run_kitchenhindion(intent, session)
    elif intent_name == "kitchenhindioff":
        return run_kitchenhindioff(intent, session)
    elif intent_name == "hallenglishon":
        return run_hallenglishon(intent, session)
    elif intent_name == "hallenglishoff":
        return run_hallenglishoff(intent, session)
    elif intent_name == "hallmarathion":
        return run_hallmarathion(intent, session)
    elif intent_name == "hallmarathioff":
        return run_hallmarathioff(intent, session)
    elif intent_name == "hallhindion":
        return run_hallhindion(intent, session)
    elif intent_name == "hallhindioff":
        return run_hallhindioff(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

#***************************************************
#first change is here(add the intent name)
#****************************************************

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "it was nice talking to you . thanks ."
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# Run the Speed Test

#****************************************************
#Second change is here(add the intent function)
#****************************************************



def run_kitchenenglishon(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    reply="i have switched on the light in kitchen."
    speech_output = reply
    url = 'https://api.particle.io/v1/devices/your-device-id/led?access_token=your-access-token'
    data = urllib.urlencode({'args':'kitchen_on'})
    req = urllib2.Request(url, data)
    req.add_header('content-type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    print resp
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
        
def run_kitchenenglishoff(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    reply="i have switched off the light in kitchen."
    speech_output = reply
    url = 'https://api.particle.io/v1/devices/your-device-id/led?access_token=your-access-token'
    data = urllib.urlencode({'args':'kitchen_off'})
    req = urllib2.Request(url, data)
    req.add_header('content-type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    print resp
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
        
def run_kitchenmarathion(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    reply="mi kitchen madhla light suru kela ahe ."
    speech_output = reply
    url = 'https://api.particle.io/v1/devices/your-device-id/led?access_token=your-access-token'
    data = urllib.urlencode({'args':'kitchen_on'})
    req = urllib2.Request(url, data)
    req.add_header('content-type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    print resp
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
        
def run_kitchenmarathioff(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    reply="mi kitchen madhla light banda kela ahe ."
    speech_output = reply
    url = 'https://api.particle.io/v1/devices/your-device-id/led?access_token=your-access-token'
    data = urllib.urlencode({'args':'kitchen_off'})
    req = urllib2.Request(url, data)
    req.add_header('content-type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    print resp
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))





def run_kitchenhindion(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    reply="maine kitchen ka light chalu kar diya hain ."
    speech_output = reply
    url = 'https://api.particle.io/v1/devices/your-device-id/led?access_token=your-access-token'
    data = urllib.urlencode({'args':'kitchen_on'})
    req = urllib2.Request(url, data)
    req.add_header('content-type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    print resp
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
        
def run_kitchenhindioff(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    reply="maine kitchen ka light band kar diya hain ."
    speech_output = reply
    url = 'https://api.particle.io/v1/devices/your-device-id/led?access_token=your-access-token'
    data = urllib.urlencode({'args':'kitchen_off'})
    req = urllib2.Request(url, data)
    req.add_header('content-type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    print resp
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))        
        

       
def run_hallenglishon(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    reply="i have switched on the light in hall."
    speech_output = reply
    url = 'https://api.particle.io/v1/devices/your-device-id/led?access_token=your-access-token'
    data = urllib.urlencode({'args':'hall_on'})
    req = urllib2.Request(url, data)
    req.add_header('content-type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    print resp
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
        
def run_hallenglishoff(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    reply="i have switched off the light in hall."
    speech_output = reply
    url = 'https://api.particle.io/v1/devices/your-device-id/led?access_token=your-access-token'
    data = urllib.urlencode({'args':'hall_off'})
    req = urllib2.Request(url, data)
    req.add_header('content-type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    print resp
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
        
def run_hallmarathion(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    reply="mi hall madhla light suru kela ahe ."
    speech_output = reply
    url = 'https://api.particle.io/v1/devices/your-device-id/led?access_token=your-access-token'
    data = urllib.urlencode({'args':'hall_on'})
    req = urllib2.Request(url, data)
    req.add_header('content-type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    print resp
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
        
def run_hallmarathioff(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    reply="mi hall madhla light banda kela ahe ."
    speech_output = reply
    url = 'https://api.particle.io/v1/devices/your-device-id/led?access_token=your-access-token'
    data = urllib.urlencode({'args':'hall_off'})
    req = urllib2.Request(url, data)
    req.add_header('content-type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    print resp
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))





def run_hallhindion(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    reply="maine hall ka light chalu kar diya hain ."
    speech_output = reply
    url = 'https://api.particle.io/v1/devices/your-device-id/led?access_token=your-access-token'
    data = urllib.urlencode({'args':'hall_on'})
    req = urllib2.Request(url, data)
    req.add_header('content-type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    print resp
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
        
def run_hallhindioff(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    reply="maine hall ka light band kar diya hain ."
    speech_output = reply
    url = 'https://api.particle.io/v1/devices/your-device-id/led?access_token=your-access-token'
    data = urllib.urlencode({'args':'hall_off'})
    req = urllib2.Request(url, data)
    req.add_header('content-type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    print resp
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))         


        
#****************************************************
#Second change is here(add the intent function)
#****************************************************

# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "this is your smart home skill. you can ask me to control the lights of your home."
    #code to update page
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.

        
    reprompt_text = "sorry , i didn't understood that ."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
    
    
    
# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
 return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

