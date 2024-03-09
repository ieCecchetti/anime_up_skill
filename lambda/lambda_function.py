# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

from datetime import datetime
import constants
from fuzzywuzzy import process

# from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

my_anime_list = []

def retrieve_day():
    # Get the current date and time
    current_datetime = datetime.now()
    # Get the day of the week as an integer (Monday is 0 and Sunday is 6)
    day_of_week = current_datetime.weekday()
    # Get the day of the week as a string (e.g., 'Mon', 'Tue', etc.)
    day_of_week_str = current_datetime.strftime('%a')
    return day_of_week_str

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Ciao, mio piccolo nerd preferito, che vuoi sapere?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
    
class TodayAnimeIntentHandler(AbstractRequestHandler):
    """Handler for TodayAnimeIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TodayAnimeIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        current_day = retrieve_day()
        today_list = [anime['name'] for anime in constants.HIRING_ANIME if anime['hiring_day'] == current_day]
        today_list_str = ', '.join(today_list) or 'stograncasso'
        speak_output = f"Oggi, ci sono in programma le uscite di: {today_list_str}"

        # speak_output = f"Oggi, {current_day}, ci sono in programma le uscite di: stograncasso"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(constants.FALLBACK_ASK)
                .response
        )


class AllAnimeIntentHandler(AbstractRequestHandler):
    """Handler for AllAnimeIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AllAnimeIntent")(handler_input)
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        hiring_list = [anime['name'] for anime in constants.HIRING_ANIME]

        speak_output = f"Al momento i disponibili sono: {', '.join(hiring_list)}"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(constants.FALLBACK_ASK)
                .response
        )


class AddAnimeIntentHandler(AbstractRequestHandler):
    """Handler for AddAnimeIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AddAnimeIntent")(handler_input)
        
    def find_best_match(target_name, list_of_names):
        best_match, score = process.extractOne(target_name, list_of_names)
        return best_match
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        try:
            # Extract the name associated with the slot
            anime_name = handler_input.request_envelope.request.intent.slots["anime_name"].value
            # the anime is in slot so its for sure an accepted one (but the slots can be different from the anime list constant)
            hiring_list = [anime['name'] for anime in constants.HIRING_ANIME]
            best_match = find_best_match(anime_name, hiring_list)
            
            anime_id = None
            for anime in constants.HIRING_ANIME:
                if anime['name'] == best_match:
                    anime_id = anime['id']
            
            if not anime_id:
                speak_output = f"{best_match} non corrisponde a nessun anime della lista."
            else:
                if anime_id in my_anime_list: 
                    speak_output = f"{best_match} fa gia parte della tua lista!"
                else:
                    my_anime_list.append(anime_id)
                    speak_output = f"Ok ho aggiunto {anime_name} alla tua lista."
            
        except KeyError:
            # Handle the case when "anime_name" slot is not present in the request
            speech_text = "Scusa non ho capito il nome dell'anime. Puoi ripeterlo?"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(constants.FALLBACK_ASK)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(TodayAnimeIntentHandler())
sb.add_request_handler(AllAnimeIntentHandler())
sb.add_request_handler(AddAnimeIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()