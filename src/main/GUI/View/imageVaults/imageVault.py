from abc import ABCMeta, abstractmethod


class ImageVault(metaclass=ABCMeta):
    def __init__(self):
        self.__images = self._load_images()

    @abstractmethod
    def set_camera_zoom(self, camera_zoom):
        pass

    def get_sprite(self, image_code):
        """
        :rtype: pygame.Surface
        """
        return self.__images[image_code].sprite

    def get_image(self, image_code):
        """
        :rtype: src.main.GUI.View.image.Image
        """
        return self.__images[image_code]

    @abstractmethod
    def _load_images(self):
        """
        :rtype: dict
        """
        pass

    def _scale_images(self, zoom):
        for key in self.__images:
            self.__images[key].zoom(zoom)
