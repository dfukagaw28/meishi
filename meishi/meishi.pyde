#add_library('pdf')

from hentaigana import kana2hentaigana

class Meishi:
    def __init__(self):
        self.font = None
    
    # 変体仮名フォントで名前を描画する
    def drawName(self, g):
        # 開始
        g.pushStyle()

        # 中央に配置する
        g.textAlign(CENTER, CENTER)
        
        # 文字の色は黒(0)
        g.fill(0)
        
        if g == self.g:
            # 表面（変体仮名）
            
            # フォントを設定する
            g.textFont(self.font)

            # 文字を描く
            g.text(self.name2, width/2, height/2)
        else:
            # 裏面（現代仮名）
        
            # フォントを設定する
            g.textFont(self.font_back)

            # 文字を描く
            g.text(self.name, width/2, height/2)
        
        # 終了
        g.popStyle()

    def set_name(self, value):
        self.name = value
        
        # 変体仮名をランダムに変更する    
        # 同じ音価を持つ複数の変体仮名からランダムに選ばれる
        self.name2 = kana2hentaigana(self.name)

    # ロゴを表示する
    def drawLogo(self, g):
        # 開始
        g.pushStyle()
        
        # 文字の大きさ
        g.textSize(24)
        
        # 文字の配置
        g.textAlign(RIGHT, BOTTOM)
        
        # 文字の色
        g.colorMode(RGB, 255)
        g.fill(200)
        
        # 文字を描く
        g.text('Doshisha University Girls Summer Camp 2022', width - 15, height - 15)
        
        # 終了
        g.popStyle()

    # 保存する
    def save(self):
        self.g.save(FILENAME_FRONT)
        self.g_back.save(FILENAME_BACK)
        print(u'保存しました:', FILENAME_FRONT, FILENAME_BACK)

# 一般的な名刺のサイズは 91mm×55mm = 3.583 inch × 2.165 inch
DPI = 350
WIDTH = int(91 / 25.4 * DPI)
HEIGHT = int(55 / 25.4 * DPI)

# 名前を設定する（ひらがな）
NAME = u'にいじま やゑ'

# 出力先ファイル名
FILENAME_FRONT = 'output_front.png'
FILENAME_BACK = 'output_back.png'

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
    meishi.font_back = createFont("ipamjm.ttf", 128)
    
    # PGraphics オブジェクトを生成する
    meishi.g = createGraphics(WIDTH, HEIGHT)
    meishi.g_back = createGraphics(WIDTH, HEIGHT)

    # static モード
    noLoop()

# 描画する内容を定義する
def draw():
    for pg in [meishi.g, meishi.g_back]:
        # 描画を開始する
        pg.beginDraw()
        
        # 背景をリセットする
        # 透明にする（不透明度=0）
        pg.colorMode(RGB, 255)
        pg.background(0, 0, 0, 0)

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
        
        # 右下にロゴ（？）を描画する
        meishi.drawLogo(pg)
        
        # 変体仮名フォントで名前を描画する
        meishi.drawName(pg)
        
        # 描画を終了する
        pg.endDraw()
    
    # 結果を画面に表示する
    background(255, 255, 240)
    image(meishi.g, 0, 0)

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
