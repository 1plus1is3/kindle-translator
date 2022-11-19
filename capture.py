"""
    kindle-translator
"""
import os
import time
import cv2
import pyautogui
from constant import OUTPUT_IMG_FOLDER
from os import path


class Capture:
    """
    特定の範囲のスクリーンショットを撮影するクラス
    """

    def window_manager(self) -> int:
        """
        :関数名:
            - window_manager
        :機能:
            - 撮影したい座標位置の取得

        :引数:
            - なし
        :戻り値:
            - tuple型(
                upper_left_x: 左上のx座標(int型)
                upper_left_y: 左上のy座標(int型)
                bottom_right_x: 右下のx座標(int型)
                bottom_right_y: 右下のy座標(int型)
            )
        """
        # 左上の座標を取得
        print("10秒以内に撮影したい範囲の左上にカーソルを合わせてください")
        time.sleep(10)
        upper_left_x, upper_left_y = pyautogui.position()
        print(f'左上の座標: {upper_left_x}, {upper_left_y}')

        # 右下の座標を取得
        print("10秒以内に撮影したい範囲の右下にカーソルを合わせてください")
        time.sleep(10)
        bottom_right_x, bottom_right_y = pyautogui.position()
        print(f'右上の座標: {bottom_right_x}, {bottom_right_y}')

        print('座標取得完了')

        return upper_left_x, upper_left_y, bottom_right_x, bottom_right_y

    def window_capture(
        self,
        x_1: int,
        y_1: int,
        x_2: int,
        y_2: int
    ) -> tuple:
        """
        :関数名:
            - window_capture
        :機能:
            - 電子書籍のページごとのスクリーンショットを撮影する

        :引数:
            - x_1: 左上のx座標(int型)
            - y_1: 左上のy座標(int型)
            - x_2: 右下のx座標(int型)
            - y_2: 右下のy座標(int型)
        :戻り値:
            - tuple型(
                page: 最後のページが何ページ目かの数値(int型)
                file_name: 保存したいテキスト名兼ファイル名(str型)
                img_file_path: 画像の保存先パス(str型)
            )
        """
        # 保存するテキスト名(ファイル名にもなる)をコンソールで入力
        print('保存するテキストファイル名を入力してください：')
        file_name = input()

        # 撮影できる最大のページ数
        max_page = 3000

        # スクリーンショットの間隔
        span = 0.1

        # 電子書籍リーダを起動するために10秒間待機
        time.sleep(10)

        # 画像の出力先となるフォルダパスを設定してフォルダを生成
        img_file_path = path.join(OUTPUT_IMG_FOLDER, file_name)
        os.mkdir(img_file_path)

        # 出力先フォルダに画像を出力していく
        os.chdir(img_file_path)
        print(f'{img_file_path}に画像を保存していきます')

        # 最初のページの撮影
        png_name = 'picture_0.png'
        screen_shot = pyautogui.screenshot(region=(
            x_1,
            y_1,
            x_2 - x_1,
            y_2 - y_1
        ))
        screen_shot.save(png_name)

        # ページ送りの方向(デフォルトは右)
        pyautogui.keyDown('right')
        pyautogui.keyUp('right')
        time.sleep(span)

        # 残りのページのスクリーンショット撮影
        for page in range(1, max_page):
            png_name = f'picture_{page}.png'
            screen_shot = pyautogui.screenshot(region=(
                x_1,
                y_1,
                x_2 - x_1,
                y_2 - y_1
            ))
            screen_shot.save(png_name)
            pyautogui.keyDown('right')
            pyautogui.keyUp('right')
            img_prev_name = f'picture_{page-1}.png'

            # 前のページとの差分を比較
            # 最大ページ数に到達したら撮影を終了する
            # もしくは差分が0であれば(最後のページに到達したら)撮影を終了する
            img_prev = cv2.imread(img_prev_name)
            img_current = cv2.imread(png_name)
            time.sleep(span)
            mask = cv2.absdiff(img_prev, img_current)
            mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
            if page == max_page or not cv2.countNonZero(mask_gray):
                break

        print('画像の保存が終了しました')

        return page, file_name, img_file_path
