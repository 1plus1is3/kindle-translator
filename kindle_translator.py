"""
    kindle-translator
"""
from capture import Capture
from ocr import OCR
from translator import Translate
from PDFconverter import PDFConverter


class Main:
    """
    kindle_translatorを実行するMainクラス
    """

    capture = Capture()
    ocr = OCR()
    translator = Translate()
    convert = PDFConverter()

    # スクリーンショットを撮影する範囲の座標を取得
    x_1, y_1, x_2, y_2 = capture.window_manager()

    # ページごとにスクリーンショットを撮影(png形式で保存)
    page_number, file_name, img_file_path = capture.window_capture(x_1, y_1, x_2, y_2)

    # 取得した画像から文字を抽出してひとつのtxtファイルに保存
    file_name_txt, txt_file_path = ocr.extract_characters(page_number, file_name, img_file_path)

    # DeepLに投げられるようにファイルを100キロバイトごとに分割して保存
    file_list = ocr.divide_file(file_name, file_name_txt)

    # テキストファイルをDeepLに投げる
    translator.translate_with_deepl(file_list, file_name)

    # 翻訳されたテキストファイルをPDF形式に変換
    # 出力先はテキストファイルと同じフォルダ
    convert.text_to_pdf(file_name)
