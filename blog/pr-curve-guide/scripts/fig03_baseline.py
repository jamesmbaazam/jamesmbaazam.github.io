"""The baseline is the prevalence, not 0.5."""
from common import *

d = 2.0
fig, ax = plt.subplots(figsize=(8, 5.4))
for prev, c in zip([0.01, 0.10, 0.50], CAT):
    r, p, *_ = analytic_pr(prev, d)
    ax.plot(r, p, color=c)
    ax.axhline(prev, color=c, ls="--", lw=1.2)
    ax.text(0.02, prev + 0.015, f"random baseline {prev:.0%}", color=c, fontsize=10, fontweight="bold")
    ax.text(0.6, np.interp(0.6, r[::-1], p[::-1]) + 0.03, f"{prev:.0%} positives", color=c, fontweight="bold")
ax.set(xlim=(0, 1), ylim=(0, 1.02), xlabel="Recall", ylabel="Precision")
ax.set_xlim(0, 1); ax.set_xticks(np.arange(0, 1.01, 0.2))
titled(fig, "A random classifier sits at the prevalence, not 0.5",
       "Identical classifier quality (separation d=2). Only the class balance changes.")
finish(fig)
save(fig, "03_baseline_is_prevalence.png")
