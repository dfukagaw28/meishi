#add_library('pdf')

from hentaigana import kana2hentaigana

class Meishi:
    def __init__(self):
        self.font = None
    
    # 変体仮名フォントで名前を描画する
    def draw(self):
        g = self.g
        g.pushStyle()
        if self.font:
            g.textFont(self.font)
        g.textAlign(CENTER, CENTER)
        g.fill(0)
        g.text(self.name2, width/2, height/2)
        g.popStyle()

    def set_name(self, value):
        self.name = value
        
        # 変体仮名をランダムに変更する    
        # 同じ音価を持つ複数の変体仮名からランダムに選ばれる
        self.name2 = kana2hentaigana(self.name)

    # ロゴを表示する
    def drawLogo(self):
        g = self.g
        g.pushStyle()
        g.textSize(24)
        g.textAlign(RIGHT, BOTTOM)
        g.colorMode(RGB, 255)
        g.fill(200)
        g.text('Doshisha University Girls Summer Camp 2022', width - 15, height - 15)
        g.popStyle()

    # 保存する
    def save(self):
        g = self.g
        g.save(FILENAME)

# 一般的な名刺のサイズは 91mm×55mm = 3.583 inch × 2.165 inch
DPI = 350
WIDTH = int(91 / 25.4 * DPI)
HEIGHT = int(55 / 25.4 * DPI)

# 名前を設定する（ひらがな）
NAME = u'にいじま やゑ'

# 出力先ファイル名
FILENAME = 'output.png'

# 描画バッファを利用するかどうか
# （透過PNGを作成する場合は必須）
IMAGE_BUFFER = False

# 名刺オブジェクト
meishi = Meishi()

# プログラムを実行したときに1度だけ実行される関数を定義する
def setup():
    # サイズを設定する
    size(WIDTH, HEIGHT)
    
    # 名前を設定する
    meishi.set_name(NAME)
    
    # フォントオブジェクトを生成する
    meishi.font = createFont("UniHentaiKana-Regular.otf", 128)

    # static モード
    noLoop()

# 描画する内容を定義する
def draw():
    # PGraphics オブジェクトを取得 or 生成する
    if IMAGE_BUFFER:
        pg = createGraphics(WIDTH, HEIGHT)
        pg.beginDraw()
        pg.colorMode(RGB, 255)
        pg.background(0, 0, 0, 0)
    else:
        pg = g
        colorMode(RGB, 255)
        background(255, 255, 240)
    meishi.g = pg

    # 背景を描画する
    pg.pushStyle()
    pg.colorMode(HSB, 100)
    pg.noFill()
    for _ in range(200):
        x = random(width)
        y = random(height)
        r = random(30, 100)
        c = random(100)
        pg.stroke(c, 30, 100)
        pg.ellipse(x, y, r, r)
    pg.popStyle()
    
    print(2222)
    # 右下にロゴ（？）を描画する
    meishi.drawLogo()

    print(2222)
    # 変体仮名フォントで名前を描画する
    meishi.draw()
    
    if pg != g:
        pg.endDraw()
        background(255, 255, 240)
        image(pg, 0, 0)

# マウスをクリックしたときに実行される関数を定義する
def mouseClicked():
    # 名前を変体仮名に変換する
    meishi.set_name(NAME)
    
    # キャンバスを更新する
    redraw()

# キーボードのキーを押したときに実行される関数を定義する
def keyPressed():
    # キャンバスの内容をファイルに保存する
    meishi.save()
