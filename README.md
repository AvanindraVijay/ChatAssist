
📌 Rasa Chatbot for Social Media Support
Tech Stack: Python · Rasa · Rasa NLU · YAML · Rasa X · Custom Actions

🧠 Overview
Developed a rule-based conversational AI chatbot using the Rasa framework to automate customer support for social media platforms. The bot handles a wide range of user queries related to account issues, age restrictions, content guidelines, and technical support, delivering 90%+ response accuracy.

This project demonstrates end-to-end implementation of a Rasa chatbot, leveraging natural language understanding (NLU) and custom action servers to simulate human-like conversations and automate repetitive support tasks.

🔨 Key Features & Contributions
🗂 Intent and Entity Recognition
Designed and implemented 15+ user intents (greet, goodbye, provide_age, etc.) and key entities (age, platform, issue_type) for intent classification and slot filling.

Enhanced training data with over 100+ sample utterances to improve intent prediction using Rasa NLU pipeline.

💬 Dialog Management
Structured multi-turn conversations using stories and rules to handle both happy paths and edge cases.

Incorporated slot filling and form validation to handle user eligibility checks (e.g., age restrictions for social media usage).

⚙️ Custom Actions
Created a custom Python action (action_check_age) to validate age input, restrict underage users, and respond with contextual messages using dispatcher.utter_message().

Handled logic for age-based access control, contributing to personalized, dynamic user responses.

📈 Rasa X Integration
Integrated with Rasa X for real-time chatbot testing, intent correction, and conversation flow improvements.

Iteratively trained and refined the model based on live user feedback and conversations.

📊 Results
🚀 Achieved over 90%+ response accuracy in simulated environments with multiple user scenarios.

📉 Reduced response time to common queries by automating 30–40% of typical support interactions.

✅ Improved intent recognition and slot-filling reliability by 25% after NLU and story optimizations.

📂 Folder Structure (Optional for GitHub)
graphql
Copy
Edit
📁 chatbot/
├── data/
│   ├── nlu.yml            # NLU training data: intents, examples, entities
│   ├── rules.yml          # Rule-based dialogue paths
│   └── stories.yml        # Example story paths for conversation flow
├── domain.yml             # Domain config: intents, entities, slots, responses, actions
├── actions.py             # Custom action logic
├── config.yml             # NLU pipeline and policy configurations
├── endpoints.yml          # Action server configuration
└── README.md              # Project documentation
✅ Skills Demonstrated
Natural Language Processing (NLP)

Conversational AI Design

Python Scripting

Rasa Framework & Rasa X

YAML Configuration

Rule-Based Logic & Custom Actions
