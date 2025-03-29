import random

# コマ初期位置
pl1_pos = 1
pl2_pos = 1

# 盤面描写関数定義
def banmen():
    print("・" * (pl1_pos-1) + "P1" + "・" * (30 - pl1_pos) + "GOAL")
    print("・" * (pl2_pos-1) + "P2" + "・" * (30 - pl2_pos) + "GOAL")
    

#ゲームプログラム
print("START!!")

while True:
    # Player1
    input("Player1 Push Enter")
    pl1_pos = pl1_pos + random.randint(1,6)
    if pl1_pos > 30:
        pl1_pos = 30
    banmen()
    if pl1_pos == 30:
        print("Player1 Win!")
        break
    
    
    # Player2
    input("Player2 Push Enter")
    pl2_pos = pl2_pos + random.randint(1,6)
    if pl2_pos > 30:
        pl2_pos = 30
    banmen()
    if pl2_pos == 30:
        print("Player2 Win!")
        break
    

