"""Worked example at 2% prevalence: two operating points, in alert counts."""
from common import *

prev, d, N = 0.02, 2.42, 1000
pts = {}
for rec_t in (0.60, 0.85):
    t = d - norm.ppf(rec_t)
    tp = N * prev * rec_t; fp = N * (1 - prev) * (1 - norm.cdf(t))
    pts[rec_t] = (tp, fp, tp / (tp + fp))
r, p, *_ = analytic_pr(prev, d)

fig, (a, b) = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={"width_ratios": [1.1, 1]})
a.plot(r, p, color=BLUE); a.axhline(prev, color=MUTED, ls="--", lw=1.2)
a.text(0.02, prev + 0.02, "baseline 2%", color=MUTED, fontsize=10)
for (rt, (tp, fp, pr)), c in zip(pts.items(), [AQUA, ORANGE]):
    a.scatter([rt], [pr], s=80, color=c, zorder=5, edgecolor="white", linewidth=1.5)
    a.annotate(f"recall {rt:.0%}\nprecision {pr:.0%}", (rt, pr), (rt - 0.1, pr + 0.2), color=c, fontweight="bold",
               arrowprops=dict(arrowstyle="->", color=MUTED))
a.set(title="Two operating points", xlabel="Recall", ylabel="Precision", xlim=(0, 1), ylim=(0, 1.02))
x = np.arange(2); w = 0.36
b.bar(x - w / 2, [v[0] for v in pts.values()], w, color=BLUE, label="True positives")
b.bar(x + w / 2, [v[1] for v in pts.values()], w, color=ORANGE, label="False alarms")
for i, v in enumerate(pts.values()):
    b.text(i - w / 2, v[0] + 1, f"{v[0]:.0f}", ha="center", fontweight="bold")
    b.text(i + w / 2, v[1] + 1, f"{v[1]:.0f}", ha="center", fontweight="bold")
b.set_xticks(x, [f"Recall {k:.0%}" for k in pts]); b.set(title=f"Alerts per {N:,} cases", ylabel="Alerts"); b.legend(); b.grid(axis="x", visible=False)
titled(fig, "Same model, two thresholds, very different review workloads",
       "Which is acceptable depends on the cost of a miss vs. the cost of reviewing a false alarm.")
finish(fig)
save(fig, "11_worked_example.png")
for k, v in pts.items(): print(f"recall {k:.0%}: precision {v[2]:.1%}, TP {v[0]:.1f}, FP {v[1]:.1f}")
