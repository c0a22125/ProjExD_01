import sys
import pygame as pg

def main():
    # ゲームウィンドウの設定
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    # 画像の読み込み
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_imgs = [bg_img, pg.transform.flip(bg_img, True, False)]#背景を反転させて元の画像とのリストを作成
    kk_img = pg.image.load("ex01/fig/3.png")#練習2、こうかとん表示
    kk_img = pg.transform.flip(kk_img, True, False)#練習2、画像を左右反転
    kk_imgs = [pg.transform.rotozoom(kk_img, i, 1.0) for i in range(1, 11)] + [pg.transform.rotozoom(kk_img, i, 1.0) for i in range(10, 0, -1)]#練習3、1～10度傾いたこうかとんを作成しリストを作る

    # ゲームループの開始
    tmr = 0
    bg_x = 0
    while True:
        # イベントの処理
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return  # ウィンドウが閉じられたらゲームループを終了

        # 背景の描画
        bg_x = tmr
        bg_img_x = [1600 * i for i in range(10)]#10回繰り返す
        for i in range(len(bg_img_x)):
            screen.blit(bg_imgs[i % 2], [bg_img_x[i] - bg_x, 0])#背景の元の画像と反転させた画像を交互に出力(繰り返す回数は上で指定)

        screen.blit(kk_imgs[tmr % 20], [300,200])#練習5、こうかとんが羽ばたくような動きを実装し表示
        pg.display.update()

        # ゲーム内タイマーの更新
        tmr += 1


        # フレームレートの制御（10FPS）
        clock.tick(60)#フレームレートが10だと羽ばたくのがおそくなってしまうため60に変更した

if __name__ == "__main__":
    # Pygameの初期化
    pg.init()

    # ゲームのメインループを実行
    main()

    # Pygameの終了
    pg.quit()

    # スクリプトの終了
    sys.exit()
