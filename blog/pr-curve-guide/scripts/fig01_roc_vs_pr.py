"""Same model, 1% positives: ROC looks great, PR tells the truth."""
from common import *
from sklearn.metrics import roc_curve, roc_auc_score, precision_recall_curve, average_precision_score

y, s = make_scores(prevalence=0.01, d=2.5)
fpr, tpr, _ = roc_curve(y, s)
p, r, _ = precision_recall_curve(y, s)
auc, ap = roc_auc_score(y, s), average_precision_score(y, s)

fig, (a, b) = plt.subplots(1, 2, figsize=(11, 5))
a.plot(fpr, tpr, color=BLUE); a.plot([0, 1], [0, 1], color=MUTED, ls="--", lw=1.2)
a.set(title="ROC curve", xlabel="False positive rate", ylabel="Recall (true positive rate)")
a.text(0.5, 0.25, f"AUC = {auc:.2f}\n\"Excellent!\"", color=BLUE, fontsize=13, fontweight="bold")
b.plot(r, p, color=ORANGE); b.axhline(0.01, color=MUTED, ls="--", lw=1.2)
b.set(title="Precision-recall curve", xlabel="Recall", ylabel="Precision", ylim=(0, 1.02))
b.text(0.5, 0.5, f"AP = {ap:.2f}\n\"Wait, many alerts are wrong\"", color=ORANGE, fontsize=13, fontweight="bold")
b.text(0.02, 0.03, "random baseline = 1%", color=MUTED, fontsize=10)
titled(fig, "Same model, same data, very different story", "1% positives. ROC hides the false-alarm cost; PR exposes it.")
finish(fig)
save(fig, "01_roc_vs_pr.png")
