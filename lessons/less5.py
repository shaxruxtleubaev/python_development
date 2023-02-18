
'''
c
'''
def main(*say):
    for i in range(len(say)):
        word_len = len(say[i])
        word = say[i].count('0')
        start_word = say[i].lower().startswith('h')
        return f'Длина - {word_len} \
            букв о пов-я {word} \
                {start_word}'

if __name__ == '__main__':
    word_list = dict()
    for i in range(5):
        vol_1 = input('enter: ')
        word_list[i] = main(vol_1)
    print(word_list)






