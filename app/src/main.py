import streamlit as st

import pipeline

import ui_components as components


st.set_page_config(
    layout="wide"
)

ts, real_y = components.load_dataset()
if ts is None:
    exit()

with st.spinner():
    pl = pipeline.Pipeline(ts, ground_truth=real_y)
    pl.predict()
    engine_inference_mapping = pl.get_fmt_data()

    for family_id, inference_by_phase in engine_inference_mapping.items():
        components.chart.family_accordion(family_id, inference_by_phase)

