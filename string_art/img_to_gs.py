import pathlib

from PIL import Image


def convert_to_gs(img_open_path: str, img_save_path: str):
    """ Convert image from rgb into grayscale

    :param img_open_path: path to the image
    :param img_save_path: path to save the result
    :return:
    """
    img = Image.open(img_open_path).convert('LA')
    img.save(img_save_path)


if __name__ == '__main__':
    print(pathlib.Path().resolve())
    open_ = str(pathlib.Path().resolve()) + r"\images\corgi.jpg"
    save_ = str(pathlib.Path().resolve()) + r"\images\corgi_gs.png"
    convert_to_gs(open_, save_)
