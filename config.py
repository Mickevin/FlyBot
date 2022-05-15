#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os
from random import randint
import logging
from opencensus.ext.azure.log_exporter import AzureEventHandler


class DefaultConfig:
    """Configuration for the bot."""


   # PORT = 3978
    CLIENT_ID = randint(1e6, 1e7)
    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId", "173dbf00-4b5a-4932-8e5f-1f9dd70dda38")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "80990656a996434895ec74d4e613ace3")
   # APP_ID = os.environ.get("MicrosoftAppId", "")
  #  APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = os.environ.get("LuisAppId", "9b0fd8a7-81ed-402c-a2a0-b534ee7d78cf")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "123007a9fbfb4ec2bd2e4cd7c88c37fa")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "languep10-authoring.cognitiveservices.azure.com/")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "InstrumentationKey=adea8d73-a6d0-4c32-a83d-8e7f6380a431"
    )


class AppInsights():
    def __init__(self, UserID, key):
        self.key = key
        self.UserID = UserID
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(AzureEventHandler(connection_string=self.key))
        self.logger.setLevel(logging.INFO)
        self.entity = []
        self.trace = []
        
    def start(self):
        self.logger.info(f'Application started correctly. User ID : {self.UserID}')
        
    def info(self):
        pass
    
    def warning(self, message):
        properties = {'custom_dimensions':{
                      'message' : message,
                      'trace' : self.trace}}
        self.logger.setLevel(logging.WARNING)
        self.logger.warning(f'Messagerie failled : {self.UserID}')
        
    
    def traces(self, message, agent):
        properties = {'messages': {agent: message}}
        self.logger.setLevel(logging.INFO)
        self.logger.info(f'Messages User ID :{self.UserID}', extra=properties)
        
        
    def entities(self, message, val_entity, entity):
        properties = {'custom_dimensions':{'messages': message,
                     'entity': entity,
                     'val_entity': val_entity}}
        self.logger.setLevel(logging.INFO)
        self.logger.info(f'Messages User ID :{self.UserID}', extra=properties)
        self.entity.append(entity)
    
    def end_conversation(self):
        properties = {'messages':'Fin de conversation',
                      'User ID' : self.UserID,
                      'trace' : self.trace,
                      'entity': self.entity
                     }
        self.logger.setLevel(logging.INFO)
        self.logger.info('Info', extra=properties)


AppInsights = AppInsights(DefaultConfig.CLIENT_ID, DefaultConfig.APPINSIGHTS_INSTRUMENTATION_KEY)
