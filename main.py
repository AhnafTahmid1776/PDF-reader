# importing the modules
import PyPDF2
import pyttsx3
# path of the PDF file
path = open('/home/saad/Documents/text2speech/test1.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)

# the page with which you want to start
# this will read the page of 25th page.
from_page = pdfReader.getPage(2)

# extracting the text from the PDF
text = from_page.extractText()

# reading the text

speak = pyttsx3.init()

speak.setProperty('rate', 160)

speak.say(text)
speak.runAndWait()
