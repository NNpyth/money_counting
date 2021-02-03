import sys


def main(money=0):
    if not check_valid(money):
        print("正しい金額を入力してください。")
    else:
        print_result(money, *get_result(money))


def check_valid(money):
    return type(money) is int and money >= 0 and sys.maxsize > money


def print_result(money, mannsatu, gosenn, senn, gohyaku, hyaku, gojuu, juu, go, ichi):
    print(
        money,
        "円は一万円が",
        mannsatu,
        "枚と、五千円札が",
        gosenn,
        "枚と、千円札が",
        senn,
        "枚と、\n",
        "五百円玉が",
        gohyaku,
        "枚と、百円玉が",
        hyaku,
        "枚と、五十円玉が",
        gojuu,
        "枚と、\n",
        "十円玉が",
        juu,
        "枚と、五円玉が",
        go,
        "枚と、一円玉が",
        ichi,
        "枚です。",
    )


def get_result(money):
    (
        issennmann,
        hyakumann,
        juumann,
        ichimann,
        mannsatu,
        gosenn,
        senn,
        gohyaku,
        hyaku,
        gojuu,
        juu,
        go,
        ichi,
    ) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    while money >= 10000000:
        money = money - 10000000
        issennmann = issennmann + 1
    while money >= 1000000:
        money = money - 1000000
        hyakumann = hyakumann + 1
    while money >= 100000:
        money = money - 100000
        juumann = juumann + 1
    while money >= 10000:
        money = money - 10000
        ichimann = ichimann + 1
    if money >= 5000:
        money = money - 5000
        gosenn = 1
    else:
        gosenn = 0
    while money >= 1000:
        money = money - 1000
        senn = senn + 1
    if money >= 500:
        money = money - 500
        gohyaku = 1
    else:
        gohyaku = 0
    while money >= 100:
        money = money - 100
        hyaku = hyaku + 1
    if money >= 50:
        money = money - 50
        gojuu = 1
    else:
        gojuu = 0
    while money >= 10:
        money = money - 10
        juu = juu + 1
    if money >= 5:
        money = money - 5
        go = 1
    else:
        go = 0
    while money >= 1:
        money = money - 1
        ichi = ichi + 1
    mannsatu = issennmann * 1000 + hyakumann * 100 + juumann * 10 + ichimann
    return mannsatu, gosenn, senn, gohyaku, hyaku, gojuu, juu, go, ichi


# If you use this, use below and comment out 'main(12345678)'.
#
# if __name__ == "__main__":
# main(12345678)

# If you use jupyter notebook, use 'main(12345678)'.
#
main(11111111111111)
