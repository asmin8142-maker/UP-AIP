# data_loader.py

import pandas as pd
import numpy as np

from config import (
    CSV_PATH,
    DATE_COL,
    NUMERIC_COLS
)


def load_and_prepare(path=CSV_PATH):

    df = pd.read_csv(path, skiprows=2)

    print(df.head())

    df[DATE_COL] = pd.to_datetime(
        df[DATE_COL],
        errors='coerce'
    )

    df = df.dropna(subset=[DATE_COL])

    df = df.sort_values(DATE_COL)

    for col in NUMERIC_COLS.values():

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors='coerce'
            )

    df = df.dropna(
        subset=list(NUMERIC_COLS.values()),
        how='all'
    )

    print(
        f'Загружено {df.shape[0]} строк'
    )

    return df


def filter_by_period(
        df,
        start_idx,
        end_idx
):

    return df.iloc[
        start_idx:end_idx + 1
    ].copy()


def get_date_labels(df, n=6):

    idx = np.linspace(
        0,
        len(df) - 1,
        n,
        dtype=int
    )

    return [
        df.iloc[i][DATE_COL].strftime('%d.%m.%Y')
        for i in idx
    ]