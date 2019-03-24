from abc import ABCMeta, abstractmethod


class ImageVault(metaclass=ABCMeta):
    def __init__(self):
        self.__images = self._load_images()

    @abstractmethod
    def set_camera_zoom(self, camera_zoom):
        pass

    def get(self, image_code):
        return self.__images[image_code].sprite

    @abstractmethod
    def _load_images(self):
        """
        :rtype: dict
        """
        pass

    def _scale_images(self, zoom):
        for key in self.__images:
            self.__images[key].scale_sprite(zoom)
