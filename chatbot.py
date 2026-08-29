
import json
import re
import os
from difflib import SequenceMatcher


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAQ_FILE = os.path.join(BASE_DIR, "faq_data.json")

with open(FAQ_FILE, "r", encoding="utf-8") as file:
    faqs = json.load(file)


stop_words = {
    "the", "is", "are", "a", "an", "when", "what", "where",
    "how", "can", "i", "my", "for", "to", "of", "do", "does"
}


def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    synonyms = {
        "timings": "timing",
        "hours": "timing",
        "closes": "close",
        "closing": "close",
        "opens": "open",
        "opening": "open",
        "examinations": "exam",
        "examination": "exam",
        "fees": "fee",
        "exams": "exam"
    }

    words = text.split()

    return set(
        synonyms.get(word, word)
        for word in words
        if word not in stop_words
    )


def calculate_score(user_question, faq):
    user_text = user_question.lower()
    user_words = normalize(user_question)
    question_words = normalize(faq["question"])

    score = len(user_words.intersection(question_words)) * 2

    for keyword in faq["keywords"]:
        keyword_words = normalize(keyword)

        if keyword.lower() in user_text:
            score += 5
        elif keyword_words.intersection(user_words):
            score += 2

    similarity = SequenceMatcher(
        None,
        user_text,
        faq["question"].lower()
    ).ratio()

    score += similarity * 5

    return score


def find_answer(user_question):
    if not user_question.strip():
        return "Please type a question first."

    results = []

    for faq in faqs:
        score = calculate_score(user_question, faq)
        results.append((score, faq))

    results.sort(key=lambda item: item[0], reverse=True)

    best_score, best_faq = results[0]
    second_score = results[1][0] if len(results) > 1 else 0

    if best_score < 4:
        return (
            "Sorry, I could not find a reliable answer in the "
            "college FAQ knowledge base."
        )

    if best_score - second_score < 1.5:
        return (
            "Could you please provide more details? "
            "Your question may match more than one FAQ."
        )

    return best_faq["answer"]


def run_terminal_chatbot():
    print("College FAQ Chatbot")
    print("Ask a question or type 'exit' to stop.\n")

    while True:
        user_question = input("You: ")

        if user_question.lower() == "exit":
            print("LPU Connect: Goodbye!")
            break

        answer = find_answer(user_question)
        print("LPU Connect:", answer)


if __name__ == "__main__":
    run_terminal_chatbot()