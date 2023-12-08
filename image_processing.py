import easyocr
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import io
from translation import translate_text

def process_image(img):
    reader = easyocr.Reader(['de'])
    img_np = np.array(img)
    result = reader.readtext(img_np)
    img_with_black_rectangles_and_text = img.copy()
    draw = ImageDraw.Draw(img_with_black_rectangles_and_text)
    font = ImageFont.load_default()

    for (bbox, text, _) in result:
        top_left = tuple(bbox[0])
        bottom_right = tuple(bbox[2])
        translated_text = translate_text(text)
        draw.rectangle([top_left, bottom_right], fill="black")
        text_width, text_height = draw.textsize(translated_text, font=font)
        text_position = (
        (bottom_right[0] + top_left[0] - text_width) // 2, (bottom_right[1] + top_left[1] - text_height) // 2)
        draw.text(text_position, translated_text, fill="white", font=font)

    return img_with_black_rectangles_and_text
