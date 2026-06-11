import matplotlib.dates as mdates
import numpy as np
import pandas as pd

from config import (
    PALETTE,
    HIST_BINS,
    DATE_COL,
    PIE_BINS
)


def clear_axes(axes):
    for ax in axes:
        ax.cla()


def plot_line(ax, df, col, label):

    if df.empty:
        return

    ax.plot(
        df[DATE_COL],
        df[col],
        color=PALETTE[0],
        alpha=0.20,
        linewidth=0.8,
        label='Исходные данные'
    )

    rolling = df[col].rolling(
        720,
        min_periods=1
    ).mean()

    ax.plot(
        df[DATE_COL],
        rolling,
        color='#D9480F',
        linewidth=3,
        label='Среднее (30 дней)'
    )

    if df[col].notna().any():

        idx = df[col].idxmax()

        ax.annotate(
            f"max={df.loc[idx,col]:.1f}",
            xy=(df.loc[idx, DATE_COL], df.loc[idx, col]),
            xytext=(20, -20),
            textcoords="offset points",
            fontsize=9,
            color="#D9480F",
            arrowprops=dict(
                arrowstyle='->',
                color="#D9480F"
            )
        )

    ax.set_title(
        f'Динамика: {label}',
        fontsize=20,
        fontweight='bold'
    )

    ax.set_ylabel(label)

    ax.legend()

    ax.xaxis.set_major_formatter(
        mdates.DateFormatter('%b %Y')
    )

    ax.tick_params(
        axis='x',
        rotation=30
    )


def plot_histogram(ax, df, col, label):

    data = df[col].dropna()

    if data.empty:
        return

    mean_val = data.mean()
    median_val = data.median()

    ax.hist(
        data,
        bins=25,
        color='#F59E0B',
        edgecolor='white',
        alpha=0.9
    )

    ax.axvline(
        mean_val,
        color='#DC2626',
        linestyle='--',
        linewidth=2,
        label=f'mean={mean_val:.1f}'
    )

    ax.axvline(
        median_val,
        color='#059669',
        linestyle=':',
        linewidth=2,
        label=f'median={median_val:.1f}'
    )

    ax.set_title(
        f'Распределение: {label}',
        fontsize=20,
        fontweight='bold'
    )

    ax.set_xlabel(label)
    ax.set_ylabel('Частота')

    ax.legend()


def plot_scatter(ax, df, col, label):

    data = df[col].dropna()

    if data.empty:
        return

    if len(data) > 1000:

        step = len(data) // 1000

        data = data.iloc[::step]

    x = np.arange(len(data))

    ax.scatter(
        x,
        data,
        c=data,
        cmap='plasma',
        s=15,
        alpha=0.5
    )

    z = np.polyfit(
        x,
        data,
        1
    )

    trend = np.poly1d(z)(x)

    ax.plot(
        x,
        trend,
        '--',
        linewidth=2.5,
        color='#7C3AED',
        label=f'Тренд k={z[0]:.3f}'
    )

    ax.set_title(
        f'Разброс + тренд: {label}',
        fontsize=20,
        fontweight='bold'
    )

    ax.set_xlabel('Индекс точки')
    ax.set_ylabel(label)

    ax.legend()


def plot_pie(ax, df, col, label):

    data = df[col].dropna()

    if data.empty:
        return

    try:

        cats = pd.qcut(
            data,
            q=PIE_BINS,
            duplicates='drop'
        )

    except Exception:

        cats = pd.cut(
            data,
            bins=PIE_BINS
        )

    counts = cats.value_counts().sort_index()

    labels = []

    for interval in counts.index:
        labels.append(
            f"{interval.left:.1f}–{interval.right:.1f}"
        )

    ax.pie(
        counts.values,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=[
            '#F97316',
            '#22C55E',
            '#EF4444',
            '#0EA5E9'
        ]
    )

    ax.set_title(
        f'Доли диапазонов: {label}',
        fontsize=20,
        fontweight='bold'
    )