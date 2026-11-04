"""Undersampling negatives inflates predicted probabilities."""
from common import *
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import calibration_curve

y, s = make_scores(0.02, 2.0, n=200_000, seed=5)
s = s.reshape(-1, 1)
natural = LogisticRegression().fit(s, y)
rng = np.random.default_rng(0)
keep = (y == 1) | (rng.random(len(y)) < 0.05)         # keep 5% of negatives
under = LogisticRegression().fit(s[keep], y[keep])
y_t, s_t = make_scores(0.02, 2.0, n=200_000, seed=99); s_t = s_t.reshape(-1, 1)

fig, ax = plt.subplots(figsize=(6.8, 6))
ax.plot([0, 0.85], [0, 0.85], color=MUTED, ls="--", lw=1.2)
for m, c, lab in [(natural, BLUE, "Trained on natural data"), (under, ORANGE, "Trained after undersampling")]:
    pr = m.predict_proba(s_t)[:, 1]
    fp_, mp_ = calibration_curve(y_t, pr, n_bins=15, strategy="quantile")
    ax.plot(mp_, fp_, "o-", color=c, label=lab, markersize=6)
ax.set(xlabel="Predicted probability", ylabel="Observed fraction positive", xlim=(0, 0.85), ylim=(0, 0.85))
ax.set_aspect("equal"); ax.legend(loc="upper left")
titled(fig, "Resampling distorts probabilities", "Thresholds from a resampled set won't transfer. Evaluate on the natural distribution.")
finish(fig)
save(fig, "08_resampling_calibration.png")
