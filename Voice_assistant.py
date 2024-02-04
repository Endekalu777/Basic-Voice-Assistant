import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=30, phrase_time_limit=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio).lower()
            print("User:", query)
            process_command(query)
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
            speak("Sorry, I didn't catch that. Could you please repeat?")
        except sr.RequestError as e:
            print(f"Error accessing the speech recognition service: {e}")
            speak("Sorry, I'm having trouble accessing the speech recognition service.")

# Function to process voice commands
def process_command(command):
    if "name" in command and "hello" in command:
        response = "Hello, My name is Ashisword AI"
        speak(response)
    elif "hello" in command:
        response = "Hello! How can I assist you today?"
        speak(response)
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}."
        speak(response)
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %d %B %Y")
        response = f"Today is {current_date}."
        speak(response)

    elif "name" in command:
        response="My name is Ashisword AI"
        speak(response)
    elif "search" in command:
        query = command.replace("search", "").strip()
        search_url = "https://www.google.com/search?q=" + query
        webbrowser.open(search_url)
        response = f"Here are the search results for {query}."
        speak(response)
    else:
        response = "Sorry, I don't understand. Could you please repeat?"
        speak(response)

# Main program loop
if __name__ == "__main__":
    speak("Hello! How can I assist you today?")
    while True:
        listen()