from collections import OrderedDict, defaultdict
from datetime import date


categoryInfo = {}
postInfo = []
leaderboard = {}
categories = {'any': 'Any%', 'crouchless': 'Crouchless', 'refresh': 'Refresh%', 'jumps': 'Minimum Jumps', 'test': 'Test%'}

def getLeaderboards(txt):
    global categoryInfo, leaderboard, postInfo

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
        #print('\ngetCat')
        #print(current)
        info = '-' + current.partition('-')[2].partition('\n')[0]
        #print(info)
        current = current.partition('[list=1]\n')[2]
        current = current.partition('\n[/list]')
        leaderboard = current[0].split('\n')
        current = current[2].partition('Category Rules[/b][/u]:\n')[2]
        rules = current.partition('\n[/quote]')[0]
        categoryInfo[cat] = [info,rules]
        return [leaderboard,current]

    
    txt = txt.partition('\n')[2]
    postInfo.append(txt.partition('\n[quote]')[0])

    categories = [['Any%','any'],['Crouchless','crouchless'],['Refresh%','refresh'],['Minimum Jumps','jumps'],['Test%','test']]
    for i in categories:
        cat = getCat(i[0],txt)
        txt = cat[1]
        leaderboard[i[1]] = {}
        for run in cat[0]:
            runInfo = parseRun(run,i[1])
            leaderboard[i[1]][runInfo['user']] = runInfo['info']

    txt = txt.partition('[/quote]\n')[2]
    postInfo.append(txt)


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
            for run in jumps[1]:
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

def export():
    def getLeaderboard(cat):
        board = leaderboard[cat]
        time = ''
        result = []
        for run in board.items():
            if run[1]['time'] == time:
                item = '. .'
            else:
                item = '[*]. .'
            
            if cat == 'jumps':
                item = item + '(' + run[1]['jumps'] + '). .'
            item = item + run[1]['time']
            item = item + ' by [url=https://scratch.mit.edu/users/' + run[0] + '/]@' + run[0] + '[/url]'
            result.append(item)
            time = run[1]['time']
        
        result = '\n'.join(result)
        #print('\n' + cat)
        #print(result)
        return result

    def getCatTxt(cat):
        info = [categories[cat],categoryInfo[categories[cat]]]
        result = '[quote]\n[big][b]' + info[0] + '[/b][/big] ' + info[1][0] + '\n[list=1]\n' + getLeaderboard(cat) + '\n[/list]\n[u][b]Category Rules[/b][/u]:\n' + info[1][1] + '\n[/quote]'
        #print(result)
        return result

    result = []
    for cat in ['any','crouchless','refresh','jumps','test']:
        leaderboard[cat] = sortCategory(cat)
        result.append(getCatTxt(cat))
    
    today = date.today()
    update = today.strftime("%B %d, %Y")

    result = '\n'.join(result)
    result = '[b][big]Hello all! . . . . (Last Update: ' + update +')[/big][/b]\n' + postInfo[0] + '\n' + result + '\n' + postInfo[1]
    
    f = open('mmo leaderboard ' + today.strftime("%m-%d-%y"),"w")
    f.write(result)
    f.close()
    
    return result

def setup():
    f = open('mmo leaderboard.txt','r',encoding='utf8')
    post = f.read()
    f.close()
    getLeaderboards(post)


if __name__ == "__main__":
    f = open('mmo leaderboard.txt','r',encoding='utf8')
    post = f.read()
    f.close()

    getLeaderboards(post)

