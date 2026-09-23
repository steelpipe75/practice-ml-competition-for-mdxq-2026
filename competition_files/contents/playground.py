import streamlit as st
from st_screen_stats import ScreenData

from utils import page_config, check_password

# --- Playground Page Settings ---
PLAYGROUND_PAGE_URL_JUPYTERLITE = (
    "https://steelpipe75.github.io/practice-ml-competition-for-mdxq-2026/JupyterLite/"
)
PLAYGROUND_PAGE_URL_MARIMO = (
    "https://steelpipe75.github.io/practice-ml-competition-for-mdxq-2026/marimo/"
)
PLAYGROUND_PAGE_URL_COLAB = (
    "https://colab.research.google.com/github/steelpipe75/practice-ml-competition-for-mdxq-2026/blob/main/competition_files/playground/Colab/sample.ipynb"
)

page_config()

st.title(":material/terminal: playground")

# 認証チェック
check_password()


def playground() -> None:
    screenD = ScreenData(setTimeout=1000)
    data = screenD.st_screen_data()

    calculated_height = int(data["innerHeight"] * 0.9)
    iframe_height = max(calculated_height, 720)

    select_playground = st.segmented_control(
        "select type",
        [
            ":material/dynamic_form: JupyterLite",
            ":material/flowsheet: marimo",
            ":material/code_blocks: Colab",
        ],
        selection_mode="single",
        default=":material/dynamic_form: JupyterLite",
    )

    if select_playground == ":material/dynamic_form: JupyterLite":
        st.iframe(
            src=PLAYGROUND_PAGE_URL_JUPYTERLITE,
            width=data["innerWidth"],
            height=iframe_height,
        )
        st.link_button(
            ":material/dynamic_form: JupyterLite サンプルスクリプトを別タブで開く",
            url=PLAYGROUND_PAGE_URL_JUPYTERLITE,
        )
    elif select_playground == ":material/flowsheet: marimo":
        st.iframe(
            src=PLAYGROUND_PAGE_URL_MARIMO,
            width=data["innerWidth"],
            height=iframe_height,
        )
        st.link_button(
            ":material/flowsheet: marimo サンプルスクリプトを別タブで開く",
            url=PLAYGROUND_PAGE_URL_MARIMO,
        )
    else:
        st.write(
            ":material/code_blocks: Colabのサンプルスクリプトはiframeで表示できないため、以下のリンクからColabを開いてください。"
        )
        st.link_button(
            ":material/code_blocks: Colab サンプルスクリプトを別タブで開く",
            url=PLAYGROUND_PAGE_URL_COLAB,
        )


playground()
