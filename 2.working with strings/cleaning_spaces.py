#white spaces
text = " enginnering ".strip()
print(text)
#removes unwanted spaces from string
# lstrip() removes spaces from left side of string
# rstrip() removes spaces from right side of string


text2 = "##VCGSCUD#######".strip("#")
print(text2)


text3 = "     engineering  "
print(len(text3))
print(len(text3.strip()))