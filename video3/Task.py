# 1
msg = 'Denis Pitsul'

# 2
print(msg)

# 3-4
hello = "Hello"
print(hello + msg)
hello = hello + " "
print(hello)

# 5
msgList = msg.split()
msgList.insert(1, "Mykolayovych")
msg = ' '.join(msgList)
print(msg)

# 6
s = "colorless"
s = s[:4] + "u" + s[4:]
print(s)

# 7
wordsStr = "dish-es, run-ning, nation-ability, un-do, pre-heat"
wordsList = wordsStr.split(', ')
wordsStr = ""
for word in wordsList:
    afixIndex = word.find('-')
    word = word[:afixIndex]
    wordsStr += word + ", "
print(wordsStr)
