"""
    kindle-translator
"""
import requests

class Translate:
    """
    テキストファイルの翻訳を行うクラス
    """
    def translate_with_deepl(
        self,
        file_list: list,
        file_name: str
    ) -> None:
        """
        :関数名:
            - translate_with_deepl
        :機能:
            - テキストファイルをDeepLを用いて翻訳し、結果をひとつのテキストファイルに書き込む

        :引数:
            - 分割されたファイルの名前のリスト(list型)
            - 保存したいファイルの名前(str型)
        :戻り値:
            - なし
        """
        print('テキストファイルの翻訳を行います')
        # XXXXXXの部分に自分のAPI Keyを入力
        API_KEY:str = 'XXXXXX'

        # file_listに記載されているファイルを順番に開いて翻訳にかける
        for partial_file_name in file_list:
            print('翻訳中...')
            # 翻訳したいファイルを開く
            with open(partial_file_name, "r", encoding="utf-8") as f:
                txt = f.read().replace('\n', ' ')

            # 英語から日本語に変換
            params = {
                "auth_key": API_KEY,
                "text": txt,
                "source_lang": 'EN',
                "target_lang": 'JA'
            }

            # DeepL APIにPOST
            # 無償版の場合は適宜URLを変更すること
            req = requests.post("https://api.deepl.com/v2/translate", data=params)

            # json形式で結果を取得
            result = req.json()

            # JA_foo.txtとしてtxt形式で結果を保存()
            with open(f'JA_{file_name}.txt', "a", encoding='utf-8') as text_file:
                text_file.write(result["translations"][0]["text"])

        # 句点で改行する
        with open(f'JA_{file_name}.txt', "r", encoding="utf-8") as f:
            raw_data = f.read().replace("。", "。\n")
        with open(f'JA_{file_name}.txt', "w", encoding='utf-8') as f:
            f.write(raw_data)

        print('翻訳が完了しました')
