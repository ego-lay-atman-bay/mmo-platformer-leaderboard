categoryInfo = {}
leaderboard = {}

def getLeaderboards(txt):
    global categoryInfo, leaderboard

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

    def parseRun(run,cat):
        if cat == 'jumps':
            result = [run.partition('). .')[2].partition(' by ')[0],run.partition(']@')[2].partition('[/url]')[0]]
            result.append(run.partition('(')[2].partition(')')[0])
        else:
            result = [run.partition('. .')[2].partition(' by ')[0],run.partition(']@')[2].partition('[/url]')[0]]

        return result

    txt = txt.partition('\n')[2]

    categories = [['Any%','any'],['Crouchless','crouchless'],['Refresh%','refresh'],['Minimum Jumps','jumps'],['Test%','test']]
    for i in categories:
        cat = getCat(i[0],txt)
        leaderboard[i[1]] = cat[0]
        txt = cat[1]


    txt = txt.partition('[/quote]\n')[2]
    

    for cat in leaderboard:
        for i in range(len(leaderboard[cat])):
            leaderboard[cat][i] = parseRun(leaderboard[cat][i],cat)



if __name__ == "__main__":
    f = open('mmo leaderboard.txt','r',encoding='utf8')
    post = f.read()

    print('\n1')
    print(post)

    print(getLeaderboards(post))

    f.close()
