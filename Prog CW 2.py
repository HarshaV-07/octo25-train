import random as ra
import pandas as ps

summary = []
def f_t():
    gd = ra.randint(1, 6)
    print('Shooter rolls the green dice')
    print('Shooter rolled', gd)
    
    blocks = 0  
    fouls = 0   
    
    if gd == 1 or gd == 2:
        print('Shooter made a clean shot')
        return ('Shooter scores', blocks, fouls)         
    
    elif gd == 3:
        print('Shooter missed the shot ')
        return ('Defender scores', blocks, fouls)
    
    else:
        print('The shot is in progress....')
        print('Defender is trying to block the shot')
        
    od = ra.randint(1, 6)
    print('Defender rolls orange dice')
    print('Defender rolled', od)
    
    if od == 1:
        print('Blocked by the defender')
        blocks += 1  
        return ('Defender scores', blocks, fouls) 
    elif od == 2:
        print('Foul drawn by the shooter')
        fouls += 1  
        return ('It\'s a Foul, shooter gets a free throws', blocks, fouls)
    else:
        print('Shooter is in pressure right now')
        pd = ra.randint(1, 6)
        print('Shooter rolls purple dice')
        print('Shooter rolled', pd)
        if pd == 1:
            print('Shooter made the basket')
            return ('Shooter scores', blocks, fouls)
        elif pd == 2:
            print('The ball is out of bounds')
            return ('Defender scores', blocks, fouls)
        else:
            f_t()
            return('Rebound fight', blocks, fouls)
            
def hoop_shot():
    s_s = 0
    d_s = 0
    s_fouls = 0   
    d_blocks = 0  
    while s_s < 5 and d_s < 5:
        if s_s == 4 and d_s == 4:
            print('The game is tied')
            print('The game is intense. Let\'s see who will win....')
            
        res, blocks, fouls = f_t()
        if res == 'Shooter scores':
            s_s+=1
            print('Shooter\'s score is ', s_s)
            print('Defender\'s score is', d_s)
            print('')
        elif res == 'Defender scores':
            d_s += 1
            d_blocks += blocks
            print('Shooter\'s score is ', s_s)
            print('Defender\'s score is', d_s)
            print('')  
        elif res == 'It\'s a Foul, shooter gets a free throws':
            s_s += 1
            s_fouls += fouls
            res, blocks, fouls = f_t()
            
    if s_s == 5:
        match=[]
        match = [s_s, d_s, d_blocks, s_fouls]
        print('SHOOTER WINS') 
        summary.append(match)
        print('')
    elif d_s == 5:
        match=[]
        match = [s_s, d_s, d_blocks, s_fouls]
        print('DEFENDER WINS')
        summary.append(match)
        print('')


for hoop in range(4):
    if hoop==0: #for early shooter lead
        s_s=3
        d_s=0
        hoop_shot()
    elif hoop==1: #for early defender lead
        s_s=0
        d_s=3
        hoop_shot()
    else:
        hoop_shot()

print(summary)
D = ps.DataFrame(columns=['S_Points', 'D_Points', 'Blocks', 'Fouls'])
for i in range(4):
    D.loc[i] = summary[i]
    
print(D)
