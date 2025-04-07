# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionCheckAge(Action):

    def name(self) -> Text:
        return "action_check_age"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        age = tracker.get_slot("age")

        if age is None:
            dispatcher.utter_message(text="I couldn't understand your age. Could you please tell me again?")
            return []

        if age >= 18:
            dispatcher.utter_message(response="utter_age_allowed")
        else:
            dispatcher.utter_message(response="utter_age_restricted")

        return []