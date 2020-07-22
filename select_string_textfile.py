try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


file=open('C:\\Users\\inaee\\Desktop\\2020-1MAKERS\\OCR\\square_real\\real_scanned\\text\\real_text_45.txt', 'w', -1, "utf-8")
#UnicodeEncodeError: 'cp949' codec can't encode character '\xa9' in position 106: illegal multibyte sequence
#오류해결방법 -> open(file_name, 'w', -1, "utf-8") 로 수정 후 오류가 사라지고 정상 실행되었습니다.
#-1은 버퍼



#tesseract path
pytesseract.pytesseract.tessreact_cmd=r'C:\Program Files\Tesseract-OCR'

#영어 사진은 lang 안써도 되지만, 한글 사진은 lang을 써야지 한글로 판독하여 나타냄
text=pytesseract.image_to_string(Image.open('C:\\Users\\inaee\\Desktop\\2020-1MAKERS\\OCR\\square_real\\real_scanned\\real_scanned_45.jpg'), lang='eng+kor')

print(text)

file.write(text)
file.close()
