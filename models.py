class Usb:
    """
    Model class for usb stick with memes
    It contains current value and set of memes saved on it
    """

    def __init__(self):
        self.value = 0
        self.meme_set = set()
