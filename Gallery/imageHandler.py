from .models import Picture
from PIL import Image


def shrink_image(from_p, to_p):
    im = Image.open(from_p)
    im.thumbnail((300, 300))
    im.save(to_p)
