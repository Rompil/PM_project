import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert to grayscale script")
    parser.add_argument("-o", dest="open_path", required=True)
    parser.add_argument("-s", dest="save_path", required=True)
    return parser.parse_args()
