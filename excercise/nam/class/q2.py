import cv2

class Image:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.image_name = image_path.split('/')[-1].split('.')[0]

    def show_image_name(self):
        print("Image name:", self.image_name)

    def show_image_shape(self):
        print("Image shape:", self.image.shape)

class ImageManipulator(Image):
    def reshape_image(self, shape):
        resized_image = cv2.resize(self.image, shape)
        cv2.imwrite(self.image_path, resized_image)
        print("Image resized to:", shape)
        self.show_image_shape()

image_path = "c:/Users/admin/Pictures/Co_do_sao_vang.png"
image = ImageManipulator(image_path)
image.show_image_name()
image.show_image_shape()
image.reshape_image((500, 500))