from config import config_instance
from controllers.test import test
from controllers.close_eye import closeEye
from controllers.open_eye import openEye

urls = [
    (r"/post_image", test),
    (r"/post_openeye", openEye),
    (r"/post_closeeye", closeEye),
]