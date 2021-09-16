#!/usr/bin/python3

from PIL import Image
import argparse

# from string_art.src.arg_parser import parse_arguments


class Picture:
    def __init__(self, open_path: str) -> None:
        self.image = Image.open(open_path)

    def convert_to_grayscale(self) -> None:
        self.image = self.image.convert('L')

    def save(self, save_path: str) -> None:
        self.image.save(save_path)

    def resize(self, new_size: tuple) -> None:
        self.image = self.image.resize(new_size)

    def thumbnail_resize(self, new_size: tuple) -> None:
        """ Resize image and keeping it aspect ratios"""
        self.image.thumbnail(new_size)

    def crop(self, box: tuple) -> None:
        """ Crop an image

        :param box: the position and size of the cropped region (left, upper, right, lower)
        :return: None
        """
        self.image = self.image.crop(box)


if __name__ == '__main__':
    # args = parse_arguments()

    parser = argparse.ArgumentParser(description="Convert to grayscale script")
    parser.add_argument("-o", dest="open_path", required=True)
    parser.add_argument("-s", dest="save_path", required=True)
    parser.add_argument("--resize", dest="new_size", nargs="+", type=int)
    parser.add_argument("--t_resize", dest="t_size", nargs="+", type=int)
    parser.add_argument("--crop", dest="crop_box", nargs="+", type=int)
    args = parser.parse_args()

    corgi = Picture(args.open_path)
    corgi.convert_to_grayscale()
    if args.new_size:
        corgi.resize(tuple(args.new_size))
    if args.t_size:
        corgi.thumbnail_resize(tuple(args.t_size))
    if args.crop_box:
        corgi.crop(tuple(args.crop_box))

    corgi.save(args.save_path)
