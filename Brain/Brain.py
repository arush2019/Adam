import os
import requests

question = "what is python"

def search_local_file(question):
    # Specify the path to the local file where answers are stored
    file_path = "E:/Adam/DataBase/chat_log.txt"

    # Check if the file exists
    if os.path.exists(file_path):
        # Open the file for reading
        with open(file_path, 'r') as file:
            # Read the content line by line
            for line in file:
                # Split the line into question and answer
                stored_question, answer = line.strip().split(':')

                # Compare the stored question with the provided question
                if stored_question.strip().lower() == question.strip().lower():
                    print( answer.strip())
                    break

                else:
                    print("Sorry, I don't know the answer to that question.")

    else:
        return open(file_path, "w")
    
search_local_file(question)




#def search_internet(question):
    # Make an internet search query
    #search_query = "site:wikipedia.org " + question

    # Send a GET request to search the internet
    #response = requests.get("https://www.google.com/search", params={"q": search_query})

    # Check if the request was successful
    #search_results = response.text

        # Extract the answer from the search results using some parsing or scraping technique
        #answer = extract_answer_from_search_results(search_results)

        # Return the answer if found, otherwise return None
        #if answer:
            #return answer

    # Return None if the answer is not found on the internet
    #return None


#def extract_answer_from_search_results(search_results):
    # Implement your own logic to extract the answer from the search results
    # This could involve parsing HTML, using regular expressions, or using a library like BeautifulSoup

    # Return a placeholder value for now
    #return "Answer extracted from search results"


#def save_to_local_file(question, answer):
    # Specify the path to the local file where answers are stored
    #file_path = "E:/Adam/DataBase/chat_log.txt"

    # Open the file in append mode and write the question and answer
    #with open(file_path, 'a') as file:
        #file.write(question.strip() + ":" + answer.strip() + "\n")

# Main function
#def find_answer(question):
    # Search in the local file first
    #answer = search_local_file(question)

    # If the answer is not found in the local file, search on the internet
    #if not answer:
        #answer = search_internet(question)

        # If the answer is found on the internet, save it to the local file
        #if answer:
            #save_to_local_file(question, answer)

    #return answer

# Example usage
#question = input("Enter your question: ")
#answer = find_answer(question)

#if answer:
    #print("Answer:", answer)
#else:
    #print("Answer not found.")
