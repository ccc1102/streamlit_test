'''
ターミナルに↓のコマンドを入力して実行
python -m streamlit run uranai.py
'''


import streamlit as st
import random
from datetime import datetime

today = datetime.now().strftime("%m月%d日")

luck_array = ["超スッキリ", "スッキリ", "最悪"]
luck = random.choice(luck_array)

st.write(f" {today}の運勢は「{luck}」です！")
