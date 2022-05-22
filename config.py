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


    PORT = 3978
    CLIENT_ID = randint(1e6, 1e7)
    #PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId", "173dbf00-4b5a-4932-8e5f-1f9dd70dda38")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "80990656a996434895ec74d4e613ace3")
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = os.environ.get("LuisAppId", "fd24c90b-e679-4a4a-91d7-e0e3e35c8b13")
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
        self.entity = None
        self.trace = {}
        self.n_message = 0
        self.err = 0
    
    def n_messages(self):
        self.n_message+=1
        if self.n_message >10 and self.n_message <15:
            self.warning(f'Warning, to many message User{self.UserID}')

        elif self.n_message >15:
            self.critical(f'Warning, to many message User{self.UserID}')

    def message_error(self):
        self.err+=1
        if self.err >3:
            self.error(f'To many message eroro UserID {DefaultConfig.CLIENT_ID}')

    # Fonction permettant d'envoyer des allerte de niveau info
    def info(self, message, entities=False):
        if entities:
            self.trace['entities'] = str(list(self.entity.values()))
        properties = {'custom_dimensions': self.trace}
        self.logger.setLevel(logging.INFO)
        self.logger.info(message, extra=properties)
        
    # Fonction permettant d'envoyer des allerte de niveau warning  
    def warning(self, message):
        properties = {'custom_dimensions': self.trace}
        
        self.logger.setLevel(logging.WARNING)
        self.logger.warning(message, extra=properties)
        
    # Fonction permettant d'envoyer des allerte de niveau error  
    def error(self, message):
        properties = {'custom_dimensions': self.trace}
        
        self.logger.setLevel(logging.ERROR)
        self.logger.error(message, extra=properties)
        
    # Fonction permettant d'envoyer des allerte de niveau critical  
    def critical(self, message):
        properties = {'custom_dimensions': self.trace}
        
        self.logger.setLevel(logging.CRITICAL)
        self.logger.critical(message, extra=properties)


AppInsights = AppInsights(DefaultConfig.CLIENT_ID, DefaultConfig.APPINSIGHTS_INSTRUMENTATION_KEY)
