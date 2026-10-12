# Wreath math

Bundles of greenery for the frame, meters of ribbon for the bow, and what a wreath costs to make against its selling price. Exact arithmetic in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/wreathmath/

## The three tools

- **Frame plan** - `framePlan(diameterCm, coverPerBundleCm)`: circumference and bundles of greenery.
- **Ribbon plan** - `ribbonPlan(loops, loopLenCm, tailLenCm)`: centimeters of ribbon and meters to buy.
- **Cost plan** - `costPlan(framePriceDollars, bundles, bundlePriceDollars, ribbonPriceDollars, sellPriceDollars)`: cost to make and margin per wreath.

## Labeled norms (illustrative estimates, not rules)

- Labeled circumference: 3.1416 times the diameter. Labeled coverage: one bundle covers about 25 cm of frame. Prices are your own inputs; the craft stall's tags win.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (12 cases, 54 checks)

Regenerate the oracle expectations: `python3 oracle.py`
