from abc import abstractmethod

from src.main.GUI.View.imageVaults.imageVault import ImageVault


class ImageVaultWithHighlights(ImageVault):
    def __init__(self):
        super().__init__()
        self.__highlighted_images = self._load_highlighted_images()

    def get_highlighted(self, image_code):
        return self.__highlighted_images[image_code].sprite

    @abstractmethod
    def _load_highlighted_images(self):
        """
        :rtype: dict
        """
        pass

    def _scale_images(self, zoom):
        super()._scale_images(zoom)
        for key in self.__highlighted_images:
            self.__highlighted_images[key].zoom(zoom)
