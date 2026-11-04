"""If production prevalence differs from eval, recall holds but precision moves."""
from common import *

d, t = 2.4, 1.6
prevs = np.logspace(-3, np.log10(0.5), 200)
rec = 1 - norm.cdf(t - d); fpr = 1 - norm.cdf(t)
prec = prevs * rec / (prevs * rec + (1 - prevs) * fpr)

fig, ax = plt.subplots(figsize=(8.5, 5.2))
ax.plot(prevs, prec, color=ORANGE); ax.axhline(rec, color=BLUE)
ax.text(0.0011, rec + 0.02, f"Recall stays at {rec:.0%}", color=BLUE, fontweight="bold")
ax.text(0.0011, 0.2, "Precision depends on\nclass balance", color=ORANGE, fontweight="bold")
ax.set_xscale("log"); ax.set(xlabel="Positive rate in the data (log scale)", ylabel="Metric", ylim=(0, 1.02))
ax.xaxis.set_major_formatter(mpl.ticker.PercentFormatter(1.0, decimals=1))
for pv, lab in [(0.02, "eval set"), (0.002, "production")]:
    ax.axvline(pv, color=MUTED, ls=":", lw=1.2); ax.text(pv * 1.05, 0.02, lab, color=MUTED, fontsize=10)
titled(fig, "Same model, same threshold, different prevalence", "Undersampled your negatives? Re-weight precision by the true prior.")
finish(fig)
save(fig, "07_prevalence_shift.png")
