import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def money(c): return "$" + str(c // 100) + "." + str(c % 100).zfill(2)
def fmt(x): return str(jsnum(x))
def rnd(x): return math.floor(x + 0.5)

def frame_plan(diameterCm, coverPerBundleCm):
    if not (diameterCm > 0) or not (coverPerBundleCm > 0):
        return {"error": "frame diameter and bundle coverage must be positive"}
    circ = diameterCm * 3.1416
    return {"circ": jsnum(rnd(circ * 10) / 10), "bundles": math.ceil(circ / coverPerBundleCm)}

def ribbon_plan(loops, loopLenCm, tailLenCm):
    if not (loops > 0) or not (loopLenCm > 0) or not (tailLenCm > 0):
        return {"error": "loops, loop length and tails must be positive"}
    total = 2 * loops * loopLenCm + tailLenCm
    return {"total": jsnum(total), "buyM": math.ceil(total / 100)}

def cost_plan(framePriceDollars, bundles, bundlePriceDollars, ribbonPriceDollars, sellPriceDollars):
    if not (framePriceDollars > 0) or not (bundles > 0) or not (bundlePriceDollars > 0) or not (ribbonPriceDollars > 0) or not (sellPriceDollars > 0):
        return {"error": "prices and bundles must be positive"}
    cost = rnd(framePriceDollars * 100) + rnd(bundles * bundlePriceDollars * 100) + rnd(ribbonPriceDollars * 100)
    sell = rnd(sellPriceDollars * 100)
    return {"costCents": cost, "sellCents": sell, "marginCents": sell - cost}

def render_frame(r, diameterCm, coverPerBundleCm):
    return ("A " + fmt(diameterCm) + " cm frame runs about " + fmt(r["circ"]) + " cm around - at a labeled "
            + fmt(coverPerBundleCm) + " cm of coverage a bundle, " + plural(r["bundles"], "bundle") + " of greenery.")

def render_ribbon(r, loops, loopLenCm, tailLenCm):
    return ("A bow of " + plural(loops, "loop") + " at " + fmt(loopLenCm) + " cm with " + fmt(tailLenCm)
            + " cm of tails: " + fmt(r["total"]) + " cm of ribbon - buy " + plural(r["buyM"], "meter", "meters") + ".")

def render_cost(r, framePriceDollars, bundles, bundlePriceDollars, ribbonPriceDollars, sellPriceDollars):
    return (money(rnd(framePriceDollars * 100)) + " for the frame, " + plural(bundles, "bundle") + " at "
            + money(rnd(bundlePriceDollars * 100)) + " and " + money(rnd(ribbonPriceDollars * 100)) + " of ribbon: "
            + money(r["costCents"]) + " to make. At " + money(r["sellCents"]) + " a wreath that leaves "
            + money(r["marginCents"]) + " a piece.")

cases = []
for a in [(30, 25), (45, 30), (25, 20), (0, 25)]:
    r = frame_plan(*a)
    cases.append({"fn": "framePlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_frame(r, *a)})
for a in [(6, 12, 30), (8, 15, 40), (4, 10, 25), (0, 12, 30)]:
    r = ribbon_plan(*a)
    cases.append({"fn": "ribbonPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_ribbon(r, *a)})
for a in [(4, 4, 3, 2.5, 45), (6, 5, 3.5, 3, 60), (5, 3, 4, 2, 35), (0, 4, 3, 2.5, 45)]:
    r = cost_plan(*a)
    cases.append({"fn": "costPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_cost(r, *a)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
