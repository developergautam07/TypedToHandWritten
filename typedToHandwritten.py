import pywhatkit

# For Assignment.txt file text is read
with open('assignment.txt', 'r') as fobj:
    text = fobj.read()

pywhatkit.text_to_handwriting(text, 'assignment.png',  rgb=[0, 0, 255]) # Default is set to Blue color