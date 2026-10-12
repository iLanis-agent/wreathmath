(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function money(c) { return "$" + Math.floor(c / 100) + "." + ("0" + (c % 100)).slice(-2); }

  function framePlan(diameterCm, coverPerBundleCm) {
    if (!(diameterCm > 0) || !(coverPerBundleCm > 0)) return { error: "frame diameter and bundle coverage must be positive" };
    var circ = diameterCm * 3.1416;
    var bundles = Math.ceil(circ / coverPerBundleCm);
    var shown = Math.round(circ * 10) / 10;
    return { circ: shown, bundles: bundles };
  }

  function ribbonPlan(loops, loopLenCm, tailLenCm) {
    if (!(loops > 0) || !(loopLenCm > 0) || !(tailLenCm > 0)) return { error: "loops, loop length and tails must be positive" };
    var total = 2 * loops * loopLenCm + tailLenCm;
    var buyM = Math.ceil(total / 100);
    return { total: total, buyM: buyM };
  }

  function costPlan(framePriceDollars, bundles, bundlePriceDollars, ribbonPriceDollars, sellPriceDollars) {
    if (!(framePriceDollars > 0) || !(bundles > 0) || !(bundlePriceDollars > 0) || !(ribbonPriceDollars > 0) || !(sellPriceDollars > 0)) return { error: "prices and bundles must be positive" };
    var frameCents = Math.round(framePriceDollars * 100);
    var bundleCents = Math.round(bundles * bundlePriceDollars * 100);
    var ribbonCents = Math.round(ribbonPriceDollars * 100);
    var costCents = frameCents + bundleCents + ribbonCents;
    var sellCents = Math.round(sellPriceDollars * 100);
    return { costCents: costCents, sellCents: sellCents, marginCents: sellCents - costCents };
  }

  function renderFrame(r, diameterCm, coverPerBundleCm) {
    return "A " + diameterCm + " cm frame runs about " + r.circ + " cm around - at a labeled " + coverPerBundleCm + " cm of coverage a bundle, " + plural(r.bundles, "bundle") + " of greenery.";
  }

  function renderRibbon(r, loops, loopLenCm, tailLenCm) {
    return "A bow of " + plural(loops, "loop") + " at " + loopLenCm + " cm with " + tailLenCm + " cm of tails: " + r.total + " cm of ribbon - buy " + plural(r.buyM, "meter", "meters") + ".";
  }

  function renderCost(r, framePriceDollars, bundles, bundlePriceDollars, ribbonPriceDollars, sellPriceDollars) {
    return money(Math.round(framePriceDollars * 100)) + " for the frame, " + plural(bundles, "bundle") + " at " + money(Math.round(bundlePriceDollars * 100)) + " and " + money(Math.round(ribbonPriceDollars * 100)) + " of ribbon: " + money(r.costCents) + " to make. At " + money(r.sellCents) + " a wreath that leaves " + money(r.marginCents) + " a piece.";
  }

  var api = { framePlan: framePlan, ribbonPlan: ribbonPlan, costPlan: costPlan, renderFrame: renderFrame, renderRibbon: renderRibbon, renderCost: renderCost };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.WreathMath = api;
})(this);
