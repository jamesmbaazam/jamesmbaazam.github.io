"""Three typical shapes and how to read them."""
from common import *
from sklearn.metrics import precision_recall_curve

fig, axs = plt.subplots(1, 3, figsize=(13, 4.6), sharey=True)
# 1 steep decline: hard problem
r, p, *_ = analytic_pr(0.05, 1.2); axs[0].plot(r, p, color=BLUE)
axs[0].set_title("Steep decline"); axs[0].text(0.3, 0.55, "Each extra bit of recall\ncosts many false alarms", color=MUTED)
# 2 plateau: easy subset + hard remainder (mixture of positives)
rng = np.random.default_rng(1)
n, prev = 100_000, 0.05
y = (rng.random(n) < prev).astype(int)
easy = rng.random(n) < 0.6
s = rng.normal(0, 1, n) + y * np.where(easy, 6, 1.2)
p2, r2, _ = precision_recall_curve(y, s); axs[1].plot(r2, p2, color=ORANGE)
axs[1].set_title("High plateau, then a cliff"); axs[1].text(0.05, 0.45, "Some positives are cleanly\nseparable; the rest are not", color=MUTED)
axs[1].axvspan(0, 0.58, color=ORANGE, alpha=0.08, lw=0)
# 3 jagged left edge: few positives
y3, s3 = make_scores(0.002, 2.2, n=20_000, seed=3)
p3, r3, _ = precision_recall_curve(y3, s3); axs[2].plot(r3, p3, color=AQUA, lw=1.6)
axs[2].set_title("Jagged left edge"); axs[2].text(0.3, 0.55, "Top-scored predictions are\nfew; one error swings precision", color=MUTED)
axs[2].annotate("noisy", (0.065, 0.74), (0.2, 0.85), arrowprops=dict(arrowstyle="->", color=MUTED), color=MUTED)
for a in axs: a.set(xlabel="Recall", ylim=(0, 1.02), xlim=(0, 1))
axs[0].set_ylabel("Precision")
titled(fig, "Reading the shape of the curve", "Not guaranteed monotonic. Don't over-read the far left.")
finish(fig)
save(fig, "04_curve_shapes.png")
