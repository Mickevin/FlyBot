from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount

from azure.cognitiveservices.language.luis.authoring import LUISAuthoringClient
from azure.cognitiveservices.language.luis.authoring.models import ApplicationCreateObject
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials



class My_bot:
    def __init__(self, api_id = '9b0fd8a7-81ed-402c-a2a0-b534ee7d78cf'):
        self.code = 4
        
        def getEndpointKeys_kb(client):
            keys = client.endpoint_keys.get_keys()
            return keys.primary_endpoint_key
        
        self.api_id = api_id
        self.authoringKey = '123007a9fbfb4ec2bd2e4cd7c88c37fa'
        self.authoringEndpoint = 'https://languep10-authoring.cognitiveservices.azure.com/'
        self.predictionKey = '75800c252f4246e9b665a9015f046091'
        self.predictionEndpoint = 'https://langue-p10.cognitiveservices.azure.com/'
        
        
        self.subscription_key = 'cbb4bcaa0a334e02a1261cf18aa1ad18'
        self.authoring_endpoint = 'https://qna0.cognitiveservices.azure.com/'
        self.runtime_endpoint = 'https://qna0.azurewebsites.net'
        
        
        # We use a UUID to avoid name collisions.
        self.versionId = "0.1"
        self.intentName = "FlyMe.Booking"
        
        self.client = LUISAuthoringClient(self.authoringEndpoint,
                                          CognitiveServicesCredentials(self.authoringKey))
        
        self.runtimeCredentials = CognitiveServicesCredentials(self.predictionKey)
        self.clientRuntime = LUISRuntimeClient(endpoint=self.predictionEndpoint,
                                               credentials=self.runtimeCredentials)
     
        self.data = {
            'or_city': False,
              'dst_city': False,
              'str_date': False,
              'end_date': False,
              'budget': False
             }
        
        self.trad = {
            'or_city': "origin's city",
              'dst_city': "destination's city",
              'str_date': "day's start",
              'end_date': "end's date",
              'budget': "your budget"
             }


    def prediction(self, text):

        # Production == slot name
        self.predictionRequest = { "query" : text}

        predictionResponse = self.clientRuntime.prediction.get_slot_prediction(self.api_id,
                                                                                    "Production",
                                                                                    self.predictionRequest,
                                                                                    show_all_intents=False)
        pred = predictionResponse.prediction
        
        return pred.intents.keys(), {key:value[0] for key,value in pred.entities.items()}
    
    
    