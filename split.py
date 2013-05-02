__author__ = 'haowu'

def genJSON():
    ins = open("data/parsed.txt","r")
    datas = [];
    for line in ins:
        datas.append(line.replace("{'USER_NAME': u","{'USER_NAME': "))
    ins.close()


    ins = open("data/json.txt","w")
    # datas = [];
    for line in datas:
        ins.write(line+ "\n")
    ins.close()

