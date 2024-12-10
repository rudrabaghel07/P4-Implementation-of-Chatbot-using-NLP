import streamlit as st
import re


# Intent patterns and responses
intents = [
    {
        "tag": "greeting",
        "patterns": ["Hi", "Hello", "Hey", "How are you", "What's up"],
        "responses": ["Hi there", "Hello", "Hey", "I'm fine, thank you", "Nothing much"]
    },
    {
        "tag": "goodbye",
        "patterns": ["Bye", "See you later", "Goodbye", "Take care"],
        "responses": ["Goodbye", "See you later", "Take care"]
    },
    {
        "tag": "thanks",
        "patterns": ["Thank you", "Thanks", "Thanks a lot", "I appreciate it"],
        "responses": ["You're welcome", "No problem", "Glad I could help"]
    },
    {
        "tag": "about",
        "patterns": ["What can you do", "Who are you", "What are you", "What is your purpose"],
        "responses": ["I am a chatbot", "My purpose is to assist you", "I can answer questions and provide assistance"]
    },
    {
        "tag": "help",
        "patterns": ["Help", "I need help", "Can you help me", "What should I do"],
        "responses": ["Sure, what do you need help with?", "I'm here to help. What's the problem?", "How can I assist you?"]
    },
    {
        "tag": "age",
        "patterns": ["How old are you", "What's your age"],
        "responses": ["I don't have an age. I'm a chatbot.", "I was just born in the digital world.", "Age is just a number for me."]
    },
    {
        "tag": "weather",
        "patterns": ["What's the weather like", "How's the weather today"],
        "responses": ["I'm sorry, I cannot provide real-time weather information.", "You can check the weather on a weather app or website."]
    },
    {
        "tag": "budget",
        "patterns": ["How can I make a budget", "What's a good budgeting strategy", "How do I create a budget"],
        "responses": ["To make a budget, start by tracking your income and expenses. Then, allocate your income towards essential expenses like rent, food, and bills. Next, allocate some of your income towards savings and debt repayment. Finally, allocate the remainder of your income towards discretionary expenses like entertainment and hobbies.", "A good budgeting strategy is to use the 50/30/20 rule. This means allocating 50% of your income towards essential expenses, 30% towards discretionary expenses, and 20% towards savings and debt repayment.", "To create a budget, start by setting financial goals for yourself. Then, track your income and expenses for a few months to get a sense of where your money is going. Next, create a budget by allocating your income towards essential expenses, savings and debt repayment, and discretionary expenses."]
    },
    {
        "tag": "credit_score",
        "patterns": ["What is a credit score", "How do I check my credit score", "How can I improve my credit score"],
        "responses": ["A credit score is a number that represents your creditworthiness. It is based on your credit history and is used by lenders to determine whether or not to lend you money. The higher your credit score, the more likely you are to be approved for credit.", "You can check your credit score for free on several websites such as Credit Karma and Credit Sesame."]
    }
]


# NLP logic to process user input
def chatbot_response(user_input):
    """
    Process user input and match against intents using regex.
    Returns a response based on intent matching.
    """
    # Loop through intents to find a match
    for intent in intents:
        for pattern in intent['patterns']:
            if re.search(pattern, user_input, re.IGNORECASE):
                # Randomly select a response from the matched intent's responses
                return intent['responses'][0]  # You can implement random choice if needed
    # Default response if no intent is matched
    return "I'm sorry, I don't understand that. Could you please rephrase your question?"


# Main Streamlit UI
def main():
    st.title("NLP-Based Chatbot with Intents")
    st.write("Welcome! This chatbot responds intelligently using NLP logic based on your input.")

    # Session state for conversation history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Input box for user
    user_input = st.text_input("You:")

    if user_input:
        # Process user input and generate chatbot response
        response = chatbot_response(user_input)

        # Store user input and chatbot response in session history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Chatbot", response))

    # Display conversation history
    st.write("### Conversation History")
    for speaker, message in st.session_state.chat_history:
        st.write(f"**{speaker}:** {message}")

    # Handle goodbye intent
    if user_input and user_input.lower() in ['bye', 'goodbye']:
        st.write("Thank you for chatting with me. Goodbye!")


# Run the chatbot
if __name__ == '__main__':
    main()
