from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "species",
    "island",
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
    "sex",
}


def validate_file_exists(file_path: str | Path) -> tuple[bool, str]:
    """Validate that the CSV file exists before loading it."""
    path = Path(file_path)
    if not path.exists():
        return False, f"El archivo no existe: {path}"
    if not path.is_file():
        return False, f"La ruta indicada no corresponde a un archivo: {path}"
    return True, "Archivo encontrado correctamente."


def load_dataset(file_path: str | Path) -> pd.DataFrame:
    """Load the penguins CSV file using controlled validation."""
    is_valid, message = validate_file_exists(file_path)
    if not is_valid:
        raise FileNotFoundError(message)

    return pd.read_csv(file_path, na_values=["NA", "", "null", "None"])


def validate_required_columns(df: pd.DataFrame) -> tuple[bool, str]:
    """Validate that the DataFrame contains the expected penguins columns."""
    missing_columns = sorted(REQUIRED_COLUMNS.difference(df.columns))
    if missing_columns:
        return False, "Faltan columnas obligatorias: " + ", ".join(missing_columns)
    return True, "El dataset contiene las columnas obligatorias."


def validate_not_empty(df: pd.DataFrame) -> tuple[bool, str]:
    """Validate that the dataset has at least one row."""
    if df.empty:
        return False, "El dataset esta vacio."
    return True, "El dataset contiene registros."


def validate_penguins_dataset(df: pd.DataFrame) -> tuple[bool, list[str]]:
    """Run all business validations required by the dashboard."""
    validations = [
        validate_not_empty(df),
        validate_required_columns(df),
    ]
    messages = [message for _, message in validations]
    is_valid = all(result for result, _ in validations)
    return is_valid, messages
