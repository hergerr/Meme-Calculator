from models import Usb


def calculate(usb_size, memes):
    """
    Given the size of usb stick and list of tuples with memes (name, size, price),
    returns the best possible value of memes on usb stick and names of those memes
    """

    # 1 GiB = 1024 MiB
    usb_size *= 1024

    # create matrix of all possible sizes of usb stick and quantity of memes inside it
    # it's important to remember that usb stick can have 0 capacity and there could be 0 memes
    # and that n+1 sized array is needed (to store values from 0 to n)
    best_values = [[Usb() for x in range(usb_size + 1)] for y in range(len(memes) + 1)]

    for i in range(1, len(memes) + 1):
        for j in range(1, usb_size + 1):

            # if current usb stick size cannot fit meme, assign memes from smaller one
            if j - memes[i - 1][1] < 0:
                best_values[i][j] = best_values[i - 1][j]
                continue

            # if usb stick with i - 1 possible memes is more valuable than this with i memes
            # current usb stick = this with i-1 memes
            # memes[i - 1][1] is i-1st meme weight
            # memes[i - 1][2] is i-1st meme value
            # condition is build in that way that images size will never be bigger than usb size
            if best_values[i - 1][j].value > best_values[i - 1][j - memes[i - 1][1]].value + memes[i - 1][2]:
                best_values[i][j] = best_values[i - 1][j]

            # else add copy usb stick with i-1 memes and add i-th meme
            else:
                best_values[i][j].value = best_values[i - 1][j - memes[i - 1][1]].value + memes[i - 1][2]
                best_values[i][j].meme_set = best_values[i - 1][j - memes[i - 1][1]].meme_set.copy()
                best_values[i][j].meme_set.add(memes[i - 1][0])

    # return tuple of value and set of meme names for given usb stick size
    return best_values[len(memes)][usb_size].value, best_values[len(memes)][usb_size].meme_set
