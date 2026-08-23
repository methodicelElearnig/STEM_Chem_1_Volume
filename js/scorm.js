/* =====================================================================
   Minimal SCORM 1.2 run-time wrapper (matches the example package:
   ADL SCORM 1.2, mastery score 80). Safe no-op when opened outside an LMS.
   ===================================================================== */
window.SCORM = (function () {
  'use strict';
  var api = null, ready = false;

  function findAPI(win) {
    var tries = 0;
    while (win && !win.API && win.parent && win.parent !== win && tries < 12) {
      win = win.parent; tries++;
    }
    return (win && win.API) ? win.API : null;
  }
  function getAPI() {
    var a = findAPI(window);
    if (!a && window.opener) a = findAPI(window.opener);
    return a;
  }

  return {
    init: function () {
      api = getAPI();
      if (!api) return false;                     // not in an LMS — stay a no-op
      ready = (api.LMSInitialize('') === 'true');
      if (ready) {
        if (api.LMSGetValue('cmi.core.lesson_status') === 'not attempted')
          api.LMSSetValue('cmi.core.lesson_status', 'incomplete');
        api.LMSSetValue('cmi.core.score.min', '0');
        api.LMSSetValue('cmi.core.score.max', '100');
        api.LMSCommit('');
      }
      return ready;
    },
    setScore: function (raw) {
      if (!ready) return;
      api.LMSSetValue('cmi.core.score.raw', String(Math.round(raw)));
      api.LMSCommit('');
    },
    complete: function (raw, mastery) {
      if (!ready) return;
      api.LMSSetValue('cmi.core.score.raw', String(Math.round(raw)));
      api.LMSSetValue('cmi.core.lesson_status', raw >= mastery ? 'passed' : 'failed');
      api.LMSCommit('');
    },
    finish: function () {
      if (!ready) return;
      api.LMSFinish('');
      ready = false;
    }
  };
})();

window.addEventListener('load', function () { window.SCORM.init(); });
window.addEventListener('unload', function () { window.SCORM.finish(); });
