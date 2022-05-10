def washMachine(mode):
    print('吸水します')

    if mode == 'soft':
        print('やさしく洗う')
    elif mode == 'hard':
        print('激しく洗う')
    else:
        print('普通に洗う')

    print('すすぎます')
    print('脱水します')
    print('乾燥します')

washMachine('test')
