

import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

# Sample data for banking services
services = {
    "balance": "Your current balance is $5000.",
    "transactions": "Here are your last 5 transactions: ...",
    "transfer": "To transfer money, please provide the recipient's account number and the amount.",
    "loan": "To apply for a loan, please provide the loan amount and your preferred term.",
    "support": "For customer support, please contact us at support@bank.com or call 1-800-123-4567."
}

def extract_query_type(user_input):
    # Tokenize and remove stop words
    words = word_tokenize(user_input.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    
    # Define patterns for different queries
    patterns = {
        "balance": re.compile(r"\b(balance|account balance|my balance)\b"),
        "transactions": re.compile(r"\b(transactions|recent transactions|transaction history)\b"),
        "transfer": re.compile(r"\b(transfer|send money|make a transfer)\b"),
        "loan": re.compile(r"\b(loan|apply for a loan|loan application)\b"),
        "support": re.compile(r"\b(support|help|customer service)\b")
    }
    
    for service, pattern in patterns.items():
        if pattern.search(user_input):
            return service
    return None

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    # Extract the query type
    query_type = extract_query_type(user_input)
    
    if query_type in services:
        return services[query_type]
    
    return "I'm not sure how to help with that. Can you provide more details or specify your request?"

# Main loop for the chatbot
def main():
    print("Welcome to the banking chatbot! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()

