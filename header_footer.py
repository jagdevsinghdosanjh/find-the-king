import streamlit as st
from htbuilder import div, a, styles
from htbuilder.units import px, percent

# ---------- HEADER ----------
def render_header(title="Find the King", subtitle="A game of luck, logic, and learning"):
    st.title(f"👑 {title}")
    st.markdown(f"##### {subtitle}")
    st.markdown("---")

# ---------- FOOTER ----------
def layout(*args):
    style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp { bottom: 105px; }
    </style>
    """
    footer_style = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="gray",
        text_align="center",
        font_size="14px",
        height="auto",
        opacity=1
    )
    foot = div(style=footer_style)(*args)
    st.markdown(style, unsafe_allow_html=True)
    st.markdown(str(foot), unsafe_allow_html=True)

def render_footer():
    layout(
        "Made with ❤️ by Jagdev Singh Dosanjh | ",
        a(_href="https://github.com/jagdevsinghdosanjh", _target="_blank")("GitHub"),
        " | ",
        a(_href="mailto:jagdevsinghdosanjh@gmail.com")("Contact"),
        " | ",
        a(_href="https://streamlit.io", _target="_blank")("Powered by Streamlit")
    )
