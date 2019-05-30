from models import Usb


def calculate(usb_size, memes):
    """
    :param usb_size: size of usb stick
    :param memes: list of tuples with memes (name, size, price)
    :return:tuple with the first element being the total value of all memes on  the USB stick,
    and the second being the set of names of the memes that should be copied onto the USB stick to maximize its value
    """

    # 1 GiB = 1024 MiB
    usb_size *= 1024

    # create matrix of all possible sizes of usb stick and quantity of memes inside it
    # it's important to remember that usb stick can have 0 capacity and there could be 0 memes
    best_values = [[Usb() for x in range(usb_size + 1)] for y in range(len(memes) + 1)]

    for i in range(1, len(memes) + 1):
        for j in range(1, usb_size + 1):

            # if current usb stick size cannot fit meme, assign memes from smaller one
            if j - memes[i - 1][1] < 0:
                best_values[i][j] = best_values[i - 1][j]
                continue

            # if usb stick with i - 1 possible memes is more valuable than this with i memes
            # current usb stick = this with i-1 memes
            if best_values[i - 1][j].value > best_values[i - 1][j - memes[i - 1][1]].value + memes[i - 1][2]:
                best_values[i][j] = best_values[i - 1][j]

            # else add copy usb stick with i-1 memes and add i-th meme
            else:
                best_values[i][j].value = best_values[i - 1][j - memes[i - 1][1]].value + memes[i - 1][2]
                best_values[i][j].meme_set = best_values[i - 1][j - memes[i - 1][1]].meme_set.copy()
                best_values[i][j].meme_set.add(memes[i - 1][0])

    # return tuple of value and set of meme names
    return best_values[len(memes)][usb_size].value, best_values[len(memes)][usb_size].meme_set


usb_size = 1
memes = [
    ('rollsafe.jpg', 205, 6),
    ('sad_pepe_compilation.gif', 410, 10),
    ('yodeling_kid.avi', 605, 12)
]
print(calculate(usb_size, memes))
