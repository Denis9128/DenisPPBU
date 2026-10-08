from PIL import Image, ImageTk
import stepic


def encod_text(image_path, text, output_path):
    image = Image.open(image_path)
    encod_image = stepic.encode(image, text.encode())
    encod_image.save(output_path)


encod_text('C:\\Photos\\100.png','Parol 100500@#$','encoded.png')
print('текст скрыт в изображении')




