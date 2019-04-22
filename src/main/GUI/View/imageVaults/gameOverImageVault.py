from src.main.GUI.View.image import Image
from src.main.GUI.View.imageVaults.imageVault import ImageVault
from src.main.constants import GameOverImageEnum


class GameOverImageVault(ImageVault):
    def set_camera_zoom(self, camera_zoom):
        pass

    def _load_images(self):
        background = Image(400, 400, '../../artwork/images/gameOverBackground.png')
        background.set_alpha(100)
        return {
            GameOverImageEnum.BACKGROUND: background,
        }
