#coding:gbk

quto ={'(':1, ')':-1}
dj = 0
exp = raw_input('>>')
for i in exp:
    if i in  quto:
       dj += quto[i]
    if dj < 0 :
        print "SHIT!!!!! ')' is more!!!!"
if not dj :
    print eval(exp)
elif dj > 0 :
    print "SHIT!!! '(' is more!!!!"
