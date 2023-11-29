morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/','?':'..--..','!':'-.-.--','(':'-.--.',')':'-.--.-'}
#This function is used to translate from english text to morse code
def english_to_morse(text):
#Firstly it converts the input text to upper case so it can be found in the dictinary.  
  text= text.upper()
  morse_code= ' '
  for char in text:
#If the charcter is not present in Morse code dictionary, a Value error is raised with an appropriate error message.
    if char not in morse_dict:
      raise ValueError ("The value doesn't exist ")
#If the charcter is present in Moese code dictionary, the corresponding Morse code is added to the output string. 
    else:
      morse_code += morse_dict[char]+' '
#Finally, the function returns the output string, which contains the Morse code translation of the input text.
  return morse_code
#This function is used to convert from morse code to english text.
def morse_to_english(morse_code):
#It creates a reverse mapping of the Morse code dictionary by swapping the keys and values. 
  morse_dict_map = {v: k for k, v in morse_dict.items()}
#It then splits the Input Morse code into a list of symbols. 
  morse_code = morse_code.split()
  text= ' '
  for symbol in morse_code:
#If the symbol in not present in the reverse mapping of Morse code dictionary, a Value error is raised with an appropriate error message.
    if symbol not in morse_dict_map:
      raise ValueError ("The value doesn't exist ")
#If the symbol is present in the reverse mapping of morse code dictionary, The corresponding English charcter is added to the output string. 
    else:
      text += morse_dict_map[symbol]
  return text
#The function is_morse is used to scan the input of the user whether it is morse code or englsih text so it can provide the right output.
def is_morse(message):
  return any(c in ['-', '.'] for c in message)
#Try except block was used to handle any Value error exception that may be raised when an invalid character is encountered in the input text or morse code. 
try:
  text= input("Enter English text For conversion to Morse code, or Morse code for conversion to English test: ")
  if is_morse(text):
    choosen_function= morse_to_english
  else:
    choosen_function= english_to_morse
  result = choosen_function(text)

  print(result)
except ValueError as m:
  print(m)