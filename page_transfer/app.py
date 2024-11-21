#python -m streamlit run page_transfer/app.py

import streamlit as st

# クエリパラメータからページ情報を取得
query_params = st.query_params.get("page", ["page_a"])[0]

# ページの切り替え
if query_params == "page_b":
    import page_b
else:
    import page_a
