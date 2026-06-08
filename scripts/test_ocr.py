from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en"
)

result = ocr.ocr("IMG_8708_small.jpeg")

for page in result:
    for line in page:
        print(result)