"""
    kindle-translator
"""
from fpdf import FPDF
from constant import FONT_PATH


class PDFConverter:
    """
    テキストファイルをPDFに変換するクラス
    """
    def text_to_pdf(self, file_name: str,) -> None:
        """
        :関数名:
            - text_to_pdf
        :機能:
            - テキストファイルをPDFに変換する

        :引数:
            - 翻訳済みのテキストファイル名
        :戻り値:
            - None
        """
        print('翻訳したファイルをPDFに変換しています...')

        # FPDF2のインスタンス化
        pdf = FPDF()

        pdf.add_page()

        pdf.add_font("yumin", fname=FONT_PATH, uni=True)
        pdf.set_font('yumin', size=12)

        # テキストファイルを開いてPDF形式で書き込み
        with open(f'JA_{file_name}.txt', 'r', encoding='utf-8') as f:
            for page in f:
                pdf.write(txt=page)

        # pdf形式で保存
        pdf.output(f'{file_name}.pdf')

        print('全ての工程が終了しました。フォルダに移動して、成果物を確認してください')
