import streamlit as st

# タイトル
st.title("登録結果")

# セッション状態からデータを取得
name = st.session_state.get("name", "")
gender = st.session_state.get("gender", "")

# 結果を表示
if name and gender:
    st.success(f"{name}さん（{gender}）を登録しました！")
else:
    st.warning("フォームに入力してください。")

# 戻るボタン
st.button("フォームページに戻る", on_click=lambda: st.experimental_set_query_params(page="form"))
