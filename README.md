# kindle-translator

非母語で書かれた電子書籍やPDFを母語で書かれたPDFに翻訳するツールです。

# 特長

一冊50万字あるKindleの洋書を1分で日本語PDFに変換できます。

キーボードの矢印キーでページ送りができるならKindleに限らずあらゆる電子書籍リーダおよびPDFビューワで使え、DeepLが対応している言語であれば英語以外の言語でも翻訳できます(仏→日とか)。

# これがこうなる

![Kindle for PC - The Ethics of Cybersecurity_ 21 (The International Library of Ethics, Law and Technology) 2022_11_08 23_22_07](https://user-images.githubusercontent.com/99042183/201051157-86063261-ad8e-4ad8-977b-efc73a9359e5.png)

↓

![Cybersecurity pdf - Adobe Acrobat Reader (64-bit) 2022_11_08 23_36_27](https://user-images.githubusercontent.com/99042183/201051238-43cbea77-1dae-4f98-9899-f37f24348940.png)

(引用 **The Ethics of Cybersecurity (The International Library of Ethics, Law and Technology Book 21) by by Markus Christen, Bert Gordijn, et al. Feb 10, 2020)
(CC: BYです)

# 必要なライブラリ

pyautogui  
img2pdf  
Pillow  
opencv-python  
pyocr  
fpdf2  
python-dotenv  
requests  

# 準備

## 1. pipまたはcondaが使えるPythonの実行環境

本ツールはpythonで書かれています。必要なライブラリをrequirements.txtおよびvenv.yamlに出力してあるので、pipを使う場合はrequirements.txtを、condaを使う場合はvenv.yamlをそれぞれ使用して仮想環境を整えてください。

### pipを使ったインストール

```bash
pip install -r requirements.txt
```

### condaを使ったインストール

```bash
conda <env name> create -f venv.yml
```

## 2. DeepL APIの登録

以下からAPI版DeepLに登録してください。(無料版であってもクレジットカードの登録が必要です)

[https://www.deepl.com/ja/pro#developer](https://www.deepl.com/ja/pro#developer)

無料版で構いませんが、その場合はtranslator.pyの48行目のURLをapi.deepl.comからapi-free.deepl.comに変更しておく必要があります。

登録が済んだら、[local.env](./local.env)の`DEEPL_API_KEY`を入力してください。

## 3. Tesseractのインストール

以下から自分の環境に合ったインストーラをダウンロードしてください。

[https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

インストールが終わったら、[local.env](./local.env)の`TESSERACT_PATH`を自分の環境に適したパスへと変更してください。

## 4. フォルダパスの設定

画像保存用フォルダとテキストファイル(とできたPDFファイル)を保存するフォルダを準備し、[local.env](./local.env)の`OUTPUT_IMG_FOLDER`と`OUTPUT_TXT_FOLDER`を適宜変更してください。

# 使い方

![Anaconda Powershell Prompt (Anaconda3) 2022_11_08 23_36_32](https://user-images.githubusercontent.com/99042183/201052912-550244b1-873b-4755-9c10-6936bee8f898.png)

このリポジトリをcloneし、

```
python kindle_translator.py
```

を実行するだけでOKです。画像の通り、ほとんどの作業がコンソール上で進みます。

その後は**電子書籍リーダをクリックしてアクティブにした上で**左上にカーソルをあてて10秒待ち、また右下にカーソルをあてて10秒待ちます。

すると座標が取得でき、保存するファイル名・フォルダ名を聞かれるので入力しましょう。拡張子はいりません。

あとは自動でフォルダが作られ、翻訳され、できたPDFがフォルダに格納されます。

# 注意

- デフォルトでは、ページ送り方向が【右】になっています。必要に応じて変更してください。(capture.py 104-105行目、118-119行目)
- 現在のバージョンでは、スクリーンショットの撮影を行うため大量のpngファイルが生成されます。容量に余裕をもって実行してください。
- 現在のバージョンでは、生成されたpngファイルやtxtファイルは自動で削除されません。必要に応じて手動で消去してください。

# 制作者

- 相良スヒト
- Twitter: @1plus1is__
