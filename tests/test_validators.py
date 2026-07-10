from pathlib import Path

import pandas as pd

from src.validators import (
    REQUIRED_COLUMNS,
    load_dataset,
    validate_file_exists,
    validate_not_empty,
    validate_penguins_dataset,
    validate_required_columns,
)


def test_penguins_file_exists() -> None:
    file_path = Path(__file__).resolve().parents[1] / "penguins.csv"

    is_valid, message = validate_file_exists(file_path)

    assert is_valid is True
    assert "Archivo encontrado" in message


def test_empty_dataframe_is_invalid() -> None:
    df = pd.DataFrame(columns=sorted(REQUIRED_COLUMNS))

    is_valid, message = validate_not_empty(df)

    assert is_valid is False
    assert "vacio" in message


def test_missing_required_columns_is_invalid() -> None:
    df = pd.DataFrame(
        {
            "species": ["Adelie"],
            "island": ["Torgersen"],
        }
    )

    is_valid, message = validate_required_columns(df)

    assert is_valid is False
    assert "bill_length_mm" in message


def test_dataframe_with_required_columns_is_valid() -> None:
    df = pd.DataFrame(
        {
            "species": ["Adelie"],
            "island": ["Torgersen"],
            "bill_length_mm": [39.1],
            "bill_depth_mm": [18.7],
            "flipper_length_mm": [181],
            "body_mass_g": [3750],
            "sex": ["male"],
        }
    )

    is_valid, messages = validate_penguins_dataset(df)

    assert is_valid is True
    assert len(messages) == 2


def test_load_dataset_reads_temporary_csv(tmp_path: Path) -> None:
    csv_file = tmp_path / "penguins_temp.csv"
    csv_file.write_text(
        "species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex\n"
        "Adelie,Torgersen,39.1,18.7,181,3750,male\n",
        encoding="utf-8",
    )

    df = load_dataset(csv_file)

    assert len(df) == 1
    assert list(df.columns) == [
        "species",
        "island",
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g",
        "sex",
    ]
