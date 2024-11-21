import streamlit as st

# タイトル
st.title("ページB")

# 戻るリンク
st.write("ページAに戻るには以下のリンクをクリックしてください。")
st.markdown("[ページAへ](?page=page_a)")  # ページAに戻るリンク
