"""Few positives => noisy curve. Bootstrap bands show how much."""
from common import *
from sklearn.metrics import precision_recall_curve

grid = np.linspace(0.02, 1, 100)
def band(n_pos, seed):
    rng = np.random.default_rng(seed)
    curves = []
    for _ in range(200):
        n = int(n_pos / 0.02)
        y, s = make_scores(0.02, 2.2, n=n, seed=int(rng.integers(1e9)))
        p, r, _ = precision_recall_curve(y, s)
        order = np.argsort(r); curves.append(np.interp(grid, r[order], p[order]))
    return np.percentile(curves, [5, 50, 95], axis=0)

fig, axs = plt.subplots(1, 2, figsize=(11, 4.8), sharey=True)
for a, n_pos, c in zip(axs, [20, 500], [ORANGE, BLUE]):
    lo, mid, hi = band(n_pos, 1)
    a.fill_between(grid, lo, hi, color=c, alpha=0.2, lw=0); a.plot(grid, mid, color=c)
    a.set(title=f"{n_pos} positives", xlabel="Recall", xlim=(0, 1), ylim=(0, 1.02))
axs[0].set_ylabel("Precision")
titled(fig, "Few positives means a wobbly curve", "Median and 90% bootstrap band over 200 resamples. Report the number of positives.")
finish(fig)
save(fig, "09_small_sample_noise.png")
