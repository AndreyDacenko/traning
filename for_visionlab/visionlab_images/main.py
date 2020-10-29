import requests
import os


# ------------------  PATHS  ------------------

your_website_url = ''
url = your_website_url + '/images'
# your_website_url = 'https://yandex.ru/'
# url = your_website_url + 'images/'


path_to_folder = input("path to folder with images: ")
# path_to_folder = os.getcwd() + '/pictures'


#  ---------------  MAIN  ----------------


def choose_images(path):
    # choose only jpg and png format files in your folder
    files_path = []
    for address, dirs, files in os.walk(path):
        for file in files:
            files_path.append(path + '\\' + str(file))
    filtered_image_list = [x for x in files_path if x.endswith('.jpg' or '.png')]
    return filtered_image_list


def send_images(images):
    multiple_files = [('file', (image, open(image, 'rb'), 'images')) for image in images]
    r = requests.post(url, files=multiple_files)
    r.raise_for_status()
    # print(r.status_code)
    # print(r.text)


# ------------------------------------------------------------------------------------------


if __name__ == '__main__':
    paths_to_images = choose_images(path_to_folder)
    send_images(paths_to_images)
