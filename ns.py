"""
T-model alpha-attractor: Delta N_* and phi_*/M_Pl vs n_s,
with Planck 2018 and ACT DR6 + DESI BAO n_s posteriors shaded.

Project layout (parent folder):
    .venv/
    chains/
        planck2018/base_plikHM_TTTEEE_lowl_lowE_lensing/...
        act_dr6_desi_dr2/...
    packages/reheating/{chains.py, tmodel.py}
    plot_tmodel_ns.py        <- this file
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "packages"))

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.ticker import AutoMinorLocator
import numpy as np

from reheating.chains import load_ns_chain, posterior_summary
from reheating.tmodel import delta_N, phi_star

# ---------------- settings ----------------
planck_root = str(
    ROOT / "chains" / "planck2018"
    / "base_plikHM_TTTEEE_lowl_lowE_lensing"
    / "base_plikHM_TTTEEE_lowl_lowE_lensing"
)
# Must be a chain from the JOINT ACT DR6 + DESI BAO likelihood.
act_desi_root = str(ROOT / "chains" / "act_dr6_desi_dr2" / "act_dr6_desi_dr2")

alpha = 1.0
burnin = 0.30
outfile = ROOT / "t_model_planck2018_act_desi.png"

# ---------------- posteriors ----------------
datasets = {}
for label, root, color in [
    ("Planck 2018", planck_root, "tab:blue"),
    ("ACT DR6 + DESI BAO", act_desi_root, "tab:orange"),
]:
    x, w = load_ns_chain(root, burnin_fraction=burnin)
    mean, std, b68, b95 = posterior_summary(x, w)
    datasets[label] = dict(color=color, b68=b68, b95=b95)
    print(f"\n{label}\n  ns = {mean:.6f} +/- {std:.6f}")
    print(f"  68%: {b68}\n  95%: {b95}")

lo = min(d["b95"][0] for d in datasets.values())
hi = max(d["b95"][1] for d in datasets.values())
ns_min, ns_max = max(0.80, lo - 0.008), min(0.999, hi + 0.008)
ns_grid = np.linspace(ns_min, ns_max, 1000)

# ---------------- figure ----------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2), sharex=True)

for ax in (ax1, ax2):
    for d in datasets.values():
        ax.axvspan(*d["b95"], color=d["color"], alpha=0.13, zorder=0)
        ax.axvspan(*d["b68"], color=d["color"], alpha=0.30, zorder=1)

ax1.plot(ns_grid, delta_N(ns_grid, alpha), "k", lw=2, zorder=3)
ax1.set_ylabel(r"$\Delta N_*$", fontsize=13)
ax1.set_title(rf"T-model: $\Delta N_*$ ($\alpha={alpha:g}$)")

ax2.plot(ns_grid, phi_star(ns_grid, alpha), "k", lw=2, zorder=3)
ax2.set_ylabel(r"$\phi_*/M_{\rm Pl}$", fontsize=13)
ax2.set_title(rf"T-model: $\phi_*/M_{{\rm Pl}}$ ($\alpha={alpha:g}$)")

for ax in (ax1, ax2):
    ax.set_xlabel(r"$n_s$", fontsize=13)
    ax.set_xlim(ns_min, ns_max)
    ax.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax.tick_params(which="major", direction="in", length=7, top=True, right=True)
    ax.tick_params(which="minor", direction="in", length=3.5, top=True, right=True)
    ax.grid(True, alpha=0.15, zorder=0)

handles = [
    Patch(facecolor=d["color"], alpha=a, label=f"{name} ({lvl})")
    for name, d in datasets.items()
    for lvl, a in (("68%", 0.30), ("95%", 0.13))
]
fig.legend(handles=handles, loc="lower center", ncol=2, frameon=False,
           bbox_to_anchor=(0.5, -0.04))
plt.tight_layout(rect=[0, 0.12, 1, 1])
plt.savefig(outfile, dpi=300, bbox_inches="tight")
plt.show()