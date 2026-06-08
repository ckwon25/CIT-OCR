from paddleocr import PaddleOCR
from PIL import Image, ImageOps
import tempfile

ocr = PaddleOCR(lang="en")


def resize_image(path):

    img = Image.open(path)

    img = ImageOps.exif_transpose(img)

    img.thumbnail((1500, 1500))

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    )

    img.save(temp.name)

    return temp.name


def extract_text(path):

    resized = resize_image(path)

    result = ocr.ocr(resized)

    texts = result[0]["rec_texts"]

    return "\n".join(texts)