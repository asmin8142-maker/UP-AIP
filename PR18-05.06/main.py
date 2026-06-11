import matplotlib.pyplot as plt

from widgets_ctrl import setup_widgets
from config import *
from data_loader import load_and_prepare
from plots import *

plt.style.use(STYLE)

df = load_and_prepare()

fig, axes = plt.subplots(
    2,
    2,
    figsize=FIG_SIZE,
    gridspec_kw={
        'hspace': 0.4,
        'wspace': 0.3,
        'bottom': 0.25
    }
)

fig.suptitle(
    TITLE,
    fontsize=22,
    fontweight='bold'
)
-
ax_line = axes[0, 0]
ax_hist = axes[0, 1]
ax_scat = axes[1, 0]
ax_pie = axes[1, 1]

label = {
    v: k
    for k, v in NUMERIC_COLS.items()
}[DEFAULT_COL]

plot_line(
    ax_line,
    df,
    DEFAULT_COL,
    label
)

plot_histogram(
    ax_hist,
    df,
    DEFAULT_COL,
    label
)

plot_scatter(
    ax_scat,
    df,
    DEFAULT_COL,
    label
)

plot_pie(
    ax_pie,
    df,
    DEFAULT_COL,
    label
)

axes_dict = {
    'line': ax_line,
    'hist': ax_hist,
    'scat': ax_scat,
    'pie': ax_pie
}

widgets = setup_widgets(
    fig,
    axes_dict,
    df
)

plt.show()