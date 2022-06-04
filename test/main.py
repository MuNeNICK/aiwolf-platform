from test_agent import *

class TestWolf:

    
    def __init__(self):
        #ゲームのデータ管理をインスタンス変数にて行う
        #ゲームの日数
        self.dayCount = 0
    
    def initialize(self):
        pass
        
    def dayStart(self):
        #一日の開始宣言
        print(self.deyCount+"日目スタート")
        
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
        #噛み先決定
        pass



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

