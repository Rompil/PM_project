import pathlib

from string_art.src.image import Picture

TEST_PICTURE_PATH = str(pathlib.Path().resolve()) + r"\test_images\corgi.jpg"


def test_crop():
    img = Picture(TEST_PICTURE_PATH)
    assert img.image.size == (4032, 3024)
    img.crop((500, 500, 2000, 2000))
    assert img.image.size == (1500, 1500)


def test_resize():
    img = Picture(TEST_PICTURE_PATH)
    assert img.image.size == (4032, 3024)
    img.resize((500, 500))
    assert img.image.size == (500, 500)


def test_convert_to_gs():
    img = Picture(TEST_PICTURE_PATH)
    before = img.image
    img.convert_to_grayscale()
    after = img.image
    assert before != after


def test_thumbnail_resize():
    img = Picture(TEST_PICTURE_PATH)
    assert img.image.size == (4032, 3024)
    img.thumbnail_resize((500, 500))
    assert img.image.size == (500, 375)
