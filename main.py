import os.path

from qrcodegenerator import create_qr_code_image  # import function to create qr code image
from config import Config  # import config file


def main():
    full_path = os.getcwd()  # get current working directory

    directory_path_and_file_name = os.path.join(full_path, Config.QR_CODE_IMAGE_DIRECTORY,
                                                Config.QR_CODE_DEFAULT_FILE_NAME)  # create full path to image

    qr_image = create_qr_code_image(Config.QR_CODE_DEFAULT_URL)  # create qr code image
    for i in range(0, 1):  # loop to create multiple qr code images
        while True:  # loop to check if file name already exists
            try:  # try to save image
                qr_image.save(directory_path_and_file_name)  # save image
            except FileNotFoundError:  # if file name already exists
                qr_image_directory = Config.QR_CODE_IMAGE_DIRECTORY  # get directory name
                new_directory_path = os.path.join(full_path, qr_image_directory)  # create new directory path
                os.mkdir(new_directory_path)  # create new directory
                continue  # continue loop to save image
            break  # break loop to save image


if __name__ == "__main__":
    main()
