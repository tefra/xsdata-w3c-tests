from output.models.saxon_data.xml_versions.xv100_i_xsd.xv100_i import Doc


obj = Doc(
    e=[
        ':',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '_',
        'abcdefghijklmnopqrstuvwxyz',
        'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ',
        'ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö',
        'øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜʛʜʝʞʟʠʡʢʣʤʥʦʧʨʩʪʫʬʭʮʯʰʱʲʳʴʵʶʷʸʹʺʻʼʽʾʿˀˁ˂˃˄˅ˆˇˈˉˊˋˌˍˎˏːˑ˒˓˔˕˖˗˘˙˚˛˜˝˞˟ˠˡˢˣˤ˥˦˧˨˩˪˫ˬ˭ˮ˯˰˱˲˳˴˵˶˷˸˹˺˻˼˽˾˿',
        'ͰͱͲͳʹ͵Ͷͷ\u0378\u0379ͺͻͼͽ',
        'Ϳ\u0380\u0381\u0382\u0383΄΅Ά·ΈΉΊ\u038bΌ\u038dΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡ\u03a2ΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώϏϐϑϒϓϔϕϖϗϘϙϚϛϜϝϞϟϠϡϢϣᾛᾜᾝᾞᾟᾠᾡᾢᾣᾤᾥᾦᾧᾨᾩᾪᾫᾬᾭᾮᾯᾰᾱᾲᾳᾴ\u1fb5ᾶᾷᾸᾹᾺΆᾼ᾽ι᾿῀῁ῂῃῄ\u1fc5ῆῇῈΈῊΉῌ῍῎῏ῐῑῒΐ\u1fd4\u1fd5ῖῗῘῙῚΊ\u1fdc῝῞῟ῠῡῢΰῤῥῦῧῨῩῪΎῬ῭΅`\u1ff0\u1ff1ῲῳῴ\u1ff5ῶῷῸΌῺΏῼ´῾\u1fff',
        '\u200c\u200d',
        '⁰ⁱ\u2072\u2073⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎\u208fₐₑₒₓₔₕₖₗₘₙₚₛₜ\u209d\u209e\u209f₠₡₢₣₤₥₦₧₨₩₪₫€₭₮₯₰₱₲₳₴₵₶₷₸₹₺₻₼₽₾₿⃀\u20c1\u20c2\u20c3\u20c4\u20c5\u20c6\u20c7\u20c8\u20c9\u20ca\u20cb\u20cc\u20cd\u20ce\u20cf⃒⃓⃐⃑⃔Åℬℭ℮ℯℰℱℲℳℴℵℶℷℸℹ℺℻ℼℽℾℿ⅀⅁⅂⅃⅄ⅅⅆⅇⅈⅉ⅊⅋⅌⅍ⅎ⅏⅐⅑⅒⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫⅬⅭⅮⅯⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻⅼⅽⅾⅿↀↁↂↃↄↅↆↇↈ↉↊↋\u218c\u218d\u218e\u218f',
        'ⰀⰁⰂⰃⰄⰅⰆⰇⰈⰉⰊⰋⰌⰍⰎⰏⰐⰑⰒⰓⰔⰕⰖⰗⰘⰙⰚⰛⰜⰝⰞⰟⰠⰡⰢⰣⰤⰥⰦⰧⰨⰩⰪⰫⰬⰭⰮⰯⰰⰱⰲⰳⰴⰵⰶⰷⰸⰹⰺⰻⰼⰽⰾⰿⱀⱁⱂⱃⱄⱅⱆⱇⱈⱉⱊⱋⱌⱍⱎⱏⱐⱑⱒⱓⱔⱕⱖⱗⱘⱙⱚⱛⱜⱝⱞⱟⱠⱡⱢⱣⱤ⾋⾌⾍⾎⾏⾐⾑⾒⾓⾔⾕⾖⾗⾘⾙⾚⾛⾜⾝⾞⾟⾠⾡⾢⾣⾤⾥⾦⾧⾨⾩⾪⾫⾬⾭⾮⾯⾰⾱⾲⾳⾴⾵⾶⾷⾸⾹⾺⾻⾼⾽⾾⾿⿀⿁⿂⿃⿄⿅⿆⿇⿈⿉⿊⿋⿌⿍⿎⿏⿐⿑⿒⿓⿔⿕\u2fd6\u2fd7\u2fd8\u2fd9\u2fda\u2fdb\u2fdc\u2fdd\u2fde\u2fdf\u2fe0\u2fe1\u2fe2\u2fe3\u2fe4\u2fe5\u2fe6\u2fe7\u2fe8\u2fe9\u2fea\u2feb\u2fec\u2fed\u2fee\u2fef',
        '、。〃〄々〆〇〈〉《》「」『』【】〒〓〔〕〖〗〘〙〚〛〜〝〞〟〠〡〢〣〤〥〦〧〨〩〪〭〮〯〫〬〰〱〲〳〴〵〶〷〸〹〺〻〼〽〾〿\u3040ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづ힛힜힝힞힟힠힡힢힣\ud7a4\ud7a5\ud7a6\ud7a7\ud7a8\ud7a9\ud7aa\ud7ab\ud7ac\ud7ad\ud7ae\ud7afힰힱힲힳힴힵힶힷힸힹힺힻힼힽힾힿퟀퟁퟂퟃퟄퟅퟆ\ud7c7\ud7c8\ud7c9\ud7caퟋퟌퟍퟎퟏퟐퟑퟒퟓퟔퟕퟖퟗퟘퟙퟚퟛퟜퟝퟞퟟퟠퟡퟢퟣퟤퟥퟦퟧퟨퟩퟪퟫퟬퟭퟮퟯퟰퟱퟲퟳퟴퟵퟶퟷퟸퟹퟺퟻ\ud7fc\ud7fd\ud7fe\ud7ff',
        '豈更車賈滑串句龜龜契金喇奈懶癩羅蘿螺裸邏樂洛烙珞落酪駱亂卵欄爛蘭鸞嵐濫藍襤拉臘蠟廊朗浪狼郎來冷勞擄櫓爐盧老蘆虜路露魯鷺碌祿綠菉錄鹿論壟弄籠聾牢磊賂雷壘屢樓淚漏累縷陋勒肋凜凌稜綾菱陵讀拏樂諾丹寧怒率異北磻ﵫﵬﵭﵮﵯﵰﵱﵲﵳﵴﵵﵶﵷﵸﵹﵺﵻﵼﵽﵾﵿﶀﶁﶂﶃﶄﶅﶆﶇﶈﶉﶊﶋﶌﶍﶎﶏ\ufd90\ufd91ﶒﶓﶔﶕﶖﶗﶘﶙﶚﶛﶜﶝﶞﶟﶠﶡﶢﶣﶤﶥﶦﶧﶨﶩﶪﶫﶬﶭﶮﶯﶰﶱﶲﶳﶴﶵﶶﶷﶸﶹﶺﶻﶼﶽﶾﶿﷀﷁﷂﷃﷄﷅﷆﷇ\ufdc8\ufdc9\ufdca\ufdcb\ufdcc\ufdcd\ufdce﷏',
        'ﷰﷱﷲﷳﷴﷵﷶﷷﷸﷹﷺﷻ﷼﷽﷾﷿︀︁︂︃︄︅︆︇︈︉︊︋︌︍︎️︐︑︒︓︔︕︖︗︘︙\ufe1a\ufe1b\ufe1c\ufe1d\ufe1e\ufe1f︧︨︩︪︫︬︭︠︡︢︣︤︥︦︮︯︰︱︲︳︴︵︶︷︸︹︺︻︼︽︾︿﹀﹁﹂﹃﹄﹅﹆﹇﹈﹉﹊﹋﹌﹍﹎﹏﹐﹑﹒\ufe53﹔ﾙﾚﾛﾜﾝﾞﾟﾠﾡﾢﾣﾤﾥﾦﾧﾨﾩﾪﾫﾬﾭﾮﾯﾰﾱﾲﾳﾴﾵﾶﾷﾸﾹﾺﾻﾼﾽﾾ\uffbf\uffc0\uffc1ￂￃￄￅￆￇ\uffc8\uffc9ￊￋￌￍￎￏ\uffd0\uffd1ￒￓￔￕￖￗ\uffd8\uffd9ￚￛￜ\uffdd\uffde\uffdf￠￡￢￣￤￥￦\uffe7￨￩￪￫￬￭￮\uffef\ufff0\ufff1\ufff2\ufff3\ufff4\ufff5\ufff6\ufff7\ufff8\ufff9\ufffa\ufffb￼�',
        '𐀀𐀁𐀂𐀃𐀄𐀅𐀆𐀇𐀈𐀉𐀊𐀋\U0001000c𐀍𐀎𐀏𐀐𐀑𐀒𐀓𐀔𐀕𐀖𐀗𐀘𐀙𐀚𐀛𐀜𐀝𐀞𐀟𐀠𐀡𐀢𐀣𐀤𐀥𐀦\U00010027𐀨𐀩𐀪𐀫𐀬𐀭𐀮𐀯𐀰𐀱𐀲𐀳𐀴𐀵𐀶𐀷𐀸𐀹𐀺\U0001003b𐀼𐀽\U0001003e𐀿𐁀𐁁𐁂𐁃𐁄𐁅𐁆𐁇𐁈𐁉𐁊𐁋𐁌𐁍\U0001004e\U0001004f𐁐𐁑𐁒𐁓𐁔𐁕𐁖𐁗𐁘𐁙𐁚𐁛𐁜𐁝\U0001005e\U0001005f\U00010060\U00010061\U00010062\U00010063\U00010064\U000eff9b\U000eff9c\U000eff9d\U000eff9e\U000eff9f\U000effa0\U000effa1\U000effa2\U000effa3\U000effa4\U000effa5\U000effa6\U000effa7\U000effa8\U000effa9\U000effaa\U000effab\U000effac\U000effad\U000effae\U000effaf\U000effb0\U000effb1\U000effb2\U000effb3\U000effb4\U000effb5\U000effb6\U000effb7\U000effb8\U000effb9\U000effba\U000effbb\U000effbc\U000effbd\U000effbe\U000effbf\U000effc0\U000effc1\U000effc2\U000effc3\U000effc4\U000effc5\U000effc6\U000effc7\U000effc8\U000effc9\U000effca\U000effcb\U000effcc\U000effcd\U000effce\U000effcf\U000effd0\U000effd1\U000effd2\U000effd3\U000effd4\U000effd5\U000effd6\U000effd7\U000effd8\U000effd9\U000effda\U000effdb\U000effdc\U000effdd\U000effde\U000effdf\U000effe0\U000effe1\U000effe2\U000effe3\U000effe4\U000effe5\U000effe6\U000effe7\U000effe8\U000effe9\U000effea\U000effeb\U000effec\U000effed\U000effee\U000effef\U000efff0\U000efff1\U000efff2\U000efff3\U000efff4\U000efff5\U000efff6\U000efff7\U000efff8\U000efff9\U000efffa\U000efffb\U000efffc\U000efffd\U000efffe\U000effff',
    ]
)
