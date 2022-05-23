from botbuilder.core import BotFrameworkAdapterSettings
from config import DefaultConfig
from flight_booking_recognizer import FlightBookingRecognizer    # The code to test
import unittest   # The test framework

import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

class Test_Config(unittest.TestCase):
    def test_config(self):
        CONFIG = DefaultConfig()
        SETTINGS = BotFrameworkAdapterSettings(CONFIG.APP_ID,CONFIG.APP_PASSWORD)
        self.assertEqual(CONFIG.PORT, 8000)
        self.assertIsNot(CONFIG.APP_ID, '')
        self.assertIsNot(CONFIG.APP_PASSWORD, '')
        self.assertIsNot(CONFIG.LUIS_APP_ID, '')
        self.assertIsNot(CONFIG.LUIS_API_KEY, '')

class Test_Luis(unittest.TestCase):
    def test_luis_connexion(self):
        CONFIG = DefaultConfig()
        SETTINGS = BotFrameworkAdapterSettings(CONFIG.APP_ID,CONFIG.APP_PASSWORD)
        RECOGNIZER = FlightBookingRecognizer(CONFIG)
        self.assertEqual(RECOGNIZER.is_configured, True)

        
class Test_Insights(unittest.TestCase):
    def test_AppInsights_connexion(self):
        CONFIG = DefaultConfig()
        try:
            logger = logging.getLogger(__name__)
            logger.addHandler(AzureLogHandler(connection_string=CONFIG.APPINSIGHTS_INSTRUMENTATION_KEY))
        except:
            self.assertIsNot(True, True)


if __name__ == '__main__':
    unittest.main()