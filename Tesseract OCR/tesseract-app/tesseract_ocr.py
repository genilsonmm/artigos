import cv2
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\tesseract.exe'
import numpy as np
from PIL import ImageFont, Image, ImageDraw


class TesseractOCR:

    def __init__(self):
        self.config_pytesseract = '--tessdata-dir assets/tessdata'
        self.font = r'../assets/font/calibri.ttf'

    def read_text(self, img_path):
        return self.__get_text_from_img(img_path)

    def find(self, img_path, text):
        img_data = self.__get_image_data(img_path)
        funded = False
        threshold = 70

        for i in range(0, len(img_data['text'])):
            current_text = img_data['text'][i].upper()
            confidence = int(float(img_data['conf'][i]))
            if confidence > threshold and not current_text.isspace() and len(current_text) and current_text == text.upper():
                funded = True
                break

        return funded

    def find_all(self, img_path):
        img = self.__get_rgb_img(img_path)
        img_data = self.__get_image_data(img_path)
        img_copy = img.copy()
        threshold = 70

        for i in range(0, len(img_data['text'])):
            text = img_data['text'][i]
            confidence = int(float(img_data['conf'][i]))

            if confidence > threshold and not text.isspace() and len(text):
                print(text, confidence)
                x, y, img_copy = self.__draw_rectangle(img_data, img_copy, i)
                img_copy = self.__write_text(text, x, y, img_copy)

        cv2.imshow('Image', img_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def find_date(self, img_path):
        img = self.__get_rgb_img(img_path)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Image', gray_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Métodos privados
    def __draw_rectangle(self, result, img, index, color=(255, 100, 0)):
        x = result['left'][index]
        y = result['top'][index]
        w = result['width'][index]
        h = result['height'][index]
        thickness = 2
        cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)
        return x, y, img

    def __write_text(self, text, x, y, img, text_size=12):
        font_type = ImageFont.truetype(self.font, text_size)
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        draw.text((x, y - text_size), text, font=font_type, fill=(0, 0, 255))
        img = np.array(img_pil)
        return img

    def __get_text_from_img(self, img_path):
        img = self.__get_rgb_img(img_path)
        return pytesseract.image_to_string(img, lang='por', config=self.config_pytesseract)

    def __get_rgb_img(self, img_path):
        img_bgr = cv2.imread(img_path)
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        # self.__show_two_images(img_bgr, img_rgb)
        return img_rgb

    def __show_two_images(self, img1, img2):
        numpy_horizontal_concat = np.concatenate((img1, img2), axis=1)
        cv2.imshow('BGR -> RGB', numpy_horizontal_concat)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def __get_image_data(self, img_path):
        img = self.__get_rgb_img(img_path)
        return pytesseract.image_to_data(img, config=self.config_pytesseract, lang='por', output_type=Output.DICT)
