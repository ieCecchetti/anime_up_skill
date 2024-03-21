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
import utils

# from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def retrieve_day(plus_days=0):
    # Get the current date and time
    current_datetime = datetime.now() + timedelta(days=plus_days)
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


class SelectAnimeIntentHandler(AbstractRequestHandler):
    """Handler for SelectAnimeIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SelectAnimeIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # get the handler_input["anime_name"] param
        anime_name = handler_input.request_envelope.request.intent.slots["anime_name"].value
        # Initialize session attributes
        session_attr = handler_input.attributes_manager.session_attributes
        # store the anime name on the state for future operations
        session_attr['selected_anime'] = anime_name
        speak_output = f"Ok, parliamo di {anime_name}"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(constants.FALLBACK_ASK)
                .response
        )


class WhichAnimeSelectedIntentHandler(AbstractRequestHandler):
    """Handler for SelectAnimeIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WhichAnimeSelectedIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # Initialize session attributes
        session_attr = handler_input.attributes_manager.session_attributes
        # store the anime name on the state for future operations
        anime_name = session_attr.get('selected_anime', None)
        if anime_name:
            # get the anime info
            anime_list = [anime["name"] for anime in constants.AIRING_ANIME]
            selected_anime = utils.get_closer_name(anime_name, anime_list)
            speak_output = f"Stiamo parlando di: {selected_anime}"
        else:
            speak_output = f"Ah, non lo so! Non me lo hai ancora specificato."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(constants.FALLBACK_ASK)
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
        today_list = [anime['name'] for anime in constants.AIRING_ANIME if anime['airing_day'] == current_day]
        today_list_str = ', '.join(today_list) or 'stograncasso'
        speak_output = f"Oggi, ci sono in programma le uscite di: {today_list_str}"

        # speak_output = f"Oggi, {current_day}, ci sono in programma le uscite di: stograncasso"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(constants.FALLBACK_ASK)
                .response
        )


class WhatsAnimeInIntentHandler(AbstractRequestHandler):
    """Handler for TodayAnimeIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WhatsAnimeInIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # Initialize session attributes
        session_attr = handler_input.attributes_manager.session_attributes
        # get the handler_input["dates_word"] param: ex `domani`
        date_word = handler_input.request_envelope.request.intent.slots["dates_word"].value
        days_to_add = constants.DAYS_TO_ADD[date_word]
        if not anime_name:
            speak_output = "Non ho capito di che giorno stai parlando!"
        else:
            
            current_day = retrieve_day(days_to_add)
            today_list = [anime['name'] for anime in constants.AIRING_ANIME if anime['airing_day'] == current_day]
            today_list_str = ', '.join(today_list) or 'stograncasso'
            speak_output = f"Oggi, ci sono in programma le uscite di: {today_list_str}"

        # speak_output = f"Oggi, {current_day}, ci sono in programma le uscite di: stograncasso"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(constants.FALLBACK_ASK)
                .response
        )

class WhatsOutInDayOfWeekIntentHandler(AbstractRequestHandler):
    """Handler for TodayAnimeIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WhatsOutInDayOfWeekIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # Initialize session attributes
        session_attr = handler_input.attributes_manager.session_attributes
        # get the handler_input["anime_name"] param
        unparsed_day = handler_input.request_envelope.request.intent.slots["day_of_week"].value
        selected_day = None
        for key, value in constants.DAY_OF_THE_WEEK.items():
            if value == unparsed_day.title():
                selected_day = key
        if selected_day:
            today_list = [anime['name'] for anime in constants.AIRING_ANIME if anime['airing_day'] == selected_day]
            today_list_str = ', '.join(today_list) or 'stograncasso'
            speak_output = f"{unparsed_day.title()}, ci sono in programma le uscite di: {today_list_str}"
        else:
            speak_output = f"Scusa bro, Non ho capito che giorno intendi!"

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
        airing_list = [anime['name'] for anime in constants.AIRING_ANIME]

        speak_output = f"Al momento gli anime di cui ho informazioni sono: {', '.join(airing_list)}"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(constants.FALLBACK_ASK)
                .response
        )


