"""Shared helpers: synthetic data, plot style, saving."""
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import norm

FIG_DIR = Path(__file__).resolve().parent.parent / "figures"
FIG_DIR.mkdir(exist_ok=True)

# Colours (validated categorical slots 1-3 + neutrals)
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"
CAT = [BLUE, ORANGE, AQUA]


def style():
    mpl.rcParams.update({
        "figure.facecolor": "white", "axes.facecolor": "white",
        "savefig.facecolor": "white", "figure.dpi": 100, "savefig.dpi": 150,
        "font.size": 11, "axes.edgecolor": MUTED, "axes.labelcolor": MUTED,
        "xtick.color": MUTED, "ytick.color": MUTED, "text.color": INK,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
        "axes.axisbelow": True, "axes.titlesize": 13, "axes.titleweight": "bold",
        "axes.titlelocation": "left", "lines.linewidth": 2.2,
        "legend.frameon": False,
    })


style()


def make_scores(prevalence=0.01, d=2.0, n=200_000, seed=0):
    """Binormal toy model: negatives ~ N(0,1), positives ~ N(d,1).
    d controls how separable the classes are (higher = easier)."""
    rng = np.random.default_rng(seed)
    y = (rng.random(n) < prevalence).astype(int)
    s = rng.normal(0, 1, n) + d * y
    return y, s


def analytic_pr(prevalence, d, grid=None):
    """Exact PR curve of the binormal model (no sampling noise)."""
    t = np.linspace(-3, d + 4, 800) if grid is None else grid
    rec = 1 - norm.cdf(t - d)
    fpr = 1 - norm.cdf(t)
    tp, fp = prevalence * rec, (1 - prevalence) * fpr
    prec = np.where(tp + fp > 0, tp / (tp + fp + 1e-300), 1.0)
    return rec, prec, fpr, t


def titled(fig, title, subtitle=None):
    """Title + subtitle laid out in absolute inches so they never overlap."""
    h = fig.get_figheight()
    fig.text(0.005, 1 - 0.10 / h, title, ha="left", va="top", fontsize=15, fontweight="bold")
    if subtitle:
        fig.text(0.005, 1 - 0.45 / h, subtitle, ha="left", va="top", color=MUTED, fontsize=11)


def finish(fig):
    h = fig.get_figheight()
    fig.tight_layout(rect=(0, 0, 1, 1 - 0.85 / h))


def save(fig, name):
    path = FIG_DIR / name
    fig.savefig(path, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print("wrote", path.relative_to(FIG_DIR.parent))
