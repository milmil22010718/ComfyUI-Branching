# ComfyUI-Branching

## 概要
[下記の処理を*補助*します。]
1.テキストファイルAとテキストファイルBを読み込む
2.テキストファイルAを一行読み込む
3.テキストファイルBを全行を一行ずつ読み込む
4.手順3が終わったら、手順2に戻ってテキストファイルAの二行目を読み込む

処理の完了.テキストファイルAが最終行が読み込んだ後、手順3の処理が完了する。

テキストファイルの読み込み等は他者様のカスタムノードをご利用願います。

## イメージ
一回目の処理
![image1](https://github.com/milmil22010718/ComfyUI-Branching/assets/172750174/74e917f9-f743-466e-bf7d-1fd38301c9f3)

二回目の処理
![image2](https://github.com/milmil22010718/ComfyUI-Branching/assets/172750174/a341a905-ce46-488e-9d1d-7d1eeda006fa)
・
・
・
最後の処理
![image3](https://github.com/milmil22010718/ComfyUI-Branching/assets/172750174/7547d35e-b270-4cfe-b833-e07c456302fb)


## カスタムノードの追加
・Add Node>>Branching_Line>>BranchingTextLine から追加できます。
![image4](https://github.com/milmil22010718/ComfyUI-Branching/assets/172750174/f72a6620-fa5d-4452-bc05-786fe8e49d7a)

## 使用方法
・Counterには0からインクリメントするCustomノードを接続してください。
下記の画像では、AonekoSS様の"ComfyUI-SimpleCounter"を使用させていただいております。
https://github.com/AonekoSS/ComfyUI-SimpleCounter
・A_LineとB_Lineには読み込むテキストファイルの最終行を入力してください。
![image5](https://github.com/milmil22010718/ComfyUI-Branching/assets/172750174/5e5036c0-d7a3-4fdc-b838-0de21535e8da)

## 動作の例
![image5](https://github.com/milmil22010718/ComfyUI-Branching/assets/172750174/1d77e586-45cf-4f06-97ab-ea5b7922fd3e)

index_Aとindex_Bから処理の結果が出力されます。
*例*
A_LineとB_Lineに3が入力されている場合下記の出力結果が得られます。

index_A:0
index_B:0

index_A:0
index_B:1

index_A:0
index_B:2

index_A:1
index_B:0

index_A:1
index_B:1
・
・
・
index_A:2
index_B:2

## ライセンス
ご自由にお使いいただければ幸いです。