class InfoOnAnimeIntentHandler(AbstractRequestHandler):
    """Handler for AllAnimeIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("InfoOnAnimeIntent")(handler_input)
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # Initialize session attributes
        session_attr = handler_input.attributes_manager.session_attributes
        # get the handler_input["anime_name"] param
        anime_name = handler_input.request_envelope.request.intent.slots["anime_name"].value or session_attr.get('selected_anime', None)
        if not anime_name:
            speak_output = "Non ho capito di che anime stiamo parlando!"
        else:
            session_attr['state'] = 'info_anime'
            # store the anime name on the state for future operations
            session_attr['selected_anime'] = anime_name
            # get the anime info
            anime_list = [anime["name"] for anime in constants.AIRING_ANIME]
            selected_anime = utils.get_closer_name(anime_name, anime_list)
            anime_info = utils.get_info_from_anime(selected_anime)
            day_of_week = constants.DAY_OF_THE_WEEK[anime_info['airing_day']]
            if anime_info:
                speak_output = (
                    f"{anime_name}, o con il suo nome completo {anime_info['name']}, e' un anime {anime_info['genere']}. "
                    f"Ha {anime_info['season']} stagioni e attualmente siamo al {anime_info['episode']} episodio. "
                    f"Esce di {day_of_week}. Attualmente ha un voto di {anime_info['rating']} con {anime_info['follower']} followers. "
                    f"Il mio personale commento e': {utils.get_anime_feed(anime_info['rating'], anime_info['follower'])}"
                )
            else:
                speak_output = f"Scusa, non ho trovato nessuna informazione su {anime_name}."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(constants.FALLBACK_ASK)
                .response
        )


class TramaAnimeIntentHandler(AbstractRequestHandler):
    """Handler for AllAnimeIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TramaAnimeIntent")(handler_input)
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # get the handler_input["anime_name"] param
        # Initialize session attributes
        session_attr = handler_input.attributes_manager.session_attributes
        # get the handler_input["anime_name"] param
        anime_name = handler_input.request_envelope.request.intent.slots["anime_name"].value or session_attr.get('selected_anime', None)
        if not anime_name:
            speak_output = "Non ho capito di che anime stiamo parlando!"
        else:
            # store the anime name on the state for future operations
            session_attr['selected_anime'] = anime_name
            anime_list = [anime["name"] for anime in constants.AIRING_ANIME]
            selected_anime = utils.get_closer_name(anime_name, anime_list)
            anime_info = utils.get_info_from_anime(selected_anime)
            if anime_info:
                if anime_info['descr']:
                    speak_output = f"Certo, la trama è questa: {anime_info['descr']}"
                else:
                    speak_output = f"Scusa ma non ho informazioni sulla trama di questo anime. Mando una segnalazione, magari tra qualche giorno mi aggiornano."
            else:
                speak_output = f"Scusa ma non ho trovato nessuna informazione associata a: {anime_name}. Prova a scandire meglio il nome."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(constants.FALLBACK_ASK)
                .response
        )


