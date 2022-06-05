
class TestWolf:
    
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
        
    def initialize(self):
        #エージェントの初期化（生存 = 1, 死亡 = 0, 追放 = 2）
        for x in range(1,self.agentCount+1):
            self.agentMembers[x] = 1
            
        #占いの
        
    def dayStart(self):
        #一日の開始宣言
        print(self.dayCount+"日目スタート")
        
    def finish(self):
        #最終日の判定
        pass
        
    def dayPhase(self):
        #投票先の決定
        
        #エージェントを順番に呼び出す
        #エージェントは1人一回ずつ喋る（初日の場合は役職の宣言も）
        pass
    def nightPhase(self):
        #占い先の決定
        #人狼の釣り先決定
        #狩人の守り先決定
        pass
    
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
        if self.whisperResult[dayCount] != NULL:
        
    

if __name__ == "__main__":
    test = TestWolf()
    test.initialize()
    
    print("夜から始まるよ:]")
    print("人狼同士の囁き:[")
    print("占い:>")
    test.nightPhase()
    
    test.dayStart()

    while True:
        print("お昼だよー:o")
        #お昼のフェーズ
        test.dayPhase()
        '''
        for _ in range(50):
            print("お話するよ:3")   
            print("投票するよ")

        '''
        print("夜だよー:D")
        #夜のフェーズ
        test.nightPhase()
        
        #最終日判定
        test.finish()

