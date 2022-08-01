package svm;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Villager extends Abstractvillager {
	@Override
	public void initialize(Gameinfo gameinfo, GameSetting gameSetting) {
		try {
		//学習したモデルの読み込み
		setModel():
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		latestGamelnfo = gameinfo;
		initDeadOrAlive();
	}

	@Override
	public void dayStart() {
		// TODO Auto-generated method stub
		// 特徴量の判別
		getlnfo();
		//対戦相手の判別
		if (latestGamelnfo.getDay() > 0) {
			try {
				setSVM();
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		// 各エージェントの生死の更新
		setDeadOrAlive();
		//初期化
		readTalkNum = 0;
		votingMap = new HashMapくAgent, Agent>();
		for (Agent agt :latestGamelnfo.getAliveAgentList()) {
			votingMap.put(agtnull);
		}
	}

	@Override
	public void update(GameInfo gameinfo) {
			//計測したい処理を記述
			latestGamelnfo = gameinfo;
		//今日の会話リストを取得
		ListくTalk> talkList =latestGameInfo.getTalkList();
		//votingMapの更新
		setVoteMap(talkList);
		//各エージェントのCOの更新
		setCO(talkList);
		//各CO占い師、霊媒師による人狼、　人間mapの更新
		setWolfHumanMap(talkList);
		//readTalkNum 0
		readTalkNum = talkList.size();
	}

	@Override
	public void finish() {
		// TODO Auto-generated method stub
	}

	@Override
	public String talk() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Agent vote() {
		// TODO Auto-generated method stub
		//Randomクラスのインスタンス
		Random rnd = new Random();
		Agent target=latestGameInfo.getAgentList().get(rnd.nextlnt(latestGamelnfo.getAgentList().size()));
		if(svmMap.isEmpty()){
			return target;
		}
		else{//svmMapみて人 判 のエージェントがいたら
			int blackID=0;
			for(Agent agt:svmMap.keyset()){
				if(svmMap.get(agt)>blackID){
					target=agt;
					blackID=svmMap.get(agt);
				}
			}
			return target;
		}
	}

	//変数
	//ゲー厶情報
	public Gameinfo latestGamelnfo;
	//エージェントごとの情報データ
	MapくAgent, Integer[]> infoMap = new HashMap<>();
	//ェージェントごとに-1(人狼)判定された回数を保存
	MapくAgent, Integer> svmMap = new HashMap<>();
	//投票予定map
	Map<Agent, Agent> votingMap;
	//カミングアウトしているエージェントのリスト
	Set<Agent> SeerCOAgent = new HashSet<Agent>();
	Set<Agent> MediumCOAgent = new HashSet<Agent>();
	//占い師COエージェントごとの人狼・人間判定
	Map<Agent, Set<Agent>> wolfAgentMap = new HashMap<Agent ,Set<Agent>>();
	Map<Agent, Set<Agent>> humanAgentMap = new HashMap<Agent ,Set<Agent>>();
	Map<Agent, Set<Agent>> wolfAgentMapByMedium = new HashMap<Agent ,Set<Agent>>();
	Map<Agent, Set<Agent>> humanAgentMapByMedium = new HashMap<Agent,Set<Agent>>();
	// い 、霊媒師COした

	Map<Agent, Integer> orderSeerCO = new HashMap<>();
	Map<Agent, Integer> orderMediumCO = new HashMap<>();
	//その のログの何 まで み んだか
	int readTalkNum;
	//svm のモデル
	svm_model model;
	//备エージェントの
	Map<Agent, Status> AliveOrDeadMap = new HashMap<Agent, Status>();
	// メソッド
	// の
	private void getlnfo() {
		if (latestGameInfo.getDay() > 0) {
			for (Agent agent :latestGameInfo.getAgentList()) {
				Integer[] info = new Integer[11];
				// 日にち
				info[10]=latestGamelnfo.getDay()-1;
				// 生きてるなら0、 4んでるなら1
				if (AliveOrDeadMap.get(agent) == Status.ALIVE) {
					info[0] = 0;
				} else {
					info[0]=1;
				}
				//CO占い師数
				info[1]=SeerCOAgent.size();
				//CO霊媒師数
				info[2] = MediumCOAgent.size();
				//人間と占われた
				info[3] = 0;
				//人狼と占われた
				info[4] = 0;
				for (Agent seer : SeerCOAgent) {
					if(humanAgentMap.get(seer).contains(agent)){
						info[3]++:
					}
					if(wolfAgentMap.get(seer).contains(agent)){
						info[3]++:
					}
				}
				//投票変更回数
				if (!latestGameInfo.getVoteList().isEmpty()) {
					if (AliveOrDeadMap.get(agent) == Status.ALIVE) {
						for (int i = 0; i < latestGamelnfo.getVoteList().size(); i++){
							if(latestGamelnfo.getVoteList().get(i).getAgent() == agent){

								if(latestGamelnfo.getVoteList().get(i).getTarget() != votingMap.get(agent)){
									info[9] = infoMap.get(agent)[9] + 1;
								}
							}

							else{
								info[9] = infoMap.get(agent)[9];
							}
						}
					}
				} else {
					info[9] = infoMap.get(agent)[9];
				}
				//占い師CO順
				info[5] = 0;
				//霊媒師CO順
				info[6] = 0;
				//人間判定数
				info[7] = 0;

				//人狼判定数
				info[8] = 0;
				if (SeerCOAgent.contains(agent)) {
					info[5] = orderSeerCO.get(agent);
					info[7] = humanAgentMap.get(agent).size();
					info[8] = wolfAgentMap.get(agent).size();
				}
				if (MediumCOAgent.contains(agent)) {
					info[6] = orderMediumCO.get(agent);
				}
				//infoMapを更新
				infoMap.put(agent, info);
			}
		}
	}

	//モデルのロード
	private void setModel()throws IOException {
		model=svm.svm_load_model("./lib/log.model");
	}

	//対戦相手の判別
	private void setSVM() throws Exception {
		for (Agent agt :latestGamelnfo.getAgentList()){
			int node =11;
			//判別対象にしたいデータ
			svm_node[] input = new svm_node[node];
			for (int i = 0; i < node; i++) {
				input[i] = new svm_node();
			}
			//ラベルをセット
			for (int i = 0; i < node; i++) {
				input[i].index = i + 1;
			}
			//値をセット
			for (int j = 0; j < node; j++) {
				input[j].value = infoMap.get(agt)[j];
				System, out. printIn("成功"+input[j] .value);
			}
			//判別の実行
			double v=0;
			try {
				v = svm.svm_predict(model, input);
			} catch (Exception e) {
				// TODO: handle exception
				System.out.println("判別エラー");
			}
			//人狼判定ならsvMapに追加
			if(v ==-1){
				Integer in = svmMap.get(agt);
				int i;
				if (in == null){
					i = 0;
				} else {
					i = in.intValue();
				}
				i++;
				in = Integer.valueOf(i);
				svmMap.put(agt, in);
			}
		}
	}
	//各エージェントの生死の初期化
	private void setDeadOrAlive(){
		Agent excutedAgent = latestGamelnfo.getExecutedAgent();
		if(getExecutedAgent != null){
			AliveOrDeadMap.put(excutedAgent, Status.DEAD);
		}
		List<Agent> deadAgentList = latestGamelnfo.getLastDeadAgentList();//修正

		for( Agent agt : deadAgentList ){
			AliveOrDeadMap.put(agt, Status.DEAD);
		}
	}
		}
	//C0の更新
	private void setCO(List<Talk> talkList) {
		//自分が きていれば
		if (latestGameInfo.getAliveAgentList().contains(
				latestGamelnf〇.getAgent())) {
			for (int i = readTalkNum; i < talkList.size(); i++) {
				Talk talk = talkList.get(i);
				// 発話をパース
				Content content = new Content(talk.getText());
				Agent subject = talk.getAgent();
				Agent target = content.getTarget();
				Role COrole = content.getRole();
				Set<Agent> wolf = new HashSetくAgent>();
				Set<Agent> human = new HashSetくAgent>();
				switch (content.getTopic()) {
				case COMINGOUT:
					// targetとsubjectが なっていたら、そのCOは がない
					if (target == subject) {
						switch (COrole) {
						case SEER:
							SeerCOAgent.add(target);
							wolfAgentMap.put(subject, wolf);
							humanAgentMap.put(subjecthuman);
							orderSeerCO.put(subjectj SeerCOAgent.size());
							break;
						case MEDIUM:
							MediumCOAgent.add(target);
							wolfAgentMapByMedium.put(subject, wolf);
							humanAgentMapByMedium.put(subject, human);
							orderMediumCO.put(subjectJ MediumCOAgent.size());
							break;
						}
					}
					break;
					// COしていなくても、 からCOと なせるときはCOと なす
					case DIVINED:
						SeerCOAgent.add(subject);
						humanAgentMap.put(subject, human);
						wolfAgentMap.put(subject, wolf);
						break;
					case content:
						MediumCOAgent.add(subject);
						wolfAgentMapByMedium.put(subject, wolf);
						wolfAgentMapByMedium.put(subject, wolf);
						humanAgentMapByMedium.put(subject, human);
						break;
					}
				}
			}
		}

		//判定結果の更新
		private void setWolfHumanMap(List<Talk> talkList) {{
			if (latestGamelnfo.getDay() > 0 && latestGamelnfo.getAliveAgentList().contains(
					latestGamelnfo.getAgent())) {
				for (int i = readTalkNum; i < talkList.size(); i++) {
					Talk talk = talkList.get(i);
					//発話をパース
					Content content = new Content(talk.getText());
					Agent subject = talk.getAgent();
					Agent target = content.getTarget();
					Species species = content.getResult();
					//占い結果
					if (content.getTopic() == Topic.DIVINED) {
						if (species == Species.WEREWOLF) {
							Set<Agent> wolfAgent = wolfAgentMap.get(subject);
							wolfAgent.add(target);
							wolfAgentMap.put(subjectwolfAgent);
						} else if (species == Species.HUMAN) {
							Set<Agent> humanAgent = humanAgentMap.get(subject);
							humanAgent.add(target);
							humanAgentMap.put(subject, humanAgent);

					}
				//霊媒結果
				} } else if (content.getTopic() == Topic.IDENTIFIED) {
					if (species == Species.WEREWOLF) {
						Set<Agent> wolfAgent = wolfAgentMapByMedium.get(subject);
						wolfAgent.add(target);
						wolfAgentMapByMedium.put(subject, wolfAgent);
					} else if (species == Species.HUMAN) {
						Set<Agent> humanAgent = humanAgentMapByMedium.get(subject);
						humanAgent.add(target);
						humanAgentMapByMedium.put(subjectj humanAgent);
					}
				}
			}
		}
	}
	//votingMap(投票予定先)の更新
	private void setVoteMap(ListくTalk> talkList) {
		if (latestGameInfo.getAliveAgentList().contains(
				latestGamelnfo.getAgent())) {
			for (int i = readTalkNum; i < talkList.size(); i++) {
				Talk talk = talkList.get(i);
				//発話をパース
				Content content = new Content(talk.getText());
				Agent subject = talk.getAgent();
				Agent target = content.getTarget();
				if (content.getTopic() == Topic.VOTE) {
				// vote が きていないなら ない
					if (latestGamelnfo.getAliveAgentList().contains(target)) {
						votingMap.put(subjecttarget);
					}
				}
			}
		}
	}