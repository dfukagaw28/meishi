# encoding: utf-8

import random
import unicodedata

KANA_TABLE_SMALL = {
    u'ぁ': u'あ',
    u'ぃ': u'い',
    u'ぅ': u'う',
    u'ぇ': u'え',
    u'ぉ': u'お',
    u'ゃ': u'や',
    u'ゅ': u'ゆ',
    u'ょ': u'よ',
    u'ゎ': u'わ',
}

KANA_TABLE_HENTAIGANA = {
    u'あ':[0x1B002,0x1B003,0x1B004,0x1B005],
    u'い':[0x1B006,0x1B007,0x1B008,0x1B009],
    u'う':[0x1B00A,0x1B00B,0x1B00C,0x1B00D,0x1B00E],
    u'え':[0x1B001,0x1B00F,0x1B010,0x1B011,0x1B012,0x1B013],
    u'お':[0x1B014,0x1B015,0x1B016],
    u'か':[0x1B017,0x1B018,0x1B019,0x1B01A,0x1B01B,0x1B01C,0x1B01D,0x1B01E,0x1B01F,0x1B020,0x1B021,0x1B022],
    u'き':[0x1B023,0x1B024,0x1B025,0x1B026,0x1B027,0x1B028,0x1B029,0x1B02A,0x1B03B],
    u'く':[0x1B02B,0x1B02C,0x1B02D,0x1B02E,0x1B02F,0x1B030,0x1B031],
    u'け':[0x1B022,0x1B032,0x1B033,0x1B034,0x1B035,0x1B036,0x1B037],
    u'こ':[0x1B038,0x1B039,0x1B03A,0x1B03B,0x1B098],
    u'さ':[0x1B03C,0x1B03D,0x1B03E,0x1B03F,0x1B040,0x1B041,0x1B042,0x1B043],
    u'し':[0x1B044,0x1B045,0x1B046,0x1B047,0x1B048,0x1B049],
    u'す':[0x1B04A,0x1B04B,0x1B04C,0x1B04D,0x1B04E,0x1B04F,0x1B050,0x1B051],
    u'せ':[0x1B052,0x1B053,0x1B054,0x1B055,0x1B056],
    u'そ':[0x1B057,0x1B058,0x1B059,0x1B05A,0x1B05B,0x1B05C,0x1B05D],
    u'た':[0x1B05E,0x1B05F,0x1B060,0x1B061],
    u'ち':[0x1B062,0x1B063,0x1B064,0x1B065,0x1B066,0x1B067,0x1B068],
    u'つ':[0x1B069,0x1B06A,0x1B06B,0x1B06C,0x1B06D],
    u'て':[0x1B06E,0x1B06F,0x1B070,0x1B071,0x1B072,0x1B073,0x1B074,0x1B075,0x1B076,0x1B08E],
    u'と':[0x1B06D,0x1B077,0x1B078,0x1B079,0x1B07A,0x1B07B,0x1B07C,0x1B07D],
    u'な':[0x1B07E,0x1B07F,0x1B080,0x1B081,0x1B082,0x1B083,0x1B084,0x1B085,0x1B086],
    u'に':[0x1B087,0x1B088,0x1B089,0x1B08A,0x1B08B,0x1B08C,0x1B08D,0x1B08E],
    u'ぬ':[0x1B08F,0x1B090,0x1B091],
    u'ね':[0x1B092,0x1B093,0x1B094,0x1B095,0x1B096,0x1B097,0x1B098],
    u'の':[0x1B099,0x1B09A,0x1B09B,0x1B09C,0x1B09D],
    u'は':[0x1B09E,0x1B09F,0x1B0A0,0x1B0A1,0x1B0A2,0x1B0A3,0x1B0A4,0x1B0A5,0x1B0A6,0x1B0A7,0x1B0A8],
    u'ひ':[0x1B0A9,0x1B0AA,0x1B0AB,0x1B0AC,0x1B0AD,0x1B0AE,0x1B0AF],
    u'ふ':[0x1B0B0,0x1B0B1,0x1B0B2],
    u'へ':[0x1B0B3,0x1B0B4,0x1B0B5,0x1B0B6,0x1B0B7,0x1B0B8,0x1B0B9],
    u'ほ':[0x1B0BA,0x1B0BB,0x1B0BC,0x1B0BD,0x1B0BE,0x1B0BF,0x1B0C0,0x1B0C1],
    u'ま':[0x1B0C2,0x1B0C3,0x1B0C4,0x1B0C5,0x1B0C6,0x1B0C7,0x1B0C8,0x1B0D6],
    u'み':[0x1B0C9,0x1B0CA,0x1B0CB,0x1B0CC,0x1B0CD,0x1B0CE,0x1B0CF],
    u'む':[0x1B0D0,0x1B0D1,0x1B0D2,0x1B0D3,0x1B11D,0x1B11E],
    u'め':[0x1B0D4,0x1B0D5,0x1B0D6],
    u'も':[0x1B0D7,0x1B0D8,0x1B0D9,0x1B0DA,0x1B0DB,0x1B0DC,0x1B11D,0x1B11E],
    u'や':[0x1B0DD,0x1B0DE,0x1B0DF,0x1B0E0,0x1B0E1,0x1B0E2],
    u'ゆ':[0x1B0E3,0x1B0E4,0x1B0E5,0x1B0E6],
    u'よ':[0x1B0E2,0x1B0E7,0x1B0E8,0x1B0E9,0x1B0EA,0x1B0EB,0x1B0EC],
    u'ら':[0x1B07D,0x1B0ED,0x1B0EE,0x1B0EF,0x1B0F0],
    u'り':[0x1B0F1,0x1B0F2,0x1B0F3,0x1B0F4,0x1B0F5,0x1B0F6,0x1B0F7],
    u'る':[0x1B0F8,0x1B0F9,0x1B0FA,0x1B0FB,0x1B0FC,0x1B0FD],
    u'れ':[0x1B0FE,0x1B0FF,0x1B100,0x1B101],
    u'ろ':[0x1B102,0x1B103,0x1B104,0x1B105,0x1B106,0x1B107],
    u'わ':[0x1B108,0x1B109,0x1B10A,0x1B10B,0x1B10C],
    u'ゐ':[0x1B10D,0x1B10E,0x1B10F,0x1B110,0x1B111],
    u'ゑ':[0x1B112,0x1B113,0x1B114,0x1B115],
    u'を':[0x1B005,0x1B116,0x1B117,0x1B118,0x1B119,0x1B11A,0x1B11B,0x1B11C],
    u'ん':[0x1B11D,0x1B11E],
}

def kana_upper(char):
    return KANA_TABLE_SMALL[char] if char in KANA_TABLE_SMALL else char

def k2h(c):
    c2 = kana_upper(c)
    if c2 in KANA_TABLE_HENTAIGANA:
        codes = KANA_TABLE_HENTAIGANA[c2]
        code = random.choice(codes)
        return unichr(code)
    return c

def kana2hentaigana(s):
    s2 = unicodedata.normalize('NFD', s)
    arr = map(k2h, list(s2))
    return ''.join(arr)
