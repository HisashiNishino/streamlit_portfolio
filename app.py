# streamlit run app.py
# stenv\Scripts\activate
# pip install -r requirements.txt
# streamlit run app.py

import streamlit as st 
import streamlit as st
import pandas as pd
import plotly.graph_objects as go


# タイトルの設定 
st.title('私のStreamlitアプリ') 

# テキストの表示 
st.write('こんにちは、Streamlit！')

# テキスト⼊⼒
name = st.text_input('あなたの名前を⼊⼒してください')
if name:
    st.write(f'こんにちは、{name}さん！')

# 数値⼊⼒
age = st.number_input('あなたの年齢を⼊⼒してください', min_value=0,
max_value=120, value=20)
st.write(f'あなたは{age}歳です。')

# ⽇付⼊⼒
date = st.date_input('⽇付を選択してください')
st.write(f'選択された⽇付: {date}')

# サンプルデータの作成
data = {
'名前': ['太郎', '花⼦', '⼀郎'],
'年齢': [25, 30, 35],
'都市': ['東京', '⼤阪', '福岡']
}
df = pd.DataFrame(data)
# データフレームの表⽰
st.subheader('データフレームの表⽰')
st.dataframe(df)

# 表の表⽰
st.subheader('表の表⽰')
st.table(df)


st.header('レッスン5: 折れ線グラフ(plotly,go)の作成')
# サンプルデータの作成
data = {
'⽉': ['1⽉', '2⽉', '3⽉', '4⽉', '5⽉', '6⽉'],
'売上': [100, 120, 140, 180, 200, 210],
'利益': [20, 25, 30, 40, 50, 55]
}
df = pd.DataFrame(data)
st.write('サンプルデータ:')
st.dataframe(df)

# カスタマイズされた折れ線グラフの作成
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['⽉'], y=df['売上'], mode='lines+markers',
name='売上', line=dict(color='blue', width=2)))
fig.add_trace(go.Scatter(x=df['⽉'], y=df['利益'], mode='lines+markers',
name='利益', line=dict(color='red', width=2)))
fig.update_layout(
title='⽉別売上と利益の推移',
xaxis_title='⽉',
yaxis_title='⾦額（万円）',
font=dict(family="Meiryo", size=12),
legend=dict(orientation="h", yanchor="bottom", y=1.02,
xanchor="right", x=1),
hovermode="x unified"
)
fig.update_xaxes(tickangle=45)
fig.update_yaxes(zeroline=True, zerolinewidth=2,
zerolinecolor='lightgrey')
st.plotly_chart(fig)

