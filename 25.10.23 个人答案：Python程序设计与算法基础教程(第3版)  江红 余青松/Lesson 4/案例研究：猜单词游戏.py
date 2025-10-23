import random
WORDS = ['apple','pear','banana','cherry','good','better','best','python','while','tuple','dictionary','jumble','difficult','aesthetic','stereotype','civilization','anniversary']
print("欢迎参加猜单词游戏!\n 请把乱序后的字母组成一个单词\n")
isContinue = "y"
while isContinue in ("Y", "y"):
    word = random.choice(WORDS)
    answer = word
    jumble = ""
    for i in word:
        #随机抽取一个位置的字符放入乱序jumble 中，并从原word 中删除该字符
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    print("乱序后的单词:" + jumble)
    guess = input("请输入您猜测的结果:")
    while guess != answer:
        guess = input("结果不对，请重新猜测:")
        print("恭喜您，猜对了!")
#询问是否重复游戏
    isContinue = input("是否继续(Y/N)?")
    if isContinue in ("Y", "y"):
        continue
    else:
        break
print("游戏结束，欢迎下次再来!")