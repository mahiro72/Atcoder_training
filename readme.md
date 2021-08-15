# Atcoder
___
## 夏休みAtcoder頑張るための日記  
virtual contest でといた問題を記録していきます


training1 ~  

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
  
