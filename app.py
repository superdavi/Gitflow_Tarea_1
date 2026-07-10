from pathlib import Path

import matplotlib.pyplot as plt
import streamlit as st

from src.data_view import show_data_table
from src.validators import load_dataset, validate_penguins_dataset


DATA_FILE = Path(__file__).parent / "penguins.csv"


def main() -> None:
    st.set_page_config(
        page_title="Penguins Analytics",
        page_icon="🐧",
        layout="wide",
    )

    st.title("Dashboard de Analisis de Penguins")
    st.write(
        "Aplicacion Streamlit para cargar, validar y explorar el dataset "
        "penguins.csv como parte de una practica de Gitflow."
    )

    try:
        df = load_dataset(DATA_FILE)
    except FileNotFoundError as error:
        st.error(str(error))
        st.stop()
    except Exception as error:
        st.error(f"No fue posible cargar el dataset: {error}")
        st.stop()

    is_valid, messages = validate_penguins_dataset(df)
    st.subheader("Validaciones del dataset")
    for message in messages:
        st.success(message) if is_valid else st.warning(message)

    if not is_valid:
        st.error("La estructura del archivo no es valida para el dashboard.")
        st.stop()

    species_count = df["species"].dropna().nunique()
    island_count = df["island"].dropna().nunique()

    st.subheader("Metricas generales")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de registros", f"{len(df):,}")
    col2.metric("Total de columnas", len(df.columns))
    col3.metric("Especies disponibles", species_count)
    col4.metric("Islas disponibles", island_count)

    st.subheader("Distribucion por especie")
    species_distribution = df["species"].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8, 4))
    species_distribution.plot(kind="bar", ax=ax, color="#2563eb")
    ax.set_xlabel("Especie")
    ax.set_ylabel("Cantidad de registros")
    ax.set_title("Cantidad de pinguinos por especie")
    st.pyplot(fig)

    show_data_table(df)


if __name__ == "__main__":
    main()
