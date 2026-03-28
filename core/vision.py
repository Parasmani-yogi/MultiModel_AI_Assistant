from PIL import Image

def load_image(image_path):
    return Image.open(image_path)


def preprocess_image(image_path, size=(512, 512)):
    image = Image.open(image_path)
    image = image.resize(size)
    return image