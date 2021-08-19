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
  3. [A - Shik and Stone](https://atcoder.jp/contests/agc007/tasks/agc007_a)  
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
  3. [E - Akari](https://atcoder.jp/contests/abc182/tasks/abc182_e)  
  愚直に光が届いてるか調べたらO(HW)  
  ただうまく実装できていない.......


- training15
  1. [A - Remove Substrings](https://atcoder.jp/contests/agc054/tasks/agc054_a)  
  場合分け、
  2. [C - 4-adjacent](https://atcoder.jp/contests/arc080/tasks/arc080_a)  
  N-1の幅で考えた。その中で4で割り切れるものと2が2つで4の倍数になる可能性があるものの2パターン考えた
  3. [C - String Invasion](https://atcoder.jp/contests/arc113/tasks/arc113_c)  
  まえやった
  3. [A - Shik and Stone](https://atcoder.jp/contests/agc007/tasks/agc007_a)  
  ダイクストラはO(NlogN)でできるらしい  
  ポイントは最短距離を時間にするのだが、与えられたT,Kを使って1つの式を作れるか
