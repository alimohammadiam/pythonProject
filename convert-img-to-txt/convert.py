from PIL import Image
import pytesseract
from pathlib import Path
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
translator = Translator()

text = ""
ans = input('Do you want text of photos translate to Farsi ? (y/n): ')

for path in Path('fa-img').iterdir():
    if path.is_file():
        img = path
        text += pytesseract.image_to_string(Image.open(img), lang="fas")
        text += '\n' + (100 * '_') + '\n'

for path in Path('eng-img').iterdir():
    if path.is_file():
        img = path
        eng = pytesseract.image_to_string(Image.open(img), lang="eng")
        if 'y' in ans.lower():
            text += str(translator.translate(eng, src='en', dest='fa'))

        else:
            text += eng
        text += '\n' + (100 * '_') + '\n'

print(text)
