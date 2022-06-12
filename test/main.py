import random
#from asyncio.windows_events import NULL


class wolfWolf:
    
    def __init__(self):
        #ゲームのデータ管理をインスタンス変数にて行う
        #ゲームの日数
        self.dayCount = 0
        self.agentCount = 3
        self.voteList = []
        self.voteAgents = []
        self.voteResult = [] #インデックス = ゲームの日数
        self.agentMembers = [] #インデックス = エージェントの番号
        self.agentRole = [] #インデックス = エージェントの番号
        self.devinevoteResult = [] #インデックス = ゲームの日数
        self.devineResult = [] #インデックス = エージェントの番号
        self.wisperResult = [] #インデックス = 
        self.guardvoteResult = []
        self.devineResult = 0
        self.devineJudge = 0
        self.whisperResult = []
        self.wolfCount = 0 #人狼の数
        self.humanCount = 0 #人間の数
        self.openAgent = [] #公開されるエージェント
        self.executeAgent = 0 #追放されるエージェント
        self.wolfList = [] #人狼の一覧
        self.humanList = [] #人間の一覧
        self.devineList = [] #占い師の一覧
        
    def initialize(self):
        #エージェントの初期化（死亡 = 0, 生存している人間 = 1, 生存している人狼 = 2, 追放 = 3）
        for x in range(self.agentCount+1):
            self.agentMembers.append(1)
            self.humanList.append(1)
        for x in range(self.agentCount+1):
            self.agentMembers[x] = 1
            self.humanList[x] = 1
        
        #データ初期化
        for x in range(self.agentCount+1):
            self.voteAgents.append(0)
    
        for x in range(self.agentCount+1):
            self.openAgent.append(1)
        
        for x in range(self.agentCount+1):
            self.openAgent[x] = 1
        
        for x in range(self.agentCount+1):
            self.voteResult.append(1)
        
            
        #エージェント1~3の誰かに人狼を割り当て
        randomWolf = random.randint(1, self.agentCount)
        self.agentMembers[randomWolf] = 2
        self.wolfList.append(randomWolf)
        
        
    def dayStart(self):
        #一日の開始宣言
        print(str(self.dayCount)+"日目スタート")
    
    def dayEnd(self):
        #一日の終了
        print(str(self.dayCount)+"一日目の終了")
        self.dayCount += 1
        
    def finish(self):
        #ゲーム終了の判定
        
        #判定が1 = 人間勝利, 0 = 人狼勝利, 2 = 終了しない 
        finishJudge = 2
        
        for x in self.agentMembers:
            if x == 1:
                self.humanCount += 1
            elif x == 2:
                self.wolfCount += 1
            else:
                continue
        
        if self.humanCount <= self.wolfCount:
            finishJudge = 0
        elif self.wolfCount == 0:
            finishJudge = 1
        elif self.humanCount == 0:
            finishJudge = 0
        
        return finishJudge
        
                    
        '''
        finishJudge = 0
        finishwJudge = 1
        finishhJudge = 1
        for x in self.agentMembers:
            if x == 1:
                finishhJudge = 0
            elif x == 2:
                finishwJudge = 0
            else:
                continue
        
        if finishhJudge == 1:
            if finishwJudge == 0:
                finishJudge = 1
        
        if finishwJudge == 1:
            if finishhJudge == 0:
                finishJudge = 1
    
        if finishJudge == 1:
            print("")
        '''        
            
        
    def dayPhase(self):
        print(str(self.dayCount)+"日目の朝が来ました")
        
    
    def nightPhase(self):
        #占い先の決定
        #人狼の釣り先決定
        #狩人の守り先決定
        print("夜")
    
    def inputVote(self, selfNumber):
        print("投票先一覧")
        
        for x in range(1, self.agentCount+1):
            if x == selfNumber:
                continue
            print("エージェント"+str(x))            
        vote = int(input("投票先エージェントを入力してください\nエージェント"))
        self.voteList.append(vote) 

    def inputDevine(self, selfNumber):
        self.devineJudge = input("占いを実行しますか？\n実行する場合: 1\n実行しない場合0\nを入力してください\n")
        
        if self.devineJudge == 1:
            print("占い先一覧")
            for x in self.agentMembers:
                if x == selfNumber:
                    continue
                print("エージェント"+str(x))
            devine = int(input("占い先エージェントを入力してください\nエージェント"))
            self.devinevoteResult.append(devine) 

    def inputWhisper(self, selfNumber):
        print("噛み先一覧")
        for x in self.agentMembers:
            if x == selfNumber:
                continue
            print("エージェント"+str(x))
        wisper = int(input("噛み先エージェントを入力してください\nエージェント"))
        self.whisperResult.append(wisper)
    
    def inputGuard(self, selfNumber):
        print("守り先一覧")
        for x in self.agentMembers:
            if x == selfNumber:
                continue
            print("エージェント"+str(x))
        guard = input("守り先エージェントを入力してください\nエージェント")
        self.guardvoteResult.append(guard)

    def devine(self):
        #占い結果を返す
        if self.devineJudge == 0:
            print("占いが行われませんでした")
            return
        print("占い結果を表示します")
        devineResult = self.agentRole[self.devinevoteResult[self.dayCount]]
        
        print("プレイヤー"+str(self.devinevoteResult[self.dayCount])+"さんは"+str(devineResult)+"です")
        
        
        
    def execute(self):
        print("追放実行")
        
        #追放
        #追放するエージェント
        self.executeAgent = self.voteResult[self.dayCount]
        self.agentMembers[self.executeAgent] = 2
        
        
    def attack(self):
        print("噛み実行")
        
        ##噛み先
        attackAgent = self.whisperResult[self.dayCount]
        
        if attackAgent != None:
            if attackAgent != self.guardvoteResult[self.dayCount]:
                self.agentMembers[attackAgent] = 0         


