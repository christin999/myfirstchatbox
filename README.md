## Overview
This repository contains the code and configuration files for a Rasa-based chatbot. The chatbot is designed to handle greetings, provide weather information, play music, find restaurants, and engage in chitchat.

## Assignment 1
### I worked on 3 Chat boxes : 
-	The first one is for finding the top restaurants in the world
-	The second one is for searching music depends on genre 
-	The third one is for the weather depends on location

I have made the specific choices of Chat boxes in order to provide useful and basic information through links to the user,  simplifying their lives.

I would like the chat box to be capable of understanding every day needs of the user and to be able to make life easier. Chat box must be trained to make more complicated and specified actions.

## Assignment 2

## Handling Chitchat and Invalid Inputs

To handle chitchat and invalid inputs, the following changes were made:

- Added a story and rule in `stories.yml` and `rules.yml` to respond appropriately to chitchat.
- Implemented the `utter_chitchat` response in `domain.yml` to provide a friendly response during chitchat.

## Examples for Each Policy

### RulePolicy

#### Works Well:
- User: "Goodbye"
- Bot: "Bye"
- Explanation: The RulePolicy is effective in handling straightforward rules, such as responding to a specific intent like "goodbye."

#### Doesn't Work Well:
- User: "Tell me a joke"
- Bot: "I am a bot, powered by Rasa."
- Explanation: The RulePolicy may not handle more complex interactions like asking for a joke.
- But with the changes for Handling Chitchat responds well ("I'm here to assist you. If you have any specific questions or requests, feel free to let me know!")


### MemoizationPolicy

#### Works Well:
- User: "Play some music"
- Bot: "What type of music do you want to listen to?"
- User: "I'm in the mood for pop music"
- Bot: (Continues with the relevant actions)
- Explanation: MemoizationPolicy can effectively handle multi-turn conversations.

#### Doesn't Work Well:
- User: "Play some music"
- Bot: "What type of music do you want to listen to?"
- User: "What's the weather like in Paris?"
- Bot: (Confused response)
- Explanation: MemoizationPolicy may struggle with context changes.

### TEDPolicy

#### Works Well:
- User: "What's the weather?"
- Bot: "Sure, I can provide you with the current weather. Which location?"
- User: "Paris"
- Bot: (Continues with the relevant actions)
- Explanation: TEDPolicy handles context switches and generalizes well.

## Policy Optimization
Experimentation with different policy hyperparameters, increased training data, and adjustments to policy weights were performed to find the optimal combination for the specific use case.

