
from PIL import Image
import argparse

# from string_art.src.arg_parser import parse_arguments


def convert_to_gs(img_open_path: str, img_save_path: str):
    """ Convert image from rgb into grayscale

    :param img_open_path: path to the image
    :param img_save_path: path to save the result
    :return:
    """
    img = Image.open(img_open_path).convert('L')
    img.save(img_save_path)


if __name__ == '__main__':
    # args = parse_arguments()

    parser = argparse.ArgumentParser(description="Convert to grayscale script")
    parser.add_argument("-o", dest="open_path", required=True)
    parser.add_argument("-s", dest="save_path", required=True)
    args = parser.parse_args()

    convert_to_gs(args.open_path, args.save_path)
