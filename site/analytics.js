/* Google Analytics 4 for the Loka Context Harness page (property "Loka Context Harness",
   G-2XTTZLT5BD). gtag.js is fetched after the page has loaded so it never delays the first
   paint; calls made earlier queue in dataLayer.

   Events (link_location = the page section the click came from):
     repo_click     any link into the GitHub repository   link_url = path in the repo  (key event)
     demo_play      the demo video started (once per page view)
     demo_complete  the demo video reached the end
     demo_download  the MP4 fallback link
     prompt_copy    a Copy button                          copy_target                 */
(function () {
  var ID = 'G-2XTTZLT5BD';
  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag('js', new Date());
  gtag('config', ID);
  function load() {
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + ID;
    document.head.appendChild(s);
  }
  if (document.readyState === 'complete') setTimeout(load, 0);
  else addEventListener('load', function () { setTimeout(load, 0); }, { once: true });

  var REPO = /^https:\/\/github\.com\/Wazifati\/loka-context-harness(\/.*)?$/;
  function where(el) {
    if (el.closest('footer')) return 'footer';
    if (el.closest('header')) return 'header';
    var sec = el.closest('section[id], [id]');
    return sec && sec.id ? sec.id : 'page';
  }
  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('a[href], [data-copy-target]');
    if (!t) return;
    if (t.matches('[data-copy-target]')) { gtag('event', 'prompt_copy', { copy_target: t.dataset.copyTarget, link_location: where(t) }); return; }
    var m = t.href.match(REPO);
    if (m) {
      /* The release workflow pins /blob/main/ to a commit; report the file, not the commit. */
      var path = (m[1] || '/').replace(/^\/(blob|tree)\/[^/]+/, '') || '/';
      gtag('event', 'repo_click', { link_url: path, link_location: where(t) });
    } else if (/\.mp4($|\?)/.test(t.href)) {
      gtag('event', 'demo_download', { link_location: where(t) });
    }
  }, true);

  var video = document.querySelector('.demo-player video');
  if (video) {
    video.addEventListener('play', function () { gtag('event', 'demo_play'); }, { once: true });
    video.addEventListener('ended', function () { gtag('event', 'demo_complete'); });
  }
})();
