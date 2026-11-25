/* 時程列：每段第一頁加 data-seg="代號|名稱|開始|結束"，之後的頁面沿用最近一段。
 * 左邊顯示目前段落，右邊顯示這段的預定時間、整場進度格、現在時間。
 * 現在時間落在 13:50–16:10 之間才判斷「準時／超時」（彩排時同一時段也看得到）。 */
(function () {
  var slides = Array.prototype.slice.call(document.querySelectorAll('.reveal .slides > section'));
  var segs = [];
  var cur = null;
  slides.forEach(function (sl) {
    if (sl.dataset.seg) {
      var p = sl.dataset.seg.split('|');
      cur = { mod: p[0], name: p[1], start: p[2], end: p[3], idx: segs.length };
      segs.push(cur);
    }
    sl._seg = cur;
  });
  var toMin = function (t) { var a = t.split(':'); return (+a[0]) * 60 + (+a[1]); };
  slides.forEach(function (sl) {
    var s = sl._seg;
    if (!s || sl.hasAttribute('data-nohud')) return;
    var hud = document.createElement('div');
    hud.className = 'hud';
    var bars = segs.map(function (g) {
      var w = Math.max(10, Math.round((toMin(g.end) - toMin(g.start)) * 3.2));
      var cls = g.idx < s.idx ? 'past' : (g.idx === s.idx ? 'cur' : '');
      return '<i class="' + cls + '" style="width:' + w + 'px" title="' + g.start + '–' + g.end + ' ' + g.name + '"></i>';
    }).join('');
    hud.innerHTML = '<span class="hud-mod">' + s.mod + '</span><span class="hud-name">' + s.name + '</span>' +
      '<span class="hud-segs" aria-hidden="true">' + bars + '</span>' +
      '<span class="hud-time">' + s.start + '–' + s.end + '</span><span class="hud-now" data-end="' + s.end + '" data-start="' + s.start + '"></span>';
    sl.insertBefore(hud, sl.firstChild);
  });
  function tick() {
    var d = new Date();
    var m = d.getHours() * 60 + d.getMinutes();
    var txt = 'NOW ' + String(d.getHours()).padStart(2, '0') + ':' + String(d.getMinutes()).padStart(2, '0');
    var live = m >= toMin('13:50') && m <= toMin('16:10');
    document.querySelectorAll('.hud-now').forEach(function (el) {
      el.textContent = txt;
      if (!live) { el.removeAttribute('data-st'); return; }
      el.dataset.st = m > toMin(el.dataset.end) ? 'late' : 'ok';
    });
  }
  tick();
  setInterval(tick, 15000);
})();
