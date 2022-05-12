#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "173dbf00-4b5a-4932-8e5f-1f9dd70dda38")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "80990656a996434895ec74d4e613ace3")
    #APP_ID = os.environ.get("MicrosoftAppId", "")
    #APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = os.environ.get("LuisAppId", "9b0fd8a7-81ed-402c-a2a0-b534ee7d78cf")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "123007a9fbfb4ec2bd2e4cd7c88c37fa")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "languep10-authoring.cognitiveservices.azure.com/")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "InstrumentationKey=adea8d73-a6d0-4c32-a83d-8e7f6380a431"
    )
