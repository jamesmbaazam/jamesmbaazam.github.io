"""Step-wise AP vs optimistic trapezoid AUC."""
from common import *
from sklearn.metrics import precision_recall_curve, average_precision_score, auc

y, s = make_scores(0.1, 1.3, n=60, seed=7)
p, r, _ = precision_recall_curve(y, s)
ap, trap = average_precision_score(y, s), auc(r, p)

fig, ax = plt.subplots(figsize=(8, 5.2))
ax.step(r, p, where="post", color=BLUE, label=f"Step-wise (average_precision_score) = {ap:.3f}")
ax.fill_between(r, p, step="post", color=BLUE, alpha=0.12, lw=0)
ax.plot(r, p, color=ORANGE, ls="--", lw=1.8, label=f"Trapezoid auc(recall, precision) = {trap:.3f}")
ax.set(xlabel="Recall", ylabel="Precision", xlim=(0, 1), ylim=(0, 1.05))
ax.legend(loc="lower left")
titled(fig, "Prefer step-wise average precision", "Straight lines between PR points aren't achievable, so the trapezoid is a biased estimate (here lower; it can also run high).")
finish(fig)
save(fig, "05_ap_vs_trapezoid.png")
print(f"AP={ap:.3f} trapezoid={trap:.3f}")
