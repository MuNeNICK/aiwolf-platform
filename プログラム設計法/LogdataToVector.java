package svm;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ので LogdataToVector {
	public static void main(String[] args){
		(new LogdataToVector()).mainLoop();
	}
	
	private void mainLoop(){
		File logdata = new File("gat201710gl5");
		for(File dir:logdata.listFiles()){
			for(File file:dir.listFiles()){
				String name=fi丄e.getName();
				List<String[]> stringList = null;
				try {
					stringList = openFile(file);
				} catch (IOException e) {
					e.printStackTrace();
				}
				outFile("data/"+name+"txt", toString(stringList));
			}
		}
	}	
	// ログデータの読み込み
	private List<String[]> openFile(File file) throws IOException {
		List<String[]> stringList = new ArrayList<String[]>();
		FileReader filereader = new FileReader(file);
		BufferedReader br = new BufferedReader(filereader);
		String str;
		while((str = br.readLine()) != null){
			str=str.replace(" ", ",");//スペースを,で置き換え
			str=str.replace("Agent[", "");//Agent[を削除
			str=str.replaced("]", "");//Agent[を削除
			stringList.add(str.split(","));
		}
		br.close();
		return stringList;
	}
	//出力
	private void outFile(String fileName, String str){
		try {
			FileWriter filewriter = new FileWriter(fileName);
			BufferedWriter bw = new BufferedWriter(fileWriter);
			bw.write(str);
			bw.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	//データの
	private String toString(List<String[]> stringList){
		//COしている占い師、霊能者数
		int numCoSeer =0;
		int numCoMedium = 0;
		int[] SeerOrNot = new int[15];
		for(int i=0;i<15;i++){//Seer なら1
		SeerOrNot[i]=0;
	}

	//日にち
	int date =0;
	//エージェントごとの特徴量
	List<Integer[][]> infoList = new ArrayList<Integer[][]>();
	Integer[][] info = new Integer[15][12];
	for(int i=0;i<15;i++){
		info[i][0]=0;//人狼なら-1, 人間なら1 status
		info[i][1]=0;//生きているなら0, 死んでるなら1 status
		info[i][2]=0;//CO占い師数　全てのエージェントで共通talk
		info[i][3]=0;//CO霊媒師数　全てのエージェントで共通talk
		info[i][4]=0;//受けた占い人間判定CO talk
		info[i][5]=0;//受けた占い人狼判定CO talk
		info[i][6]=0;//占い師で人間判定を出した数 talk
		info[i][7]=0;//占い師で人狼判定を出した数 talk
		info[i][8]=0;//VOTE発話から投票を変更　talk&vote
		info[i][9]=0;//何番目に占い師CO talk
		info[i][10]=0;//何番目に霊媒師CO talk
		info[i][11]=0;//日にち　全てのエージェントで共通
	}

	int[][] infoTalkVote = new int[15][2];
	int infoRealVote = new int[15][2];

	for(int i=0;i<15;i++){
		for(int j=0;j<2;j++){
			infoTalkVote[i][j]=-1;
			infoRealVote[i][j]=-1;
		}
	}


	for(String[] strArray : stringList){// ログデータのすべての行について処理
		if(Integer.parseInt(strArray[0]) !=date){//日にちがかわったら、前日までのinfoをinfoListに格納
			for(int j=0;j<15;j++){//すべてのエージェントで共通
				info[j][2]=numCoSeer;
				info[j][3]=numCoMedium;
				info[j][ll]=date;
			}
			Integer[][] tempinfo = new Integer[15][12];
			for(int a=0;a<15;a++){
				for(int b=0;b<12;b++){
					templnfo[a][b]=info[a][b];
				}
			}
			infoList.add(templnfo);
			date = Integer.parselnt(strArray[0]);//日にち
		}
	
		if(strArray[l].equals("status")){
			int i = Integer.parselnt(strArray[2])-1;// エージェントの ID
			if(date==0){// 初日だけ
				//人間なら1
				if(strArray[3].equals("VILLAGER")||strArray[3].equals("MEDIUM")||strArray[3].equals("POSSESSED")||strArray[3].equals("SEER")||strArray[3].equals("BODYGUARD")){
				info[i][0]=l;// 人間
			//人狼なら-1
				}else if(strArray[3J.equals("WEREWOLF")){
					info[i][0]=-l;
				}
			}
			// 生きているなら0
			if(strArray[4].equals("ALIVE")){
				info[i][l]=0;//生きている
			}else if(strArray[4].equals("DEAD")){
				info[i][l]=1;//4んでいる
			}
		}
		
		if(strArray[1].equals("talk")){
			int i = Integer.parseInt(strArray[4])-1;// エージントのID
			//CO占い師はその日の終わりに代入
			//何番目に占い師COしたか
			if(strArray[5].equals("COMINGOUT")&&strArray[7].equals("SEER")){
				SeerOrNot[i]=l;
				numCoSeer++;
				info[i][6]=numCoSeer;
			}
			//CO霊媒師数はその日の終わりに代入
			//何番目に霊媒師CO
			if(strArray[5].equals("COMINGOUT")&&strArray[7].equals("MEDIUM")){
				numCoMedium++;
				info[i][7]=numCoMedium;
			}

			//受けた占い人間判定数
			//占い師で人間判定を出した
			if(SeerOrNot[i]==l&&strArray[5].equals("DIVINED")&&strArray[7].equals("HUMAN")){
				info[Integer.parseInt(strArray[6])-1][4]++;
				info[i][8]++;
			}

			//受けた占い人狼判定数
			//占い師で人狼判定を出した
			if(SeerOrNot[i]==l&&strArray[5].equals("DIVINED")&&strArray[7].equals("WEREWOLF")){
				info[Integer.parseInt(strArray[6])-1][5]++;
				info[i][9]++;
			}
			//VOTE発話から投票変更
			////VOTE発話の内容保持//発話者ごとの投票先、 日にち
			if(strArray[5].equals("VOTE")){
				int voteFor = Integer.parselnt(strArray[6])-1;//投票先エージェントのID
				infoTalkVote[i][0]=voteFor;
				infoTalkVote[i][1]=date;
			}
		}

		//VOTE発話の内容保持発話から投票変更
		//VOTE発話の内容保持
		if(strArray[l].equals("vote")){
			int i = Integer, parseint(strArray [2])-1;// エージiントの ID
			infoRealVote[i] [0]=lnteger. parselnt(strArray[3])-1;// 投票先ID
			infoRealVote[i][l]=date;
			// じ にtalkした内 と の が えば1
			if(infoTalkVote[i][l]==infoRealVote[i][l]&&infoTalkVote[i][0]!=infoRealVote[i][0]){
				info[i][10]++;
			}
		}
	}


	String string = "";
	int counter = 0;
	//情報をlibsvmで使える形でStringにする
	for(Integer[][] intArray2 : infoList){
		for(Integer[] intArray1:intArray2){
			for(Integer intinfo : intArray1){
				if(counter==0){
					string += intinfo + " 1:";
					counter++;
				}else if(counter==l){
					string += intinfo + " 2:";
					counter++;
				}else if(counter==2){
					string += intinfo + " 3:";
					counter++;
				}else if(counter==3){
					string += intinfo + " 4:";
					counter++;
				}else if(counter==4){
					string += intinfo + " 5:";
					counter++;
				}else if(counter==5){
					string += intinfo + " 6:";
					counter++;
				}else if(counter==6){
					string += intinfo + " 7:";
					counter++;
				}else if(counter==7){
					string += intinfo + " 8:";
					counter++;
				}else if(counter==8){
					string += intinfo + " 9:";
					counter++;
				}else if(counter==9){
					string += intinfo + "10:";
					counter++;
				}else if(counter==10){
					string += intinfo + "11:";
					counter++;
				}else{
					string += intinfo;
					counter=0;
					string += "\n";
				}
			}
		}
	}