# Atcoder
___
## 夏休みAtcoder頑張るための日記  
virtual contest でといた問題を記録していきます


training1 ~  training3

time : 1hours  
difficulty  
1. 10~100
2. 100~400
3. 400~800
4. 800~1200
5. 1000~1200

Exclude experimental difficulty  

___
### 2021/08/15
- training1
  1. ソートして比較
  2. 途中でループに入るのでそこの判定気を付ける
  3. 二部探索や三部探索を考えたが見当違い、難しく考えすぎた。  
  周期性と右の項が単調増加していることに気づくとすぐ解けた  
  4. さっぱりだった。DPで部分和問題として解くらしい
  5. modを利用するのはわかったがうまく実装できなかった。


___
### 2021/08/16

- training2
  1. 全探索するだけ
  2. 同じく
  3. 工夫して全探索
  4. aで全探索するのかと思ってつまった。  
  O(N^2)ではTLEなので固定した全探索の典型
  もう片方も試すようにする。また、あまりなので周期性があることをすぐ気づくべき
  5. 偶数と奇数で分けるらしい。  
  排他的論理和の特徴を知ってたらいける  
  XORでは足し算も引き算も一緒  
  つまり0,1,..,A-1と0,...,Bまでの差はf(A-1) xor f(B)で答えが出る

- training3
  1. 和集合
  2. i%w==0を条件分岐
  3. 問題文読み間違えて何回かwaしてしまった。落ち着いて読む
  4. bit全探索
  5. 

___


training4 ~  training18

time : 1hours  
difficulty  
1. 100~400
2. 400~800
3. 800~1000
4. 1000~1200

Exclude experimental difficulty  

___

- training4
  1. sortするだけ、余った分は一人の子に集めればよい
  2. 二つ目のボール以降はK-1通り
  3. 制約から全探索を推測する、問題文の理解ができていなかった。  
  また、文字列区間を考えるときはランレングス圧縮も頭の隅に置いておくべき   
  もちろん、探索範囲が狭いのでランレングスなしでも十分間に合う
  4. Bを固定して全探索


- training5
  1. combinationsを使って傾きが等しいものがあるか確かめるだけ
  2. a1を決め打ちして条件に満たす数があるかループしてもとめた  
  a1+a2+a3+b1+b2+b3のペアを三つ作るとif文だけで実装できたらしい。
  3. 問題が意味わからなかった。  
  解説を見てわかったがこういう問題は図を描きながら考えると思いつきやすそう。  
  4. bit全探索、考察も完璧だった。  
  ただしょうもないミスして時間切れ...すごく悔しい
  

___
### 2021/08/17

