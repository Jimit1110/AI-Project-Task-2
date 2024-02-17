import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 170)    # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Paragraphs of text to be converted to speech
paragraph1 = "hi, I'm jimit"
paragraph2 = "what's your name"
paragraph3 = ""

# Concatenate paragraphs
text = paragraph1 + " " + paragraph2 + " " + paragraph3

# Convert text to speech
engine.save_to_file(text, 'output.mp3')

# Wait for the speech to finish
engine.runAndWait()
