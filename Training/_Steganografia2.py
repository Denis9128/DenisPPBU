from PIL import Image
import stepic

def decode_text(image_path):
    image = Image.open(image_path)
    decoded_text = stepic.decode(image)
    return decoded_text

text = decode_text('encoded.png')
print(text)
