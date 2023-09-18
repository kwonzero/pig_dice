def check_dice_num(target):
    num = 0
    while num < target:
        if dice() == 1:
            num = 0
            print('게임이 끝났습니다.')
check_dice_num(50)
