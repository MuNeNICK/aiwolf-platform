import random
from asyncio.windows_events import NULL


class wolfWolf:
    
    def __init__(self):
        #ゲームのデータ管理をインスタンス変数にて行う
        #ゲームの日数
        self.dayCount = 0
        self.agentCount = 3
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
        self.wolfCount = 0
        self.humanCount = 0
        
        
    def initialize(self):
        #エージェントの初期化（死亡 = 0, 生存している人間 = 1, 生存している人狼 = 2, 追放 = 3）
        for x in range(1,self.agentCount+1):
            self.agentMembers[x] = 1
        
        #エージェント1~3の誰かに人狼を割り当て
        randomWolf = random.randint(1, self.agentCount)
        self.agentMembers[randomWolf] = 2
        
        
    def dayStart(self):
        #一日の開始宣言
        print(self.dayCount+"日目スタート")
    
    def dayEnd(self):
        #一日の終了
        print(self.dayCount+"一日目の終了")
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
        print("お昼")
    
    def nightPhase(self):
        #占い先の決定
        #人狼の釣り先決定
        #狩人の守り先決定
        print("夜")
    
    def inputVote(self, selfNumber):
        print("投票先一覧")
        
        for x in self.agentMembers:
            if x == selfNumber:
                continue
            print("エージェント"+x)            
        self.voteList.append(input("投票先エージェントを入力してください\nエージェント")) 

    def inputDevine(self, selfNumber):
        self.devineJudge = input("占いを実行しますか？\n実行する場合: 1\n実行しない場合0\nを入力してください\n")
        
        if self.devineJudge == 1:
            print("占い先一覧")
            for x in self.agentMembers:
                if x == selfNumber:
                    continue
                print("エージェント"+x)
            self.devinvoteResult.append(input("占い先エージェントを入力してください\nエージェント")) 

    def inputWhisper(self, selfNumber):
        print("噛み先一覧")
        for x in self.agentMembers:
            if x == selfNumber:
                continue
            print("エージェント"+x)
        self.whisperResult.append(input("噛み先エージェントを入力してください\nエージェント"))
    
    def inputGuard(self, selfNumber):
        print("守り先一覧")
        for x in self.agentMembers:
            if x == selfNumber:
                continue
            print("エージェント"+x)
        self.guardvoteResult.append(input("守り先エージェントを入力してください\nエージェント"))

    def devine(self):
        #占い結果を返す
        if self.devineJudge == 0:
            print("占いが行われませんでした")
            return
        print("占い実行")
        devineResult = self.agentRole[self.devinevoteResult[self.dayCount]]
        return devineResult
        
        
    def execute(self):
        print("追放実行")
        
        #追放
        #追放するエージェント
        executeAgent = self.voteResult[self.dayCount]
        self.agentMembers[executeAgent] = 2
        
        
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
    print("人狼同士の囁き:[")
    print("占い:>")
    wolf.nightPhase()
    
    wolf.dayStart()

    while True:
        #print("お昼だよー:o")
        #お昼のフェーズ
        wolf.dayPhase()
        
        #終了判定
        if wolf.finish() == 1:
            print("ゲーム終了")

        for _ in range(wolf.dayCount):
            wolf.inputVote()

        print("夜だよー:D")
        #夜のフェーズ
        wolf.nightPhase()
    
        
        
        #終了判定
        if wolf.finish() == 1:
            print("ゲーム終了")

