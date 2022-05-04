import mmo

def addTime():
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
            catNames = ['Any%','Crouchless','Refresh%','Minimum Jumps','Test%']
            for x in range(len(catNames)):
                print(str(x+1) + ' ' + catNames[x])

        cat = ''
        while not cat in catNames:
            printCatNames()
            cat = input().lower()

        cat = catNames[cat]
        
        print(cat)
        return cat

    user = input('user: ')
    category = getCatName()
    if category == 'jumps':
        jumps = input('jumps: ')
    time = input('time: ')

    if category == 'jumps':
        mmo.addTime(category,user,time,jumps)
    else:
        mmo.addTime(category,user,time)

def delTime():
    pass

def viewLeaderboard():
    pass

def editCatInfo():
    pass

def editPost():
    pass

def runAction(action):

    def invalid():
        raise Exception('invalid action')

    actions = {
        '1': addTime,
        '2': delTime,
        '3': mmo.export,
        '4': viewLeaderboard,
        '5': editCatInfo,
        '6': editPost
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
        action = input('\n1 = add/update run\n2 = delete run\n3 = export\n\n4 = view leaderboard\n5 = edit category info\n6 = edit extra post text\n')
        runAction(action)


main()