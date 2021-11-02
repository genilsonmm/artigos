import cv2


class ImageProcessing:

    def __init__(self):
        print('Image Processing')

    def to_gray(self, img_path):
        img_bgr = cv2.imread(img_path)
        gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Image', gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Limiarização simples
    def simple_threshold(self, img_path, mim_threshold=127):
        img = cv2.imread(img_path)
        cv2.imshow('Original Image', img)

        cv2.waitKey(0)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray', gray)

        cv2.waitKey(0)

        # pixel com valor < 127 será 0. Maior que 127 será 255
        val, thresh = cv2.threshold(gray, mim_threshold, 255, cv2.THRESH_BINARY)

        cv2.imshow('THRESH_BINARY', thresh)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Limiarização com o método de otsu. O valor do threshold será calculado automativamente
    def otsu_threshold(self, img_path):
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        val, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        print('Limiar calculado (cada img possuirá um limiar diferente: ', val)
        cv2.imshow('THRESH_OTSU', otsu)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def adaptive_threshold(selfs, img_path):
        # Limiarização usando a média de pixels na região
        img = cv2.imread(img_path)
        cv2.imshow('Original Image', img)

        cv2.waitKey(0)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        val, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        print('Limiar calculado (cada img possuirá um limiar diferente: ', val)
        cv2.imshow('THRESH_OTSU', otsu)

        cv2.waitKey(0)

        adapt_media = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9)
        cv2.imshow('ADAPT_MEDIA', adapt_media)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def adaptive_gaussian_threshold(self, img_path):
        #Menos ruídos - Testar com imagens com sombras
        img = cv2.imread(img_path)
        cv2.imshow('Original Image', img)
        cv2.waitKey(0)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        adapt_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)
        cv2.imshow('ADAPT_MEDIA_GAUS', adapt_gaussian)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def invert_color(self, img_path):
        img = cv2.imread(img_path)
        cv2.imshow('Original Image', img)
        cv2.waitKey(0)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print(gray)
        cv2.waitKey(0)

        invert = 255 - gray
        print(invert)

        cv2.imshow('Imagem invertida', invert)
        cv2.waitKey(0)