import os
from PIL import Image


def convert_images(source_folder, target_format='jpeg'):
    if not os.path.exists(source_folder):
        print('پوشه مبدا وجود ندارد!')
        return

    valid_formats = ('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff')
    if target_format not in valid_formats:
        print(f'فرمت نهایی معتبر نیست! یکی از فرمت های زیر را انتخاب کنید: {valid_formats}')
        return

    for filename in os.listdir(source_folder):
        if filename.endswith(valid_formats):
            image_path = os.path.join(source_folder, filename)
            with Image.open(image_path) as img:
                target_path = os.path.splitext(image_path)[0] + '.' + target_format
                img.convert('RGB').save(target_path, target_format.upper())
            print(f'{filename} به {target_format} تبدیل شد')


if __name__ == "__main__":
    print('Enter a folder, to all image in folder change the format!')
    source_folder = input('path folder: ')
    target_format = input('new format: ')

    convert_images(source_folder, target_format)
