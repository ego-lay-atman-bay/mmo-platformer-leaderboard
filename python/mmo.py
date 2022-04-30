categoryInfo = {}
leaderboard = {}

def getLeaderboards(txt):
    global categoryInfo, leaderboard

    def parseRun(run,cat):
        if cat == 'jumps':
            user = run.partition(']@')[2].partition('[/url]')[0]
            time = run.partition('). .')[2].partition(' by ')[0]
            jumps = run.partition('(')[2].partition(')')[0]
            result = {'user' : user, 'info' : {'time' : time, 'jumps' : jumps}}
        else:
            user = run.partition(']@')[2].partition('[/url]')[0]
            time = run.partition('. .')[2].partition(' by ')[0]
            result = {'user' : user, 'info' : {'time' : time}}

        return result
    
    def getCat(cat,txt):
        current = txt.partition(cat)[2]
        print('\ngetCat')
        print(current)
        info = '-' + current.partition('-')[2].partition('\n')[0]
        print(info)
        current = current.partition('[list=1]\n')[2]
        current = current.partition('\n[/list]')
        leaderboard = current[0].split('\n')
        current = current[2].partition('Category Rules[/b][/u]:\n')[2]
        rules = current.partition('\n[/quote]')[0]
        categoryInfo[cat] = [info,rules]
        return [leaderboard,current]

    

    txt = txt.partition('\n')[2]

    categories = [['Any%','any'],['Crouchless','crouchless'],['Refresh%','refresh'],['Minimum Jumps','jumps'],['Test%','test']]
    for i in categories:
        cat = getCat(i[0],txt)
        txt = cat[1]
        leaderboard[i[1]] = {}
        for run in cat[0]:
            runInfo = parseRun(run,i[1])
            leaderboard[i[1]][runInfo['user']] = runInfo['info']

    txt = txt.partition('[/quote]\n')[2]





if __name__ == "__main__":
    f = open('mmo leaderboard.txt','r',encoding='utf8')
    post = f.read()
    f.close()

    print('\n1')
    print(post)

    print(getLeaderboards(post))

