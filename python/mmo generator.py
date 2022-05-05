import mmo

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
        cat = input().lower()
        if cat == '':
            return None

    cat = catNames[cat]
    
    print(cat)
    return cat

def addTime():
    print('\nenter nothing anytime to cancel')
    category = getCatName()
    if category == None:
        return
    user = input('user: ')
    if user == '':
        return


    while not user in mmo.leaderboard[category]:
        user = input('User not found. Maybe you used incorrect capitalization?')
        if user == '':
            return
    if category == 'jumps':
        jumps = input('jumps: ')
        if jumps == '':
            return
    time = input('time: ')
    if time == '':
        return

    if category == 'jumps':
        mmo.addTime(category,user,time,jumps)
    else:
        mmo.addTime(category,user,time)

def delTime():
    print('\nenter nothing anytime to cancel')
    category = getCatName()
    if category == None:
        return
    user = input('user: ')
    if user == '':
        return

    while not user in mmo.leaderboard[category]:
        user = input('User not found. Maybe you used incorrect capitalization?')
        if user == '':
            return

    if input('Are you sure you want to delete @'+user+"'s run " + str(mmo.leaderboard[category][user]) + ' (y/n):\n') == 'y' or 'yes':
        mmo.delTime(category,user)

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

def editCatInfo():
    print('\nenter nothing anytime to cancel')
    category = getCatName()
    if category == None:
        return
    

def editPost():
    pass

def export():
    filename = mmo.export()
    print('Post exported as ' + filename)

def runAction(action):

    def invalid():
        pass

    actions = {
        '1': addTime,
        '2': delTime,
        '3': export,
        '4': viewLeaderboard,
        '5': editCatInfo,
        '6': editPost,
        '7': exit
    }

    action_fun = actions.get(action, invalid)
    return action_fun()


def main():
    fileName = input('Enter path to post: ')

    f = open(fileName,'r',encoding='utf8')
    post = f.read()
    f.close()
    mmo.getLeaderboards(post)
    print('load successful')

    while True:
        action = input('\n1 = add/update run\n2 = delete run\n3 = export\n\n4 = view leaderboard\n5 = edit category info\n6 = edit extra post text\n\n7 = exit\n')
        runAction(action)


main()