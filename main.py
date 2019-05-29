import pprint


def calculate(usb_size, memes):
    """
    :param usb_size: size of usb stick
    :param memes: list of tuples with memes (name, size, price)
    :return:tuple with the first element being the total value of all memes on  the USB stick,
    and the second being the set of names of the memes that should be copied onto the USB stick to maximize its value
    """

    usb_size = 12

    best_values = [[0 for x in range(usb_size + 1)] for y in range(len(memes) + 1)]

    for i in range(1, len(memes) + 1):
        for j in range(1, usb_size + 1):
            if j - memes[i - 1][1] < 0:
                best_values[i][j] = best_values[i - 1][j]
                continue
            best_values[i][j] = max(best_values[i - 1][j], best_values[i - 1][j - memes[i - 1][1]] + memes[i - 1][2])

    pprint.pprint(best_values)


usb_size = 1
memes = [
    ('rollsafe.jpg', 3, 5),
    ('sad_pepe_compilation.gif', 3, 7),
    ('yodelng_kid.avi', 3, 5),
    ('rollfe.jpg', 3, 9),
    ('sad_pepe_compilation.gif', 3, 3),
    ('yodeling_kid.avi', 3, 5),
    ('rollsafe.jpg', 3, 5),
    ('sad_pepe_compilation.gif', 3, 5),
    ('yodeling_kid.avi', 3, 7),
    ('rollsafe.jpg', 2, 4),
    ('sad_pepe_compilation.gif', 2, 6),
    ('yodeling_kid.avi', 2, 8),
    ('rollsafe.jpg', 2, 4),
    ('sad_pepe_compilation.gif', 2, 6),
    ('yodeling_kid.avi', 2, 6),
    ('z', 2, 2)
]
calculate(usb_size, memes)
