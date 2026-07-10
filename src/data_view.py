import pandas as pd
import streamlit as st


def show_data_table(df: pd.DataFrame) -> None:
    """Render filters, preview, full table and numeric summary for the dataset."""
    st.subheader("Visualizacion tabular de datos")

    filtered_df = df.copy()
    filter_columns = st.columns(2)

    if "species" in filtered_df.columns:
        species_options = sorted(filtered_df["species"].dropna().unique())
        selected_species = filter_columns[0].multiselect(
            "Filtrar por especie",
            options=species_options,
            default=species_options,
        )
        if selected_species:
            filtered_df = filtered_df[filtered_df["species"].isin(selected_species)]

    if "island" in filtered_df.columns:
        island_options = sorted(filtered_df["island"].dropna().unique())
        selected_islands = filter_columns[1].multiselect(
            "Filtrar por isla",
            options=island_options,
            default=island_options,
        )
        if selected_islands:
            filtered_df = filtered_df[filtered_df["island"].isin(selected_islands)]

    st.caption(f"Registros visibles: {len(filtered_df):,}")
    st.write("Vista previa")
    st.dataframe(filtered_df.head(10), use_container_width=True)

    with st.expander("Mostrar tabla completa"):
        st.dataframe(filtered_df, use_container_width=True)

    numeric_df = filtered_df.select_dtypes(include="number")
    if not numeric_df.empty:
        st.write("Resumen estadistico")
        st.dataframe(numeric_df.describe(), use_container_width=True)
