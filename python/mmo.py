from collections import OrderedDict, defaultdict


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


def sortCategory (category):
    if category == 'jumps':
        jumps = leaderboard['jumps']
        group = {}
        for run in jumps.items():
            if not run[1]['jumps'] in group:
                group[run[1]['jumps']] = {}
                
            group[run[1]['jumps']][run[0]] = run[1]
        
        for item in group.items():
            sortedGroup = sorted(item[1].items(),key=lambda x: x[1]['time'])
            group[item[0]] = OrderedDict(sortedGroup)

        group = sorted(group.items(),key=lambda x: x[0])
        
        result = {}

        for jumps in group:
            print(jumps[1])
            for run in jumps[1]:
                print(run)
                result[run] = jumps[1][run]
    else:
        sortedGroup = sorted(leaderboard[category].items(),key=lambda x: x[1]['time'])
        result = OrderedDict(sortedGroup)
    return result

def addTime(category,user,time,jumps=''):
    leaderboard[category][user] = {'time': time}
    if category == 'jumps':
        leaderboard[category][user]['jumps'] = jumps

    leaderboard[category] = sortCategory(category)

def delTime(category,user):
    del leaderboard[category][user]



def setup():
    f = open('mmo leaderboard.txt','r',encoding='utf8')
    post = f.read()
    f.close()
    getLeaderboards(post)


if __name__ == "__main__":
    f = open('mmo leaderboard.txt','r',encoding='utf8')
    post = f.read()
    f.close()

    print('\n1')
    print(post)

    print(getLeaderboards(post))

