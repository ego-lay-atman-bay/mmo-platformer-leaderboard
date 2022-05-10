import os
import mmo
from datetime import datetime as date
import tkinter as tk
from tkinter import filedialog
from tkinter import *

def ask(txt=''):
    result = input(txt)
    if result == '':
        return None
    return result

def userInCat(user,category):
    lowUser = user.lower()
    result = user
    for run in mmo.leaderboard[category].items():
        if run[0] == user:
            result = user
            break
        elif run[0].lower() == lowUser:
            confirm = input('Did you mean "' + run[0] + '"? (y/n): ')
            if confirm == 'y' or confirm == 'yes':
                result = run[0]
                break

    return result

def getCatName():
    catNames = {
        'any%':'any',
        'any':'any',
        '1':'any',
        'crouchless':'crouchless',
        'crouch':'crouchless',
        '2':'crouchless',
        'refresh%':'refresh',
        'refresh':'refresh',
        '3':'refresh',
        'minimum jumps':'jumps',
        'min':'jumps',
        'min jumps':'jumps',
        'min jump':'jumps',
        'jumps':'jumps',
        'jump':'jumps',
        '4':'jumps',
        'test%':'test',
        'test':'test',
        '5':'test'
    }

    def printCatNames():
        print('\nChoose category')
        catNames = ['Any%','Crouchless','Refresh%','Minimum Jumps','Test%']
        for x in range(len(catNames)):
            print(str(x+1) + ' ' + catNames[x])

    cat = ''
    while not cat in catNames:
        printCatNames()
        cat = ask()
        if cat == None:
            return
        else:
            cat = cat.lower()

    cat = catNames[cat]
    
    print(cat)
    return cat

def addTime():
    print('\nenter nothing anytime to cancel')
    category = getCatName()
    if category == None:
        return
    user = ask('user: ')
    if user == None:
        return
    user = userInCat(user,category)
    if user == None:
        return
    if category == 'jumps':
        jumps = ask('jumps: ')
        if jumps == None:
            return
    time = ask('time: ')
    if time == None:
        return

    if category == 'jumps':
        mmo.addTime(category,user,time,jumps)
    else:
        mmo.addTime(category,user,time)

    backup()

def delTime():
    print('\nenter nothing anytime to cancel')
    category = getCatName()
    if category == None:
        return
    user = ask('user: ')
    if user == None:
        return
    user = userInCat(user,category)
    if user == None:
        return

    while not user in mmo.leaderboard[category]:
        user = ask('User not found. Maybe you used incorrect capitalization? ')
        if user == None:
            return
        user = userInCat(user,category)
        if user == None:
            return
        

    if input('Are you sure you want to delete @'+user+"'s run " + str(mmo.leaderboard[category][user]) + ' (y/n):\n') == 'y' or 'yes':
        mmo.delTime(category,user)
        backup()

def viewLeaderboard():
    print('\nenter nothing anytime to cancel')
    category = getCatName()
    if category == None:
        return

    for run in mmo.leaderboard[category].items():
        txt = run[1]['time']
        if category == 'jumps':
            txt += ' (' + run[1]['jumps'] + ')'
        txt += ' by ' + run[0]
        print(txt)

    n = input()

def export():
    txt = mmo.export()
    today = date.today()
    filename = 'mmo leaderboard ' + today.strftime("%m-%d-%y") + '.txt'

    root = tk.Tk()
    root.withdraw()

    path = filedialog.asksaveasfilename(initialfile=filename, title = "Save post as",filetypes = (("text files","*.txt"),("all files","*.*")))
    print(path)

    f = open(path, 'w+', encoding='utf8')
    f.write(txt)
    f.close()
    
    log('export successful')

# def createError():
#     raise 'this is an error'

def runAction(action):

    def invalid():
        pass

    actions = {
        '1': addTime,
        '2': delTime,
        '3': export,
        '4': viewLeaderboard,
        '5': exit
    }

    action_fun = actions.get(action, invalid)
    return action_fun()

def log(log):
    root = os.getcwd()
    try:
        os.mkdir(root + '/data')
    except:
        pass

    data = root + '/data'
    
    now = date.now()

    epath = data + '/log.txt'
    ef = open(epath, 'a', encoding='utf8')
    line = [now.strftime("%H:%M:%S %m-%d-%y: ") + str(log) + '\n']
    ef.writelines(line)
    ef.close()

def backup():
    root = os.getcwd()

    try:
        os.mkdir(root + '/data')
    except:
        pass

    data = root + '/data'

    path = data + '/backup.txt'
    f = open(path, 'w', encoding='utf8')
    contents = mmo.export()
    f.write(contents)
    f.close()

    log('created backup')



def main():
    # fileName = input('Enter path to post: ')

    root = tk.Tk()
    root.withdraw()

    fileName = filedialog.askopenfilename(title='Open post')

    f = open(fileName,'r',encoding='utf8')
    post = f.read()
    f.close()
    mmo.getLeaderboards(post)
    print('load successful')
    log('load successful')

    while True:
        action = input('\n1 = add/update run\n2 = delete run\n3 = export\n\n4 = view leaderboard\n5 = exit\n')
        runAction(action)

try:
    main()
except Exception as error:
    backup()

    log('error: ' + str(error))