- training6
  1. [C - Neq Min](https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_c)  
  解法はあっていたがsetやpopを使ったことによりおそらくどこかで  
  ずれた可能性あり　シンプルにlistなどで実装したほうがよかった
  2. [C - Many Medians](https://atcoder.jp/contests/abc094/tasks/arc095_a)  
  中央値を二つあらかじめ求めておく
  3. [D - 2017-like Number](https://atcoder.jp/contests/abc084/tasks/abc084_d)  
  解法ではすべての素数をさきにlistで作っていた。  
  return をうまくつかっても高速でできた
  4. [D - Christmas](https://atcoder.jp/contests/abc115/tasks/abc115_d)  
  時間なかった。制約が小さいことから再帰でやるらしい


- training7
  1. [B - Minesweeper](https://atcoder.jp/contests/abc075/tasks/abc075_b)  
  実装に13分とられた、もう少し早くミスのないコードを書くべき
  2. [D - Gathering Children](https://atcoder.jp/contests/abc136/tasks/abc136_d)  
  RLの部分を探してLとRが偶数回目で何個集まるか計算  
  ランレングス使ってS[i]=="L"でもっと簡単にできてた  
  DPでもいけるみたい
  3. [C - Digits in Multiplication](https://atcoder.jp/contests/abc057/tasks/abc057_c)  
  約数を√nのループで高速列挙するだけ
  4. [D - Coloring Dominoes](https://atcoder.jp/contests/arc081/tasks/arc081_b)  
  考察は悪くなかった。縦と横の通り数を同じと仮定したのがミス
  縦横、縦縦、横縦（横の時点で色が決まるので何もしないが）、横横の四つに場合分けして考える


- training8
  1. [B - 美しい文字列](https://atcoder.jp/contests/abc044/tasks/abc044_b)  
  Counter使って要素の個数を見る
  2. [B - Values](https://atcoder.jp/contests/arc106/tasks/arc106_b)  
  bfsで実装しようとしたけどうまくいかなかった。  
  aとbの総和に着目するらしい 、この仮定があると誤差を順番に直すうちに全体がそろう  
  **また、連結成分の判定なのでUnionFindをつかう**  
  まとめると、連結部分を判定してその総和がa==bとなるか確認する  
  3. [A - 01 Matrix ](https://atcoder.jp/contests/agc038/tasks/agc038_a)  
  左上と右下に0を固定して線を引くだけ。複雑な行列は想定しなくてよい
  4. [D - Card Eater](https://atcoder.jp/contests/arc068/tasks/arc068_b)  
  数日前にやった  
  種類が奇数個か偶数個かで場合分け、偶数の場合は一枚余分に減る



- training9
  1. [C - Divide the Problems](https://atcoder.jp/contests/abc132/tasks/abc132_c)  
  sortして二つの中央値の差
  2. [D - Water Bottle](https://atcoder.jp/contests/abc144/tasks/abc144_d)  
  三分探索しようとしたが二部探索でいいみたい
  数学的な解き方は傾けた時に底が見えるか見えないかで場合分け
  3. [E - Double Factorial](https://atcoder.jp/contests/abc148/tasks/abc148_e)  
  自分は10の数に着目したが、2と5に着目するのが正解  
  min(2,5)で0の数がわかる、また5のほうが小さいことは直感でわかるので5^xで割っていけばよい
  4. [C - 民族大移動](https://atcoder.jp/contests/abc024/tasks/abc024_c)  
  貪欲





___
### 2021/08/18

- training10
  1. [A - Fairness](https://atcoder.jp/contests/agc024/tasks/agc024_a)  
  前にやった、ループ処理に注意
  2. [C - Good Sequence](https://atcoder.jp/contests/abc082/tasks/arc087_a)  
  Counterつかって終わり
  3. [D - Disjoint Set of Common Divisors](https://atcoder.jp/contests/abc142/tasks/abc142_d)  
  自分は二つの公約数を求めてその中に素数がいくつあるか判定した  
  解法では最大公約数を先に求めてそれを素因数分解してた  
  **公約数は最大公約数の約数**
  4. [D - Blue and Red Balls](https://atcoder.jp/contests/abc132/tasks/abc132_d)  
  重複組み合わせ、仕切りのイメージ  
  pythonだとfactoricalが大きくなりすぎるので自分で配列を用意して計算する必要あり



- training11
  1. [A - Arithmetic Sequence](https://atcoder.jp/contests/arc123/tasks/arc123_a)  
  第一項と第三項の和が奇数かみる  
  あとはA2が(A1+A3)//2より大きいか小さいか
  2. [B - Values](https://atcoder.jp/contests/arc106/tasks/arc106_b)  
  まえやった、unionfind
  3. [C - String Invasion](https://atcoder.jp/contests/arc113/tasks/arc113_c)  
  後ろから確認してランレングス  
  dictでどの単語が何個あるのか記録するのがポイント
  4. [D - Blue and Red Balls](https://atcoder.jp/contests/abc132/tasks/abc132_d)  
  ビット全探索


- training12
  1. [B - Collatz Problem](https://atcoder.jp/contests/abc116/tasks/abc116_b)  
  よくわからないWAがでた、コーナーケース？  
  とにかく提出前に10秒でもいいから落ち着くようにする。
  2. [A - Two Choices ](https://atcoder.jp/contests/arc115/tasks/arc115_a)  
  思いつかなかったの超悔しい  
  奇数と偶数は必ず答えが異なるから掛け算で何通りかでる
  3. [D - Sum of Large Numbers ](https://atcoder.jp/contests/abc163/tasks/abc163_d)  
  大きい数字がくっつく場合、  
  **選んだ個数が異なるとき、和が等しくなることはない**  
  あとはk個選んだ時の最小値と最大値を記録しながら足していく
  4. よくわからんコンテストのやつだったのでパス



___
### 2021/08/19


- training13
  1. [C - Build Stairs](https://atcoder.jp/contests/abc136/tasks/abc136_c)  
  場合分け
  2. [A - Shik and Stone](https://atcoder.jp/contests/agc007/tasks/agc007_a)  
  #マスがH+W−1個か調べるだけ  
  通った道を記録する一筆書きのようなdfsを実装した、これはオーバーキル
  3. [D - aab aba baa](https://atcoder.jp/contests/abc202/tasks/abc202_d)  
  考察は悪くなかった。イメージは何回も半分に分けながら先頭がaかbか見る  
  この問題ではaが最初に来ると仮定したうえで組み合わせが何通りか計算する。
  4. [A - Shik and Stone](https://atcoder.jp/contests/agc007/tasks/agc007_a)  
  簡単なテストケースで考える  
  A B  
  C D  
  のとき高橋君から先に選ぶと A-D>C-Bとなる  
  変形するとA+B>C+Dとなるので直感的に和をsortしたらよいと気づく



- training14
  1. [C - Build Stairs](https://atcoder.jp/contests/abc136/tasks/abc136_c)  
  場合分け
  2. [A - Shik and Stone](https://atcoder.jp/contests/agc007/tasks/agc007_a)  
  #マスがH+W−1個か調べるだけ  
  通った道を記録する一筆書きのようなdfsを実装した、これはオーバーキル
  3. [D - aab aba baa](https://atcoder.jp/contests/abc202/tasks/abc202_d)  
  考察は悪くなかった。イメージは何回も半分に分けながら先頭がaかbか見る  
  この問題ではaが最初に来ると仮定したうえで組み合わせが何通りか計算する。
  4. [E - Akari](https://atcoder.jp/contests/abc182/tasks/abc182_e)  
  愚直に光が届いてるか調べたらO(HW)  
  ただうまく実装できていない.......


- training15
  1. [A - Remove Substrings](https://atcoder.jp/contests/agc054/tasks/agc054_a)  
  場合分け、
  2. [C - 4-adjacent](https://atcoder.jp/contests/arc080/tasks/arc080_a)  
  N-1の幅で考えた。その中で4で割り切れるものと2が2つで4の倍数になる可能性があるものの2パターン考えた
  3. [C - String Invasion](https://atcoder.jp/contests/arc113/tasks/arc113_c)  
  まえやった
  4. [A - Shik and Stone](https://atcoder.jp/contests/agc007/tasks/agc007_a)  
  ダイクストラはO(NlogN)でできるらしい  
  ポイントは最短距離を時間にするのだが、与えられたT,Kを使って1つの式を作れるか



___
### 2021/08/20


- training16
  1. [B - Making Triangle](https://atcoder.jp/contests/abc175/tasks/abc175_b)  
  combinations
  2. [A - Shik and Stone](https://atcoder.jp/contests/agc008/tasks/agc008_a)  
  ややこしい場合分け、だが実際は４パターン  
  3. [B - Special Subsets](https://atcoder.jp/contests/arc114/tasks/arc114_b)  
  fanctional graph  
  すごく面白い問題だった  
  関数をグラフとしてみるらしい、へー
  4. [C - Pyramid](https://atcoder.jp/contests/abc112/tasks/abc112_c)  
  ~~高さを一つ目のデータから決め打ちするのはダメだった~~  
  ~~おそらくmaxがほかのデータで決め打ちすると変わるため~~  
  そんなことなかった、max(h,0)のように書き換えるべきだった  
  for文でhを探索しても範囲が狭いので十分間に合う  




___
### 2021/08/21


- training17
  1. [D - ModSum](https://atcoder.jp/contests/abc139/tasks/abc139_d)  
  1つずらすのがあまりの最大化
  2. [C - Product and GCD](https://atcoder.jp/contests/caddi2018/tasks/caddi2018_a)  
  素因数分解してその要素がN個以上あるか(cnt//N)
  3. [C - Tsundoku](https://atcoder.jp/contests/abc172/tasks/abc172_c)  
  いろんな解法がありそう...  
  自分はN(Aの要素)をfor文で回し累積和のBについて残りの時間で  
  二部探索したときに何冊の部分に入るか確かめた
  4. [E - Peddler](https://atcoder.jp/contests/abc188/tasks/abc188_e)  
  面白い....!!!  
  スタートが特に決まってないので安く買える町をスタートとして  
  bfsを何度もする  
  計算量を減らすため訪れたことのある町はスキップ



___


training18 ~ 23

time : 1hours  
difficulty  
1. 100~400
2. 100~400
3. 400~800
4. 400~800
5. 800~1200
6. 800~1200


Exclude experimental difficulty  




___
### 2021/08/23


- training18
  1. [B - Tax Rate](https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b)  
  全探索でXを探す
  2. [B - Guidebook](https://atcoder.jp/contests/abc128/tasks/abc128_b) 
  自分は辞書型に入れてそれぞれsortした  
  二次元配列でsortしたらまとめてsortできるので二つ目の要素を-かけることで  
  昇順に並べられた 
  3. [B - KEYENCE String](https://atcoder.jp/contests/keyence2019/tasks/keyence2019_b)  
  最初と最後を全探索して調べる  
  4. [B - Many Oranges ](https://atcoder.jp/contests/abc195/tasks/abc195_b)    
  AN<=W*1000<=BNをつかってNを全探索  
  5. [B - Two Arrays ](https://atcoder.jp/contests/apc001/tasks/apc001_b)  
  二つの数列を一致させるときは和に着目  
  すべての index について a[i]<=b[i] という状態になれば "Yes"  
  4. [C - GCD on Blackboard](https://atcoder.jp/contests/abc125/tasks/abc125_c)  
  累積 GCD



___
### 2021/08/24


- training19
  1. [C - XYZ Triplets](https://atcoder.jp/contests/aising2020/tasks/aising2020_c)  
  x,y,zを√nの範囲で全探索
  2. [B - ATCoder](https://atcoder.jp/contests/abc122/tasks/abc122_b) 
  範囲が狭いので1文字ずつ調べて数え上げる
  3. [D - Megalomania](https://atcoder.jp/contests/abc131/tasks/abc131_d)  
  Bを基準にsortしてforで回す 
  4. [C - HSI](https://atcoder.jp/contests/abc078/tasks/arc085_a)    
  幾何分布　期待値は1/p  
  1回の施行にかかるms * 1/pで終わり  
  5. [D - Powerful Discount Tickets](https://atcoder.jp/contests/abc141/tasks/abc141_d)  
  -1をかけて優先度付きキュー
  6. [C - Special Trains](https://atcoder.jp/contests/abc084/tasks/abc084_c)  
  実装ゲーだったみたい(自分はしてない)  
  貪欲にやるかんじ


- training20
  1. [A - Hands](https://atcoder.jp/contests/arc109/tasks/arc109_a)  
  場合分けに時間とられすぎた...
  2. [B - Contest with Drinks Easy](https://atcoder.jp/contests/abc050/tasks/abc050_b)  
  最初に和を求めておく
  3. [B - Quadruple](https://atcoder.jp/contests/arc107/tasks/arc107_b)  
  半分全列挙、というらしい。  
  4. [C - Ubiquity](https://atcoder.jp/contests/abc178/tasks/abc178_c)      
  集合論  
  9が存在しない集合と0が存在しない集合の和集合を考え、その余事象を求める 
  5. [D - Powerful Discount Tickets](https://atcoder.jp/contests/agc016/tasks/agc016_a)  
  前にやった
  6. [A - Simple Math 2](https://atcoder.jp/contests/arc111/tasks/arc111_a)  
  10^NからM^2の倍数を引いても答えは変わらない




___
### 2021/08/25

- training21
  1. [B - Not Found ](https://atcoder.jp/contests/abc071/tasks/abc071_b)   
  setで入ってるか確認
  2. [B - Mex Boxes](https://atcoder.jp/contests/keyence2021/tasks/keyence2021_b)  
  配列を用意してそれぞれの数字をカウントする  
  Kよリ小さくなったときにKとansの更新をする
  3. [B - RGB Boxes](https://atcoder.jp/contests/diverta2019/tasks/diverta2019_b)  
  r,gを決め打ちしてbが存在するときにans+=1する
  4. [A - Divide a Cuboid](https://atcoder.jp/contests/agc004/tasks/agc004_a)    
  A,B,Cそれぞれを基準にして計算し、それらの最小値を求める  
  5. [B - fLIP](https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_b)  
  黒く塗られるマスは左上と右下に集められるので  
  x*y+(M-x)*(N-y)としxとyを全探索する O(NM)
  6. [C - String Transformation ](https://atcoder.jp/contests/abc110/tasks/abc110_c)  
  Counterで数えるだけ


___
### 2021/08/25

- training22
  1. [B - Not Found ](https://atcoder.jp/contests/abc071/tasks/abc071_b)   
  setで入ってるか確認
  2. [B - Mex Boxes](https://atcoder.jp/contests/keyence2021/tasks/keyence2021_b)  
  配列を用意してそれぞれの数字をカウントする  
  Kよリ小さくなったときにKとansの更新をする
  3. [B - RGB Boxes](https://atcoder.jp/contests/diverta2019/tasks/diverta2019_b)  
  r,gを決め打ちしてbが存在するときにans+=1する
  4. [A - Divide a Cuboid](https://atcoder.jp/contests/agc004/tasks/agc004_a)    
  A,B,Cそれぞれを基準にして計算し、それらの最小値を求める  
  5. [B - fLIP](https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_b)  
  黒く塗られるマスは左上と右下に集められるので  
  x*y+(M-x)*(N-y)としxとyを全探索する O(NM)
  6. [C - String Transformation ](https://atcoder.jp/contests/abc110/tasks/abc110_c)  
  Counterで数えるだけ




___
### 2021/08/26

- training23
  1. [A - Number of Multiples](https://atcoder.jp/contests/aising2020/tasks/aising2020_a)  
  LからRまで全探索
  2. [A - Two Sequences 2](https://atcoder.jp/contests/keyence2021/tasks/keyence2021_a)  
  aとcの最大値を記録しつつ全探索
  3. [B - log](https://atcoder.jp/contests/arc109/tasks/arc109_b)  
  これ二部探索なのか...すごい  
  1+2+....+x<=N+1の範囲で最大となるxを二部探索で見つける  
  その時答えはN-x+1となる
  4. [C - Exam and Wizard ](https://atcoder.jp/contests/keyence2019/tasks/keyence2019_c)  
  b-aの配列を用意して計算
  5. [D - Opposite](https://atcoder.jp/contests/abc197/tasks/abc197_d)  
  atan2を使うらしい、苦手問題
  6. [A - Range Flip Find Route](https://atcoder.jp/contests/agc043/tasks/agc043_a)  
  DP...reviewに追加するのであとからやる...
  




___


training24 ~ 27

time : 1hours  
difficulty  
1. 400~800
2. 400~800
3. 800~1200
4. 1200~1600

Exclude experimental difficulty  


___
### 2021/08/27

- training24
  1. [C - Many Medians ](https://atcoder.jp/contests/abc094/tasks/arc095_a)  
  中央値をあらかじめ2つ求めておく
  2. [C - Subarray Sum ](https://atcoder.jp/contests/keyence2020/tasks/keyence2020_c)  
  しょうもない問題...
  3. [C - Large RPS Tournament](https://atcoder.jp/contests/arc109/tasks/arc109_c)  
  文字列の長さの二倍程度調べるだけで全体の結果がわかる  
  連結した文字列をSとして2つ区切りで調べ、勝者の文字列Tを作る  
  それをSとして更新し、繰り返す。答えはS[0]
  4. [C - Exam and Wizard ](https://atcoder.jp/contests/keyence2019/tasks/keyence2019_c)  
  二部最大マッチングというらしい(初めてみた)  
  直感的にa<c、b<dという条件のうち最も大きいものからマッチングさせていけば良い


- training25
  1. [B - ARC Wrecker](https://atcoder.jp/contests/arc117/editorial/1111)  
  **数え上げ系の問題では、N が小さい場合を考えると考察が進むことがある**  

  2. [A - Multiple Array ](https://atcoder.jp/contests/agc009/tasks/agc009_a)  
  後ろから貪欲に計算していくという考察はあっていた  
  おそらくceilあたりで最小化に失敗してたのかな  
  とりあえず余りの時は何も考えずにa%bでいい  

  貪欲法の考察として  
  **今の自分にとっても後にとっても良くなる**ことがあげられる
  3. [C - Boxes and Candies](https://atcoder.jp/contests/abc048/tasks/arc064_a)  
  考察は完ぺきだった。x-a[i-1]が0を下回る場合を考えてなかった...
  4. []()  
  時間なかったのでとばす



- training26　(x : 3,4)
  1. [C - Not so Diverse](https://atcoder.jp/contests/arc086/tasks/arc086_a)  
  Counterで個数を数えてkを更新
  2. [A - Two Choices](https://atcoder.jp/contests/arc115/tasks/arc115_a)  
  前にやった、偶奇で分けて掛け算
  3. [B - Products of Min-Max](https://atcoder.jp/contests/arc116/tasks/)  
  愚直にやるとminとmaxを固定してforをまわO(N^2)  
  そこでminを固定し、sumを更新することでO(N)でできた  
  この手の問題を解けるようになりたい
  4. [F - Shift and Inversions](https://atcoder.jp/contests/abc190/tasks/abc190_f)  
  転倒数は Fenwick Treeやセグメントツリー を用いるらしい  
  なんとなくわかったがいまいちわかってない部分もある...  
  難しい問題にも慣れていきたい。





___
### 2021/08/28

- training27(x : 3,4)
  1. [C - Dice and Coin](https://atcoder.jp/contests/abc126/tasks/abc126_c)  
  全探索
  2. [D - Friends](https://atcoder.jp/contests/abc177/tasks/abc177_d)  
  Unionfindで最大のグループの大きさを調べる
  3. [D - Remainder Reminder](https://atcoder.jp/contests/arc091/tasks/arc091_b)  
  **片方を固定してもう片方については同じ要素/性質をまとめて数え上げる**
  4. []()  
  時間なかった


___


training28 ~ 

time : 1hours  
difficulty  
1. 400~800
2. 400~800
3. 400~800
4. 800~1200

Exclude experimental difficulty  



___

- training28(x : 3)
  1. [B - Trained?](https://atcoder.jp/contests/abc065/tasks/abc065_b)  
  実装のみ
  2. [C - Subarray Sum](https://atcoder.jp/contests/keyence2020/tasks/keyence2020_c)  
  Sの配列をk個用意して場合分け
  3. [C - Go Home](https://atcoder.jp/contests/abc056/tasks/arc070_a)  
  距離に時間の経過分追加していきXを超えたらループ終わり
  4. [E - Red and Green Apples ](https://atcoder.jp/contests/abc160/tasks/abc160_e)  
  貪欲法




- training29(x : 4)
  1. [C - Connect Cities](https://atcoder.jp/contests/abl/tasks/abl_c)  
  Unionfindの基本
  2. [C - Grand Garden ](https://atcoder.jp/contests/abc116/tasks/abc116_c)  
  h[i]<h[i+1]の時のみcountしていく
  3. [C - Skill Up](https://atcoder.jp/contests/abc167/tasks/abc167_c)  
  bit全探索の基本
  4. [D - Lamp ](https://atcoder.jp/contests/abc129/tasks/abc129_d)  
  left,right,up,downのその方向から光がとおれる道がいくつあるか数える  
  そしてそれぞれの和を求め重なっている分-3し、最大値が答え




- training30(x : 3,4)
  1. [C - Together](https://atcoder.jp/contests/abc072/tasks/arc082_a)  
  a[i]の値が何個あるのかを配列cntに記録し  
  cnt[i-1]+cnt[i]+cnt[i+1]の最大値を求める。  
  最初と最後だけindexのエラ＝が出るので注意
  2. [D - Derangement](https://atcoder.jp/contests/abc072/tasks/arc082_b)  
  貪欲に前からswapした  
  ひとつ前でswapした場合現在はswapする必要がないのでその処理に注意する
  3. [A - A+...+B Problem](https://atcoder.jp/contests/agc015/tasks/agc015_a)  
  まずA<Bと言われていないのでそこに注意する   
  **とりうる値は x 以上 y 以下の整数という具合に、区間になっていることがあげられるとき6  が作れて 8 も作れるなら 7 も作れる**
  4. [B - Exactly N points](https://atcoder.jp/contests/cf16-final/tasks/codefestival_2016_final_b)  
  Nを超えるまで和を計算する、超えた時点で和とNの差をとりその差を表示しないようにする




___
### 2021/08/29

- training32(x : 3,4)
  1. [C - Write and Erase ](https://atcoder.jp/contests/abc073/tasks/abc073_c)  
  dictにメモしてその数字の個数が奇数か偶数か
  2. [B - Choose Integers ](https://atcoder.jp/contests/abc060/tasks/abc060_b)  
  while文でA%B==0になるところからもう一度0になるところまでの間に  
  A%B==Cになるものがあるか見る
  3. [C - 一次元リバーシ](https://atcoder.jp/contests/abc047/tasks/arc063_a)  
  まず、a^b = x の時 x^a = bも成り立つ  
  自分はdictに要素をメモしながら  
  aを決め打ちすることでxを求めtmp_a = x^bでtmp_aがあるかどうか調べた  
  O(N*M)かな？
  (うまくいかなかったが)  

  解法ではc = a^xとして　配列に追加していきsortしてBと同じになるか比べていた  
  これは O(N**2*logN)
  
  4. [F - Range Xor Query](https://atcoder.jp/contests/abc185/tasks/abc185_f)  
  時間なかった  
  フェンウィック木(binary index tree)を使う  
  **-> 部分和の計算と要素の更新の両方を効率的に行える木構造**



___
AtCoder Beginner Contest 216

簡単な問題は素早く溶けるようになってきた  
ただ、難しい問題の耐性がなさすぎる
今後はdiff800-1600を中心に取り組みたい

___
