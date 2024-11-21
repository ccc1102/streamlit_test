import streamlit as st

print("@@00000")


# セッション状態を初期化
if "name" not in st.session_state:
    st.session_state["name"] = ""
if "gender" not in st.session_state:
    st.session_state["gender"] = ""

# タイトル
st.title("ユーザー登録フォーム")

# 入力フォーム
with st.form("user_form"):
    st.session_state["name"] = st.text_input("名前を入力してください")
    gender_option = st.radio("性別を選択してください", options=["男性", "女性"])
    st.session_state["gender"] = gender_option
    submitted = st.form_submit_button("送信")

# フォーム送信後の処理
if submitted:
    print("@@1111111")
    if not st.session_state["name"]:
        int("@@@222222")
        st.error("名前が入力されていません")
    else:
        print("@@@333333")
        # クエリパラメータを設定してリロード
        st.experimental_set_query_params(page="result")
        #st.experimental_rerun()  # ページをリロードしてクエリパラメータを適用
else:
    print("@@444444")