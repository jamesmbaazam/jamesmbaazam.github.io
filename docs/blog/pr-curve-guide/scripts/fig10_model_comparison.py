"""When curves cross, the 'better' model depends on your recall range."""
from common import *
from sklearn.metrics import precision_recall_curve, average_precision_score

rng = np.random.default_rng(4)
n, prev = 150_000, 0.03
y = (rng.random(n) < prev).astype(int)
# A: great on a subset of positives, weak on the rest. B: uniformly moderate.
sA = rng.normal(0, 1, n) + y * np.where(rng.random(n) < 0.5, 5, 0.6)
sB = rng.normal(0, 1, n) + y * 1.9
fig, ax = plt.subplots(figsize=(8.5, 5.4))
for s, c, nm in [(sA, BLUE, "Model A"), (sB, ORANGE, "Model B")]:
    p, r, _ = precision_recall_curve(y, s)
    ax.plot(r, p, color=c, label=f"{nm} (AP {average_precision_score(y, s):.2f})")
ax.axvspan(0, 0.55, color=BLUE, alpha=0.07, lw=0); ax.axvspan(0.55, 1, color=ORANGE, alpha=0.07, lw=0)
ax.text(0.02, 0.15, "A wins at\nlow recall", color=BLUE, fontweight="bold")
ax.text(0.7, 0.85, "B wins at\nhigh recall", color=ORANGE, fontweight="bold")
ax.set(xlabel="Recall", ylabel="Precision", xlim=(0, 1), ylim=(0, 1.02)); ax.legend(loc="center right")
titled(fig, "Crossing curves: one AP number hides the trade-off", "Pick the model for the recall range your use case lives in.")
finish(fig)
save(fig, "10_model_comparison.png")
