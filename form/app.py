
#python -m streamlit run form/app.py

import streamlit as st

# クエリパラメータからページ情報を取得
query_params = st.query_params.get("page", ["form"])[0]
print("query_params",query_params)
# ページの切り替え
if query_params == "result":
    import result_page
else:
    import form_page
