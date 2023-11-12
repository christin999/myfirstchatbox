from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

action_server_url = "http://localhost:5055/webhook"


class ActionSearchYouTube(Action):
    def name(self) -> Text:
        return "action_search_youtube"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("ActionSearchYouTube")
        print(f"Extracted text: {tracker.latest_message['entities'][0]}")
        genre = tracker.latest_message['entities'][0]['value']

        print(f"Extracted genre text: {genre}")
        # You can replace this with your actual logic to search YouTube for songs of the given genre
        search_query = f"{genre} songs"
        youtube_search_url = f"https://www.youtube.com/results?search_query={search_query}"

        dispatcher.utter_message(text=f"Sure! I've searched YouTube for {genre} songs. [YouTube Search]({youtube_search_url})")

        return []


class ActionGetWeather(Action):
    def name(self) -> Text:
        return "action_search_weather"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("ActionGetWeather")
        print(f"Extracted text: {tracker.latest_message['entities'][0]}")
        location = tracker.latest_message['entities'][0]['value']

        print(f"Extracted text: {tracker.latest_message['entities'][0]}")
        print(f"Extracted genre text: {location}")
        # You can replace this with your actual logic to search YouTube for songs of the given genre
        search_query = location.replace(" ", "+")
        weather_search_url = f"https://www.google.com/search?q=weather+in+{search_query}"

        dispatcher.utter_message(text=f"Sure! I've searched Google for {location} weather. [Google Search]({weather_search_url})")

        return []