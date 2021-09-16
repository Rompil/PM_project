#!/usr/bin/python3

from PIL import Image
import argparse

# from string_art.src.arg_parser import parse_arguments


class Picture:
    def __init__(self, open_path: str) -> None:
        self.image = Image.open(open_path)

    def save_as_grayscale(self, save_path: str) -> None:
        img = self.image.convert('L')
        img.save(save_path)


if __name__ == '__main__':
    # args = parse_arguments()

    parser = argparse.ArgumentParser(description="Convert to grayscale script")
    parser.add_argument("-o", dest="open_path", required=True)
    parser.add_argument("-s", dest="save_path", required=True)
    args = parser.parse_args()

    corgi = Picture(args.open_path)
    corgi.save_as_grayscale(args.save_path)
