"""Why: with 10,000 cases and 1% positives, count what a threshold actually does."""
from common import *

N, prev, d = 10_000, 0.01, 2.5
t = 2.0                       # one chosen threshold
pos, neg = N * prev, N * (1 - prev)
tp = pos * (1 - norm.cdf(t - d)); fp = neg * (1 - norm.cdf(t))
recall, fpr, prec = tp / pos, fp / neg, tp / (tp + fp)

fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.8), gridspec_kw={"width_ratios": [1, 1.1]})
names = ["Recall", "False positive\nrate", "Precision"]
vals = [recall, fpr, prec]
bars = a.bar(names, vals, color=[BLUE, BLUE, ORANGE], width=0.55)
for bar, v in zip(bars, vals):
    a.text(bar.get_x() + bar.get_width() / 2, v + 0.02, f"{v:.0%}", ha="center", fontweight="bold")
a.set(ylim=(0, 1.05), title="One threshold, three metrics"); a.grid(axis="x", visible=False)

b.bar(["Real positives\ncaught (TP)", "False alarms\n(FP)"], [tp, fp], color=[BLUE, ORANGE], width=0.5)
for i, v in enumerate([tp, fp]):
    b.text(i, v + 2, f"{v:.0f}", ha="center", fontweight="bold")
b.set(title="What the alerts actually contain", ylabel="Cases flagged"); b.grid(axis="x", visible=False)
titled(fig, "The 9,900 negatives dilute the false positive rate",
       f"FPR looks tiny ({fpr:.0%}) but false alarms still outnumber hits, so precision is only {prec:.0%}.")
finish(fig)
save(fig, "02_why_roc_hides_fp.png")
