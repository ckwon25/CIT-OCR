from paddleocr import PaddleOCR

ocr = PaddleOCR(lang="en")

result = ocr.ocr("/Users/calvin.kwon/Desktop/license_small.jpeg")

texts = result[0]["rec_texts"]

for text in texts:
    print(text)
