import pathlib

from PIL import Image


class Picture:
    def __init__(self, path):
        self.image = Image.open(path)

    def save_as_grayscale(self, path):
        img = self.image.convert('L')
        img.save(path)


if __name__ == '__main__':
    corgi = Picture(str(pathlib.Path().resolve()) + r"\images\corgi.jpg")
    corgi.save_as_grayscale(str(pathlib.Path().resolve()) + r"\images\corgi_gs2.png")