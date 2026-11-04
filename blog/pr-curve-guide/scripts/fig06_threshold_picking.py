"""Pick a threshold from a recall (or precision) requirement, then check the other axis."""
from common import *
from sklearn.metrics import precision_recall_curve

y, s = make_scores(0.02, 2.4, n=300_000, seed=11)
p, r, th = precision_recall_curve(y, s)
target = 0.80
i = np.where(r[:-1] >= target)[0][-1]       # highest threshold with recall >= target
t_star, p_star, r_star = th[i], p[i], r[i]

fig, (a, b) = plt.subplots(1, 2, figsize=(12, 5))
a.plot(r, p, color=BLUE); a.axvline(target, color=MUTED, ls="--", lw=1.2)
a.scatter([r_star], [p_star], s=70, color=ORANGE, zorder=5, edgecolor="white", linewidth=1.5)
a.annotate(f"Need recall ≥ {target:.0%}\nprecision = {p_star:.0%}\nthreshold = {t_star:.2f}",
           (r_star, p_star), (0.42, 0.80), arrowprops=dict(arrowstyle="->", color=MUTED), fontweight="bold")
a.set(title="1. Find the point on the curve", xlabel="Recall", ylabel="Precision", xlim=(0, 1), ylim=(0, 1.02))
b.plot(th, p[:-1], color=ORANGE, label="Precision"); b.plot(th, r[:-1], color=BLUE, label="Recall")
b.axvline(t_star, color=MUTED, ls="--", lw=1.2)
b.set(title="2. Read off the threshold", xlabel="Decision threshold (score)", ylabel="Metric", xlim=(-1, 5), ylim=(0, 1.02))
b.legend(loc="center left")
titled(fig, "From a requirement to a threshold",
       "Then check the other axis, tune on validation data, and report on a held-out test set.")
finish(fig)
save(fig, "06_threshold_picking.png")
