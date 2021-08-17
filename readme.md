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


training4 ~  

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
  解法はあっていたがsetやpopを使ったことに予知おそらくどこかで  
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

