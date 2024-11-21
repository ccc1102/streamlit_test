import streamlit as st

# タイトル
st.title("ページA")

# ページBへのリンク
st.write("ページBに遷移するには以下のリンクをクリックしてください。")
st.markdown("[ページBへ](?page=page_b)")  # ページBに遷移するリンク
