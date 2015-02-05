# coding:utf-8
import sys, os

print "------------------------------------"
print " * Siriとおしゃべりスクリプト *"
print "------------------------------------"
print ""
print "* Enter -> siriを呼ぶ"
print "* 入力"
print ""
print ""
def_msg = sys.argv[1]
os.system("say heysiri"+ def_msg)
while True:
    msg = raw_input('siriに話しかけよう! >')
    if msg == "":
        os.system("say heysiri")
    else:
        os.system("say " + msg)


