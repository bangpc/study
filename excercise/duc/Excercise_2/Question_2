import cv2
import os

class Image():
    def __init__(self, image_path) -> None:
        self.image_path = image_path
        self.image = cv2.imread(self.image_path)

    def show_image_name(self):
        print(f"Image name: {self.image_path.split('/')[-1]}")

    def show_image_shape(self):
        height, width, channel = self.image.shape
        print(f"Image shape: {width}x{height}")


class ImagiManipulator(Image):
    def __init__(self, image_path) -> None:
        super().__init__(image_path)

    def reshape_image(self, shape):
        img_resized = cv2.resize(self.image, shape)
        cv2.imwrite(self.image_path, img_resized)
        self.image = img_resized
        self.show_image_shape()

image = ImagiManipulator('C:/Users/Ud/Downloads/Test1.jpg')
image.show_image_name()
image.show_image_shape()
image.reshape_image((2000, 2000))