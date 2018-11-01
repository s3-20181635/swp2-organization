import pickle

dbfilename = 'assignment3_20181631.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    for i in scdb:
        i['Age'],i['Score'] = int(i['Age']),int(i['Score'])
    return scdb
slack

# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name':parse[1], 'Age':int(parse[2]), 'Score':int(parse[3])}
                scdb += [record]
            except:
                print("잘못된 문자 형식입니다.")
                continue
            else:
                continue
        elif parse[0] == 'del':
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            break
        elif parse[0] == 'find':
            try:
                for i in scdb:
                    if i['Name'] == parse[1]:
                        print(i)
            except:
                print("잘못된 문자 형식입니다.")
                continue
            else:
                continue
        elif parse[0] == 'inc':

             for i in scdb:
                if i['Name'] == parse[1]:
                    i['Score'] = i['Score'] + int(parse[2])
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()
scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)