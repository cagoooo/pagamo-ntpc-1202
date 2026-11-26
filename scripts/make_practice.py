"""產生研習實作用的三篇自編短文頁（低／中／高年級）。用法：python scripts/make_practice.py
每篇各自一頁，擴充套件「讀取這頁全文」才只會讀到一篇；上方切換列放在 <article> 外面。"""
from pathlib import Path

ARTICLES = [
    {
        'file': 'practice-low.html', 'key': 'low', 'tab': '低年級', 'grade': '適合一、二年級',
        'title': '小番茄長大了', 'count': 5, 'level': '二年級',
        'paras': [
            '星期一，老師帶來一包小番茄種子。小葵和同學把種子放進小花盆裡，再輕輕蓋上一層土。',
            '老師說：「種子要喝水，也要曬太陽。」所以每天早上，小葵都會拿小水壺，幫花盆澆一點點水。',
            '過了五天，土裡冒出兩片小小的綠葉。小葵開心得跳了起來，馬上拉著好朋友小杰一起來看。',
            '有一天放學前，小杰把花盆搬到走廊玩，卻忘了搬回窗台。過了兩天，小番茄的葉子變得黃黃的，還垂了下來。小杰難過得說不出話，小葵拍拍他說：「沒關係，我們一起把它搬回有陽光的地方。」',
            '又過了幾個星期，小番茄開出黃色的小花，後來結出一顆顆綠色的果實。果實慢慢變紅了，全班一起數一數，一共有十二顆。',
            '小葵在畫圖日記上寫：「只要用心照顧，小小的種子也會長大。」',
        ],
    },
    {
        'file': 'practice.html', 'key': 'mid', 'tab': '中年級', 'grade': '適合三、四年級',
        'title': '雨水撲滿', 'count': 5, 'level': '四年級',
        'paras': [
            '星期一早上，四年三班的教室外多了一個藍色的大桶子。桶子上貼著一張紙，寫著「雨水撲滿，歡迎存水」。同學們圍在旁邊你一言我一語，猜不出這個桶子要做什麼。',
            '原來，這是自然老師和同學一起做的「雨水撲滿」。他們在屋簷下接了一條水管，下雨的時候，從屋頂流下來的雨水，會順著水管流進桶子裡。桶子上方蓋著細細的網子，可以擋住樹葉和小蟲；桶子下方裝了一個水龍頭，方便把水接出來。',
            '第一個星期連下了三天雨，桶子很快就裝了半桶水。值日生小安每天放學前，都會用尺量一量水有多高，再把數字寫在記錄表上。小安發現，雨下得越大，水位升得越快；可是連續好幾天出太陽，水位也會慢慢變低。',
            '這些雨水不能喝，但是用處很多。同學們用它來澆花、洗拖把，還用來沖洗走廊邊的洗手台。過了一個月，總務處的阿姨告訴大家，四年三班這個月用的自來水，比上個月少了一些。',
            '學期末，全班一起討論雨水撲滿還能怎麼改進。有人建議再多放一個桶子，有人想在桶子上畫圖，提醒大家節約用水。小安在記錄表的最後一行寫下：「每一滴雨水，都值得好好收藏。」',
        ],
    },
    {
        'file': 'practice-high.html', 'key': 'high', 'tab': '高年級', 'grade': '適合五、六年級',
        'title': '城市裡的蜜蜂旅館', 'count': 8, 'level': '六年級',
        'paras': [
            '走進學校的後花園，你會看到一個像書櫃的木頭架子，裡面塞滿了竹管、鑽了小洞的木塊和乾樹枝。這不是堆放雜物的架子，而是一間「蜜蜂旅館」，專門給野生的獨居蜂居住。',
            '一提到蜜蜂，很多人想到的是住在蜂箱裡、會釀蜂蜜的蜜蜂。其實世界上的蜂類有兩萬種左右，大部分不釀蜜，也不住在大蜂巢裡，而是各自尋找細小的洞穴產卵，所以被稱為「獨居蜂」。牠們在花朵之間飛來飛去時，身上沾滿花粉，順便幫植物完成授粉。我們吃的許多水果和蔬菜，都要靠這些小小的幫手才能結出果實。',
            '然而，城市裡到處是水泥地和修剪整齊的草坪，獨居蜂很難找到可以築巢的枯木和泥土，也不容易找到足夠的花。少了住的地方和食物，牠們自然越來越少見。',
            '六年甲班在自然課讀到這個問題後，決定動手幫忙。他們向家長募集用不到的竹筷和木塊，把竹管鋸成一樣的長度，再用砂紙把洞口磨平，以免割傷蜂的翅膀。旅館完成後，大家把它掛在朝東、淋不到雨的牆上，又在旁邊種了薰衣草和波斯菊。',
            '一開始，旅館整整一個月都沒有房客。有同學失望地說：「我們是不是做白工了？」老師請大家耐心觀察，每週記錄一次。到了第二個月，終於有幾根竹管的洞口被一團泥巴封了起來。老師解釋，這代表有蜂媽媽在裡面產了卵，再用泥土把門關好，保護裡面的寶寶。',
            '不過，也有人提出疑問。有幾位家長擔心蜂會螫人，希望把旅館搬到別的地方。六年甲班沒有急著反駁，而是查資料、做了一張說明海報：獨居蜂沒有要保護的大蜂巢，通常比較溫和，只要不去抓牠、不堵住洞口，就不容易被螫。他們還在旅館前拉了一條繩子，提醒大家保持一步的距離觀察。看過海報後，家長們同意讓旅館留下來。',
            '學期結束時，旅館裡已經有十多個房間住進了房客。班長在成果發表會上說：「我們沒有辦法讓整座城市都變成森林，但是可以替這些小小的幫手，留下一個角落。」台下的同學和家長都用力鼓掌。',
        ],
    },
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}｜研習實作用自編短文（{tab}）</title>
  <meta name="description" content="12/2 新北市教師研習實作用的自編短文〈{title}〉，約 {chars} 字、{grade}，用來練習 PIRLS 閱讀題組小幫手出題。" />
  <meta name="theme-color" content="#0c1014" />
  <link rel="icon" href="favicon.svg?v=__BUILD_VERSION__" type="image/svg+xml" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700;900&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet" />
  <style>
    :root {{ --bg: #f4f6f2; --ink: #1b2128; --muted: #5d6874; --line: #d9dfd6; --lime: #5d7c00; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; background: var(--bg); color: var(--ink); font-family: 'Noto Sans TC', 'Microsoft JhengHei', sans-serif; }}
    .bar {{ background: #0c1014; color: #eef2f5; padding: 12px 20px; font-size: 15px; display: flex; flex-wrap: wrap; gap: 10px 16px; align-items: center; justify-content: space-between; }}
    .bar b {{ color: #c6f432; font-family: 'JetBrains Mono', monospace; letter-spacing: .06em; }}
    .bar button {{ font: inherit; font-weight: 700; border: none; border-radius: 6px; padding: 7px 14px; background: #c6f432; color: #11151b; cursor: pointer; }}
    .grades {{ max-width: 760px; margin: 22px auto 0; padding: 0 20px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }}
    .grades a {{ display: block; text-decoration: none; color: var(--ink); background: #fff; border: 1px solid var(--line); border-radius: 10px; padding: 10px 14px; font-weight: 700; }}
    .grades a small {{ display: block; font-weight: 400; color: var(--muted); font-size: 13px; margin-top: 2px; }}
    .grades a:hover {{ border-color: var(--lime); }}
    .grades a.on {{ background: #0c1014; border-color: #0c1014; color: #c6f432; }}
    .grades a.on small {{ color: #c9d3db; }}
    main {{ max-width: 760px; margin: 0 auto; padding: 18px 20px 24px; }}
    article {{ background: #fff; border: 1px solid var(--line); border-radius: 12px; padding: 32px 36px; }}
    h1 {{ font-size: 34px; margin: 0 0 6px; }}
    .by {{ color: var(--muted); font-size: 15px; margin: 0 0 22px; }}
    article p {{ font-size: {fs}px; line-height: 2; margin: 0 0 16px; text-indent: 2em; }}
    .tips {{ margin-top: 22px; font-size: 15px; color: var(--muted); line-height: 1.8; }}
    footer {{ text-align: center; font-size: 14px; color: var(--muted); padding: 8px 16px 28px; }}
    footer a {{ color: var(--lime); }}
    @media (max-width: 600px) {{ article {{ padding: 22px 18px; }} article p {{ font-size: 18px; }} h1 {{ font-size: 28px; }} .grades {{ gap: 6px; }} .grades a {{ padding: 8px 10px; font-size: 15px; }} }}
  </style>
</head>
<body>
  <div class="bar">
    <span><b>PRACTICE</b>　研習實作用短文：按擴充套件的「📖 讀取這頁全文」出題</span>
    <button type="button" id="copy">📋 複製全文（改用「📝 文字」分頁貼上）</button>
  </div>
  <nav class="grades" aria-label="選擇年級">
{tabs}
  </nav>
  <main>
    <article id="story">
      <h1>{title}</h1>
      <p class="by">自編短文・約 {chars} 字・{grade}</p>
{paras}
    </article>
    <p class="tips">
      實作步驟：① 按工具列的 PIRLS 小幫手圖示 →「📖 讀取這頁全文」　② 題數選「{count} 題」、適讀年級可試試「{level}」　③ 按「✨ 開始出題」，看完題目再決定要不要送到 PaGamO。<br>
      這是講師自己寫的示範短文，可以自由用來練習出題。上方可以切換低、中、高年級的範本文章。
    </p>
  </main>
  <footer>
    Made with ❤️ by
    <a href="https://cagoooo.github.io/Akai/" target="_blank" rel="noopener noreferrer">阿凱老師</a>
    · 桃園市龍潭區石門國民小學
  </footer>
  <script>
    document.getElementById('copy').addEventListener('click', function () {{
      var el = document.getElementById('story');
      var text = el.querySelector('h1').textContent + '\\n\\n' +
        Array.prototype.map.call(el.querySelectorAll('p:not(.by)'), function (p) {{ return p.textContent; }}).join('\\n');
      var btn = this;
      var done = function (ok) {{ btn.textContent = ok ? '✓ 已複製，到工作台「📝 文字」貼上' : '複製失敗，請手動選取'; }};
      if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(function () {{ done(true); }}, function () {{ done(false); }});
      else done(false);
    }});
  </script>
</body>
</html>
'''

def chars(a):
    return sum(len(p) for p in a['paras'])

def rounded(n):
    return int(round(n / 50.0) * 50)

root = Path(__file__).resolve().parent.parent
for a in ARTICLES:
    def tab(b):
        cur = ' class="on" aria-current="page"' if b is a else ''
        return f'    <a href="{b["file"]}"{cur}>{b["tab"]}〈{b["title"]}〉<small>約 {rounded(chars(b))} 字・{b["grade"]}</small></a>'
    tabs = '\n'.join(tab(b) for b in ARTICLES)
    paras = '\n'.join(f'      <p>{p}</p>' for p in a['paras'])
    html = TEMPLATE.format(title=a['title'], tab=a['tab'], chars=rounded(chars(a)), grade=a['grade'], tabs=tabs,
                           paras=paras, count=a['count'], level=a['level'], fs=22 if a['key'] == 'low' else 20)
    (root / a['file']).write_text(html, encoding='utf-8')
    print(a['file'], a['title'], chars(a), '字 → 約', rounded(chars(a)))
