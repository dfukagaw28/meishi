from hentaigana import kana2hentaigana

# 一般的な名刺のサイズは 91mm×55mm = 3.583 inch × 2.165 inch
DPI = 350
WIDTH = int(91 / 25.4 * DPI)
HEIGHT = int(55 / 25.4 * DPI)

# 変換前の名前（ひらがな）
name = u'にいじま やゑ'

# 変換後の名前
name2 = None

# PGraphics オブジェクト
pg = None

# フォントオブジェクト
font1 = None
font2 = None

# プログラムを実行したときに1度だけ実行される関数を定義する
def setup():
    # グローバル変数を利用するための宣言
    global name2, pg, font1, font2

    # サイズを設定する
    size(WIDTH, HEIGHT)
    
    # 描画用グラフィックスオブジェクト
    pg = createGraphics(WIDTH, HEIGHT)
    
    # フォントオブジェクトを生成する
    font1 = loadFont("Candara-Italic-24.vlw")    
    font2 = createFont("UniHentaiKana-Regular.otf", 64)    

    # 名前を変体仮名に変換する
    name2 = kana2hentaigana(name)

    # static モード
    noLoop()

# 描画する内容を定義する
def draw():
    # グローバル変数を利用するための宣言
    global pg, font1, font2
    
    # 描画を開始する
    pg.beginDraw()
    
    # 滑らかに
    pg.smooth()
    
    # 背景をリセット（不透明度を 0 にして透過させる）
    pg.colorMode(RGB, 255)
    pg.background(0, 0, 0, 0)
    
    # 背景を描画する
    for _ in range(200):
        x = random(width)
        y = random(height)
        r = random(30, 100)
        c = random(100)
        pg.colorMode(HSB, 100)
        pg.stroke(c, 30, 100)
        pg.noFill()
        pg.ellipse(x, y, r, r)
    
    # 右下にロゴ（？）を描画する
    pg.textFont(font1)
    pg.textAlign(RIGHT, BOTTOM)
    pg.colorMode(RGB, 255)
    pg.fill(200)
    pg.text('Doshisha University Girls Science Camp 2022', width - 15, height - 15)

    # 変体仮名フォントで名前を描画する
    pg.textFont(font2)
    pg.textAlign(CENTER, TOP)
    pg.colorMode(RGB, 255)
    pg.fill(0)
    pg.text(name2, width/2, height/2)

    # 描画を終了する
    pg.endDraw()

    background(255, 255, 240)
    image(pg, 0, 0)

# マウスをクリックしたときに実行される関数を定義する
def mouseClicked():
    # グローバル変数を利用するための宣言
    global name2

    # 名前を変体仮名に変換する
    name2 = kana2hentaigana(name)
    
    redraw()

# キーボードのキーを押したときに実行される関数を定義する
def keyPressed():
    # グローバル変数を利用するための宣言
    global pg
    
    # ファイルに保存する
    pg.save('output.png')