class AskFeedbackIntentHandler(AbstractRequestHandler):
    """Handler for AllAnimeIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AskFeedbackIntent")(handler_input)
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # Initialize session attributes
        session_attr = handler_input.attributes_manager.session_attributes
        # get the handler_input["anime_name"] param
        anime_name = handler_input.request_envelope.request.intent.slots["anime_name"].value or session_attr.get('selected_anime', None)
        if not anime_name:
            speak_output = "Non ho capito di che anime stiamo parlando!"
        else:
            # store the anime name on the state for future operations
            session_attr['selected_anime'] = anime_name
            anime_list = [anime["name"] for anime in constants.AIRING_ANIME]
            selected_anime = utils.get_closer_name(anime_name, anime_list)
            anime_info = utils.get_info_from_anime(selected_anime)
            if anime_info:
                speak_output = f"Il mio personale commento e': {utils.get_anime_feed(anime_info['rating'], anime_info['follower'])}"
                
            else:
                speak_output = f"Scusa, non ho trovato nessuna informazione su {anime_name}."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(constants.FALLBACK_ASK)
                .response
        )


class LastEpisodeIntentHandler(AbstractRequestHandler):
    """Handler for AllAnimeIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LastEpisodeIntent")(handler_input)
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # get the handler_input["anime_name"] param
        # Initialize session attributes
        session_attr = handler_input.attributes_manager.session_attributes
        # get the handler_input["anime_name"] param
        anime_name = handler_input.request_envelope.request.intent.slots["anime_name"].value or session_attr.get('selected_anime', None)
        if not anime_name:
            speak_output = "Non ho capito di che anime stiamo parlando!"
        else:
            # store the anime name on the state for future operations
            session_attr['selected_anime'] = anime_name
            anime_list = [anime["name"] for anime in constants.AIRING_ANIME]
            selected_anime = utils.get_closer_name(anime_name, anime_list)
            anime_info = utils.get_info_from_anime(selected_anime)
            if anime_info:
                speak_output = f"L'ultimo episodio di {anime_name} è {anime_info['episode']}"
            else:
                speak_output = f"Scusa ma non ho trovato nessuna informazione associata a: {anime_name}. Prova a scandire meglio il nome."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(constants.FALLBACK_ASK)
                .response
        )


class WhenOutAnimeIntentHandler(AbstractRequestHandler):
    """Handler for AllAnimeIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WhenOutAnimeIntent")(handler_input)
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # get the handler_input["anime_name"] param
        # Initialize session attributes
        session_attr = handler_input.attributes_manager.session_attributes
        # get the handler_input["anime_name"] param
        anime_name = handler_input.request_envelope.request.intent.slots["anime_name"].value or session_attr.get('selected_anime', None)
        if not anime_name:
            speak_output = "Non ho capito di che anime stiamo parlando!"
        else:
            # store the anime name on the state for future operations
            session_attr['selected_anime'] = anime_name
            anime_list = [anime["name"] for anime in constants.AIRING_ANIME]
            selected_anime = utils.get_closer_name(anime_name, anime_list)
            anime_info = utils.get_info_from_anime(selected_anime)
            if anime_info:
                speak_output = f"L'ultimo episodio di {anime_name} è {anime_info['episode']}"
            else:
                speak_output = f"Scusa ma non ho trovato nessuna informazione associata a: {anime_name}. Prova a scandire meglio il nome."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(constants.FALLBACK_ASK)
                .response
        )


class ConfirmIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("ConfirmIntent")(handler_input)
        
    def handle(self, handler_input):
        session_attr = handler_input.attributes_manager.session_attributes
        state = session_attr.get('state')
        # Get the slot value from the user's response
        answer = ask_utils.get_slot_value(handler_input, "answer")
        if state == 'info_anime':
            # Handle confirmation in shopping context
            session_attr['state'] = None
            return handler_input.response_builder.speak(f"AAAAAAAH hai risposto: {answer} quando parlavamo di {state}").response
        else:
            return handler_input.response_builder.speak("I'm not sure what you're confirming.").response


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

        speak_output = f"Sorry, I had trouble doing what you asked. Please try again. Error: {repr(exception)}"

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
sb.add_request_handler(SelectAnimeIntentHandler())
sb.add_request_handler(WhichAnimeSelectedIntentHandler())
sb.add_request_handler(TodayAnimeIntentHandler())
sb.add_request_handler(WhatsAnimeInIntentHandler())
sb.add_request_handler(WhatsOutInDayOfWeekIntentHandler())
sb.add_request_handler(AllAnimeIntentHandler())
sb.add_request_handler(InfoOnAnimeIntentHandler())
sb.add_request_handler(TramaAnimeIntentHandler())
sb.add_request_handler(LastEpisodeIntentHandler())
sb.add_request_handler(WhenOutAnimeIntentHandler())
sb.add_request_handler(AskFeedbackIntentHandler())
sb.add_request_handler(ConfirmIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()