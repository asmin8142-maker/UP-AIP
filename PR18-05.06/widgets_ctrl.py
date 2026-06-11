from matplotlib.widgets import Slider
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import Button

from config import *
from data_loader import filter_by_period
from plots import *


def setup_widgets(fig, axes_dict, df_full):

    ax_line = axes_dict['line']
    ax_hist = axes_dict['hist']
    ax_scat = axes_dict['scat']
    ax_pie = axes_dict['pie']

    n = len(df_full)

    # ---------- зоны под виджеты ----------

    ax_start = fig.add_axes(
        [0.10, 0.10, 0.35, 0.03]
    )

    ax_end = fig.add_axes(
        [0.10, 0.05, 0.35, 0.03]
    )

    ax_radio = fig.add_axes(
        [0.55, 0.03, 0.20, 0.15]
    )

    ax_reset = fig.add_axes(
        [0.80, 0.05, 0.10, 0.05]
    )

    # ---------- Slider ----------

    sl_start = Slider(
        ax_start,
        'Начало',
        0,
        n - 1,
        valinit=0,
        valstep=1
    )

    sl_end = Slider(
        ax_end,
        'Конец',
        0,
        n - 1,
        valinit=n - 1,
        valstep=1
    )

    # ---------- Radio ----------

    radio = RadioButtons(
        ax_radio,
        list(NUMERIC_COLS.keys())
    )

    # ---------- Reset ----------

    btn_reset = Button(
        ax_reset,
        'Сброс'
    )

    # ---------- redraw ----------

    def redraw():

        start = int(sl_start.val)
        end = int(sl_end.val)

        if start >= end:

            end = min(
                start + 1,
                n - 1
            )

        df_filt = filter_by_period(
            df_full,
            start,
            end
        )

        label = radio.value_selected

        col = NUMERIC_COLS[label]

        clear_axes(
            [
                ax_line,
                ax_hist,
                ax_scat,
                ax_pie
            ]
        )

        plot_line(
            ax_line,
            df_filt,
            col,
            label
        )

        plot_histogram(
            ax_hist,
            df_filt,
            col,
            label
        )

        plot_scatter(
            ax_scat,
            df_filt,
            col,
            label
        )

        plot_pie(
            ax_pie,
            df_filt,
            col,
            label
        )

        fig.canvas.draw_idle()

    # ---------- callbacks ----------

    sl_start.on_changed(
        lambda val: redraw()
    )

    sl_end.on_changed(
        lambda val: redraw()
    )

    radio.on_clicked(
        lambda val: redraw()
    )

    def reset(event):

        sl_start.reset()
        sl_end.reset()

        redraw()

    btn_reset.on_clicked(reset)

    return {
        'start': sl_start,
        'end': sl_end,
        'radio': radio,
        'reset': btn_reset
    }