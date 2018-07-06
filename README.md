# Discordで割り込み発言BOT
チャット欄の特定ワードに反応して発言者のボイスチャンネルに突撃して音を鳴らすBOT

# 参考
公式: [github](https://github.com/Rapptz/discord.py)  
tokenのとり方: [Qiita](https://qiita.com/PinappleHunter/items/af4ccdbb04727437477f)  

# 環境構築
## Pythonのインストール
推奨： [Enthought Canopy](https://www.enthought.com/product/canopy/)  
[ダウンロードリンク](https://store.enthought.com/downloads/): Windows[64-bit] 3.5を選択

Enthought Canopyを起動, "Tools" -> "Canopy Command Prompt"で

	$ pip install discord.py

## ffmpegのインストール
公式：　[ffmpeg](https://www.ffmpeg.org/)  
[ダウンロードリンク](https://www.ffmpeg.org/download.html): Windows Buildsを選択  

- VersionはStable(日付ではなく4.0とか書いてる方)  
- ArchitectureはWindows 64-bit
- LinkingはStatic

### 環境変数の設定  
"コントロールパネル" -> "システムとセキュリティ" -> "システム" -> "システムの詳細設定" -> "環境変数"  
ユーザー環境変数(上段)の"Path"に"{ffmpeg-install-path}\bin"を追記

Enthought Canopyを起動, "Tools" -> "Canopy Command Prompt"で  

	$ ffmpeg
と打ち込んでバージョン情報が出てくればOK

#　BOTを使う
## トークンの設定
Enthought Canopyを起動 -> "Editor"  
bot.pyを開く  
コード下部の"トークンの指定"で  

	token = "Discordから支給されたBOTのtoken"  
と指定  

画面上部の実行ボタンを押すと実行  

	Loggd in as
	{BOT Name}
	{BOT ID}

が表示されて入れば正常

## 音声ファイルと発言のヒモ付け
dict.yamlを開く

	folder: "ボイスファイルのルートフォルダ"

	passphrases:
		"反応キーワード":
			"対応するBOTの発言" : "再生する音声ファイル名"

	volumes:
		"反応キーワード": 音声ファイルのボリューム(0.5, 1,　など)

再生する音声ファイル名が空文字列("")であれば対応する発言のみして音声は流れない
