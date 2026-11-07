
import json
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess_text


class FAQChatbot:

    def __init__(self):
        # Locate the FAQ dataset
        base_dir = os.path.dirname(os.path.abspath(__file__))
        faq_path = os.path.join(base_dir, "data", "faqs.json")

        # Load FAQs from JSON
        with open(faq_path, "r", encoding="utf-8") as file:
            self.faqs = json.load(file)

        if not self.faqs:
            raise ValueError("FAQ dataset is empty.")

        # Extract and preprocess FAQ questions
        self.questions = [
            preprocess_text(faq["question"])
            for faq in self.faqs
        ]

        # Convert questions into TF-IDF vectors
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(
            self.questions
        )

    def get_response(self, user_question):

        # Preprocess user's question
        cleaned_question = preprocess_text(user_question)

        if not cleaned_question:
            return "Please enter a meaningful question.", 0.0

        # Convert user question into a TF-IDF vector
        user_vector = self.vectorizer.transform(
            [cleaned_question]
        )

        # Calculate cosine similarity
        similarities = cosine_similarity(
            user_vector,
            self.question_vectors
        )

        # Find the closest matching FAQ
        best_match_index = similarities.argmax()
        best_score = similarities[0][best_match_index]

        # Minimum similarity threshold
        threshold = 0.25

        if best_score < threshold:
            return (
                "Sorry, I couldn't find a suitable answer. "
                "Please try asking something related to college FAQs.",
                float(best_score)
            )

        # Return the matching answer
        answer = self.faqs[best_match_index]["answer"]

        return answer, float(best_score)


if __name__ == "__main__":

    chatbot = FAQChatbot()

    print("\nFAQ Chatbot is ready!")
    print("Type 'exit' to stop.\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        response, score = chatbot.get_response(question)

        print(f"Chatbot: {response}")
        print(f"Similarity Score: {score:.2f}\n")
