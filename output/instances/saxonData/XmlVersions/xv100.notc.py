from output.models.saxon_data.xml_versions.xv100_noti_xsd.xv100_noti import Doc


obj = Doc(
    e=[
        '!"#$%&\'()*+,',
        ';<=>?@',
        '[\\]^',
        '`',
        '{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0¡¢£¤¥¦§¨©ª«¬\xad®¯°±²³´µ¶',
        '¸¹º»¼½¾¿',
        '×',
        '÷',
        ';',
        '\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u200b',
        '\u200e\u200f‐‑‒–—―‖‗‘’‚‛“”„‟†‡•‣․‥…‧\u2028\u2029\u202a\u202b\u202c\u202d\u202e\u202f‰‱′″‴‵‶‷‸‹›※‼‽‾',
        '⁁⁂⁃⁄⁅⁆⁇⁈⁉⁊⁋⁌⁍⁎⁏⁐⁑⁒⁓⁔⁕⁖⁗⁘⁙⁚⁛⁜⁝⁞\u205f\u2060\u2061\u2062\u2063\u2064\u2065\u2066\u2067\u2068\u2069\u206a\u206b\u206c\u206d\u206e\u206f',
        '←↑→↓↔↕↖↗↘↙↚↛↜↝↞↟↠↡↢↣↤↥↦↧↨↩↪↫↬↭↮↯↰↱↲↳↴↵↶↷↸↹↺↻↼↽↾↿⇀⇁⇂⇃⇄⇅⇆⇇⇈⇉⇊⇋⇌⇍⇎⇏⇐⇑⇒⇓⇔⇕⇖⇗⇘⇙⇚⇛⇜⇝⇞⇟⇠⇡⇢⇣⇤⇥⇦⇧⇨⇩⇪⇫⇬⇭⇮⇯⇰⇱⇲⇳⮜⮝⮞⮟⮠⮡⮢⮣⮤⮥⮦⮧⮨⮩⮪⮫⮬⮭⮮⮯⮰⮱⮲⮳⮴⮵⮶⮷⮸⮹⮺⮻⮼⮽⮾⮿⯀⯁⯂⯃⯄⯅⯆⯇⯈⯉⯊⯋⯌⯍⯎⯏⯐⯑⯒⯓⯔⯕⯖⯗⯘⯙⯚⯛⯜⯝⯞⯟⯠⯡⯢⯣⯤⯥⯦⯧⯨⯩⯪⯫⯬⯭⯮⯯⯰⯱⯲⯳⯴⯵⯶⯷⯸⯹⯺⯻⯼⯽⯾⯿',
        '⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻⿼⿽⿾⿿\u3000',
        '\ufdd0\ufdd1\ufdd2\ufdd3\ufdd4\ufdd5\ufdd6\ufdd7\ufdd8\ufdd9\ufdda\ufddb\ufddc\ufddd\ufdde\ufddf\ufde0\ufde1\ufde2\ufde3\ufde4\ufde5\ufde6\ufde7\ufde8\ufde9\ufdea\ufdeb\ufdec\ufded\ufdee\ufdef',
        '\U000f0000\U000f0001\U000f0002\U000f0003\U000f0004\U000f0005\U000f0006\U000f0007\U000f0008\U000f0009\U000f000a\U000f000b\U000f000c\U000f000d\U000f000e\U000f000f\U000f0010\U000f0011\U000f0012\U000f0013\U000f0014\U000f0015\U000f0016\U000f0017\U000f0018\U000f0019\U000f001a\U000f001b\U000f001c\U000f001d\U000f001e\U000f001f\U000f0020\U000f0021\U000f0022\U000f0023\U000f0024\U000f0025\U000f0026\U000f0027\U000f0028\U000f0029\U000f002a\U000f002b\U000f002c\U000f002d\U000f002e\U000f002f\U000f0030\U000f0031\U000f0032\U000f0033\U000f0034\U000f0035\U000f0036\U000f0037\U000f0038\U000f0039\U000f003a\U000f003b\U000f003c\U000f003d\U000f003e\U000f003f\U000f0040\U000f0041\U000f0042\U000f0043\U000f0044\U000f0045\U000f0046\U000f0047\U000f0048\U000f0049\U000f004a\U000f004b\U000f004c\U000f004d\U000f004e\U000f004f\U000f0050\U000f0051\U000f0052\U000f0053\U000f0054\U000f0055\U000f0056\U000f0057\U000f0058\U000f0059\U000f005a\U000f005b\U000f005c\U000f005d\U000f005e\U000f005f\U000f0060\U000f0061\U000f0062\U000f0063\U0010ff9b\U0010ff9c\U0010ff9d\U0010ff9e\U0010ff9f\U0010ffa0\U0010ffa1\U0010ffa2\U0010ffa3\U0010ffa4\U0010ffa5\U0010ffa6\U0010ffa7\U0010ffa8\U0010ffa9\U0010ffaa\U0010ffab\U0010ffac\U0010ffad\U0010ffae\U0010ffaf\U0010ffb0\U0010ffb1\U0010ffb2\U0010ffb3\U0010ffb4\U0010ffb5\U0010ffb6\U0010ffb7\U0010ffb8\U0010ffb9\U0010ffba\U0010ffbb\U0010ffbc\U0010ffbd\U0010ffbe\U0010ffbf\U0010ffc0\U0010ffc1\U0010ffc2\U0010ffc3\U0010ffc4\U0010ffc5\U0010ffc6\U0010ffc7\U0010ffc8\U0010ffc9\U0010ffca\U0010ffcb\U0010ffcc\U0010ffcd\U0010ffce\U0010ffcf\U0010ffd0\U0010ffd1\U0010ffd2\U0010ffd3\U0010ffd4\U0010ffd5\U0010ffd6\U0010ffd7\U0010ffd8\U0010ffd9\U0010ffda\U0010ffdb\U0010ffdc\U0010ffdd\U0010ffde\U0010ffdf\U0010ffe0\U0010ffe1\U0010ffe2\U0010ffe3\U0010ffe4\U0010ffe5\U0010ffe6\U0010ffe7\U0010ffe8\U0010ffe9\U0010ffea\U0010ffeb\U0010ffec\U0010ffed\U0010ffee\U0010ffef\U0010fff0\U0010fff1\U0010fff2\U0010fff3\U0010fff4\U0010fff5\U0010fff6\U0010fff7\U0010fff8\U0010fff9\U0010fffa\U0010fffb\U0010fffc\U0010fffd\U0010fffe',
    ]
)