if __name__ == "__main__":
    wolf = wolfWolf()
    wolf.initialize()
    
    print("夜から始まるよ:]")
    wolf.nightPhase()
    print("人狼同士の囁き:[")
    
    """
    print("占い:>")
    wolf.inputDevine(wolf.devineList[0])
    """
    
    wolf.dayEnd()
    
    wolf.dayStart()

    while True:
        #print("お昼だよー:o")
        #お昼のフェーズ
        wolf.dayPhase()
        
        #終了判定
        if wolf.finish() == 1:
            print("人間側の勝利")
            break
        elif wolf.finish() == 0:
            print("人狼の勝利")
            break
        
        #公表する役職の入力・発表
        if wolf.dayCount == 1:
            for x in range(1, wolf.agentCount+1):
                print("プレイヤー"+str(x)+"さんの番です")
                wolf.openAgent[x] = input("あなたが公表する役職を入力してください\n人間 = 1, 人狼 = 2\nあなたの本当の役職は"+str(wolf.agentMembers[x])+"です\n役職: ")
                print(wolf.openAgent[x])
            print("全員の役職の発表をします")
            for x in range(1, wolf.agentCount+1):
                print("プレイヤー"+str(x)+"さんの役職は"+str(wolf.openAgent[x])+"です")
        
        #占い結果発表
        wolf.devine()
        
        #投票
        for x in range(1, wolf.agentCount+1):
            wolf.inputVote(x)

        for x in wolf.voteList:
            wolf.voteAgents[x] += 1
        
        result = 0
        for x in range(1, wolf.agentCount+1):
            if wolf.voteAgents[x] > wolf.voteAgents[result]:
                result = x
        wolf.voteResult[wolf.dayCount] = wolf.voteAgents[result]

        
        print("夜だよー:D")
        #夜のフェーズ
        wolf.nightPhase()
        
        #エージェントの追放
        wolf.execute()
        
        """
        #占い先の入力
        wolf.inputDevine(wolf.devineList[0])
        """
        
        #人狼の噛み先入力
        wolf.inputWhisper(wolf.wolfList[0])
        
        """
        #狩人の守り先入力
        wolf.inputGuard(wolf.guardList[0])
        """
        
        #噛み実行
        wolf.attack()        
        

        
        
        #終了判定
        if wolf.finish() == 1:
            print("人間側の勝利")
            break
        elif wolf.finish() == 0:
            print("人狼の勝利")
            break

