import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import yfinance as yf
import seaborn as sns
from datetime import datetime, date

sns.set_context("poster", 0.5)
st.sidebar.markdown("## Settings")
    
st.title('自動車関連株式（工事中）')
st.header('国内')
        
def show_heatmap(df):
    fig, ax = plt.subplots(figsize=(10,10))
    sns.heatmap(df.corr(), annot=True, ax=ax)
    st.pyplot(fig)

def main():
    selected_len = st.sidebar.radio('期間',
                             ['1ヶ月','1年','当会計年度','全てのデータ'])
    if selected_len == '1ヶ月':
        selected_len = '1mo'
    elif selected_len == '1年':
        selected_len = '1y'
    elif selected_len == '当会計年度':
        selected_len = 'ytd'
    elif selected_len == '全てのデータ':
        selected_len = 'max'
        
        
    df_motor = pd.DataFrame(yf.download(['7203.T','7201.T','7261.T','7267.T','7270.T','7269.T','7211.T'], period=selected_len, interval = "1d")["Close"])
    df_motor.columns = ['TOYOTA','日産','マツダ','ホンダ','ＳＵＢＡＲＵ','スズキ','三菱']

    df_tire = pd.DataFrame(yf.download(['5108.T','5101.T','5110.T','5105.T'], period=selected_len, interval = "1d")["Close"])
    df_tire.columns = ['ブリヂストン','横浜ゴム','住友ゴム','TOYO TIRE']
    
    st.subheader('自動車')
    selected_targets_motor = st.multiselect('select targets', sorted(df_motor.columns))
    view_motor = df_motor[selected_targets_motor]
    st.line_chart(view_motor)

    st.subheader('タイヤ')
    selected_targets_tire = st.multiselect('select targets', sorted(df_tire.columns))
    view_tire = df_tire[selected_targets_tire]
    st.line_chart(view_tire)
    
    st.subheader('自動車とタイヤの相関関係')
    df_corr = pd.concat([df_motor, df_tire], axis=1)
    st.write(date.today())
    show_heatmap(df_corr)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width=True)
    
    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", use_column_width=True)
        
    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", use_column_width=True)
        
if __name__ == '__main__':
    main()
    st.sidebar.button('Reload')