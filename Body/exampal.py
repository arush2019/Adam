import os
import requests
from googlesearch import search
from bs4 import BeautifulSoup

def find_answer(question, file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                stored_question, answer = line.strip().split(':')
                if stored_question.strip().lower() == question.strip().lower():
                    return answer.strip()
        return None
    else:
        return None

def save_answer(question, answer, file_path):
    with open(file_path, 'a') as file:
        file.write(f"{question.strip()}:{answer.strip()}\n")
    print(f"Question and answer saved successfully.")

def search_internet(question):
    try:
        search_results = search(question, num_results=5, lang='en')
        for result in search_results:
            try:
                response = requests.get(result)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    answer = soup.get_text()  # Extract the answer from the page
                    return answer
            except requests.exceptions.RequestException:
                continue
    except Exception as e:
        print(f"An error occurred during the internet search: {e}")
    return None

# Example usage
knowledge_base_file = 'knowledge_base.txt'
question_answer_file = 'question_answer.txt'

user_question = input("Enter your question: ")

answer = find_answer(user_question, knowledge_base_file)

if answer:
    print(answer)
else:
    print("Answer not found. Searching the internet...")

    answer = search_internet(user_question)

    if answer:
        print(answer)

        # Save the answer to the question-answer file
        save_answer(user_question, answer, question_answer_file)
    else:
        print("Unable to retrieve the answer from the internet.")
