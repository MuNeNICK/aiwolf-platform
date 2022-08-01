import numpy as np
import random
log=[]
LOG=[]
a=[]

for i in range(3):
    a=input()
    a=a.split(",")
    LOG.append(a)
print(LOG)

#LOG=log.splitlines(",")
#log.splitlines(",")


"""

0,status,1,WEREWOLF,ALIVE,m_cre
0,status,2,VILLAGER,ALIVE,carlo
0,status,3,POSSESSED,ALIVE,AITKN

1,talk,0,0,9,COMINGOUT,9,MEDIUM
1,talk 1,0,4,VOTE,9
1,talk,2,0,8,VOTE,13

"""

def initList(list,value,sizeX,sizeY):# ぼくえらい！ちゃんとlist型の二次元配列の初期化関数つくってる！
    for i in range(sizeX):
        tmp=[]
        for j in range(sizeY):
            tmp.append(value)
        list.append(tmp)

def toString():
    numCoSeer=0
    numCoMedium=0
    SeerOrNot=[0]*15
    date=0
    infolist=[]
    info=[]
    initList(info,0,15,12)
    
    # info[i][0]=0#人狼:-1,人間:1
    # info[i][1]=0#live:0,dead:0
    # info[i][2]=0#num of CoSeer
    # info[i][3]=0#num of CoMedium
    # info[i][4]=0#num of being seered human
    # info[i][5]=0#num of being seered werewolf
    # info[i][6]=0#order of CoSeer
    # info[i][7]=0#order of CoMedium
    # info[i][8]=0#seer human
    # info[i][9]=0#seer werewolf
    # info[i][10]=0#talk and change vote
    # info[i][11]=0#date

    infoTalkVote=[]
    infoRealVote=[]
    initList(infoTalkVote,-1,15,2)
    initList(infoRealVote,-1,15,2)
    #date=-1
    for i in range(3):#ログすべてのデータを読み込む。後で書き換え
        str=[]
        str=LOG[i]
        if(int(str[0])!=date):#日付変わった後に
            for j in range(15):#すべてのエージェントで共通
                info[j][2]=numCoSeer
                info[j][3]=numCoMedium
                info[j][11]=date
            tempInfo=[[]]
            tempInfo=info
            tempInfo.append(tempInfo)
            date=str[0]
        if(str[1]=="status"):
            a =int(str[2])-1
            if(date==0):
                if(str[3]=="VILLAGER" or str[3]=="MEDIUM" or str[3]=="POSSESSED" or str[3]=="SEER" or str[3]=="BODYGUARD"):
                    info[a][0]=1
                elif(str[3]=="WEREWOLF"):
                    info[a][0]=-1
            if(str[4]=="ALIVE"):
                info[i][0]=0
            elif(str[4]=="DEAD"):
                info[i][1]=1
        if(str[1]=="talk"):
            a=int(str[4])-1

            if(str[5]=="COMINGOUT" and str[7]=="SEER"):
                SeerOrNot[a]=1
                numCoSeer+1
                info[a][6]=numCoSeer
            if(str[5]=="COMINGOUT" and str[7]=="MEDIUM"):
                numCoMedium+1
                info[a][7]=numCoMedium
            if(SeerOrNot[a]==1 and str[5]=="DIVINED" and str[7]=="HUMAN"):
                info[str[6]-1][4]+1
                info[a][8]+1
            
            if(SeerOrNot[a]==1 and str[5]=="DIVINED" and str[7]=="WEREWOLF"):
                info[str[6]-1][5]+1
                info[a][9]+1
            if(str[5]=="VOTE"):
                voteFor=int(str[6])-1
                infoTalkVote[a][0]=voteFor
                infoTalkVote[a][1]=int(date)
            
        if(str[1]=="vote"):
            a=int(str[2])-1
            infoRealVote[a][0]=str[3]-1
            infoRealVote[a][1]=date
            if(infoTalkVote[a][1]==infoRealVote[a][1] and infoTalkVote[a][0]!=infoRealVote[a][0]):
                info[a][10]+1
    print(info)
    print(infoTalkVote)
            

toString()
