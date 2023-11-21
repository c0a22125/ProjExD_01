import sys
import pygame as pg

def main():
    # ゲームウィンドウの設定
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    # 画像の読み込み
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")#練習2、こうかとん表示
    kk_img = pg.transform.flip(kk_img, True, False)#練習2、画像を左右反転
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 10 , 1.0)]#練習3、10度傾いたこうかとんを作成しリストを作る

    # ゲームループの開始
    tmr = 0
    while True:
        # イベントの処理
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return  # ウィンドウが閉じられたらゲームループを終了

        # 背景の描画
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_imgs[1], [300,200])
        pg.display.update()

        # ゲーム内タイマーの更新
        tmr += 1

        # フレームレートの制御（10FPS）
        clock.tick(60)

if __name__ == "__main__":
    # Pygameの初期化
    pg.init()

    # ゲームのメインループを実行
    main()

    # Pygameの終了
    pg.quit()

    # スクリプトの終了
    sys.exit()
