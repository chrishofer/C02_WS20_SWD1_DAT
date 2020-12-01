def verzinse(betrag, jahre = 1, zinsen = 10):
    print(f'{betrag}, {jahre}, {zinsen}')


if __name__ == '__main__':
    verzinse(1000)
    verzinse(1000,3)
    verzinse(1000, zinsen=4, jahre=10)
    verzinse(betrag=1000, zinsen=4, jahre=10)

    # was nicht geht
    #verzinse(betrag=1000, 4, 10)
    #verzinse(wert=1000)
    #verzinse(zinsen=4, jahre=10)