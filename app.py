import pandas as pd
import streamlit as st
import streamlit.components.v1 as stc
import yfinance as yf

 
st.sidebar.button('Reload')
st.title('Tatsuro note')


def main():
    st.header('お金メモ')
    agree = st.checkbox('投資関連')
    if agree == True :
        st.text('天まで届く相場はない')
        agree = st.checkbox('自動車関連')
        if agree == True :
            st.write('海外メーカーも追加検討中')
            st.sidebar.markdown("## Settings")   

            col1, col2 = st.columns(2)
            with col1:
                selected_len = st.radio('期間',
                                        ['1ヶ月','1年','当会計年度','全てのデータ'])
                if selected_len == '1ヶ月':
                    selected_len = '1mo'
                elif selected_len == '1年':
                    selected_len = '1y'
                elif selected_len == '当会計年度':
                    selected_len = 'ytd'
                elif selected_len == '全てのデータ':
                    selected_len = 'max'
            
            with col2:
                selected_interval = st.radio('時間足',
                                        ['1日','5日','1週間','1ヶ月', '3ヶ月'])
                if selected_interval == '1日':
                    selected_interval = '1d'
                elif selected_interval == '5日':
                    selected_interval = '5d'
                elif selected_interval == '1週間':
                    selected_interval = '1wk'
                elif selected_interval == '1ヶ月':
                    selected_interval = '1mo'
                elif selected_interval == '3ヶ月':
                    selected_interval = '3mo'
            
            car_maker = ['TOYOTA','日産','マツダ','ホンダ','スバル','スズキ','三菱',
                                'BS','横浜ゴム','住友ゴム','TOYO TIRE']
            ticker = ['7203.T','7201.T','7261.T','7267.T','7270.T','7269.T','7211.T',
                                                '5108.T','5101.T','5110.T','5105.T']
            
            df = pd.DataFrame(yf.download(ticker, period=selected_len, interval = selected_interval)["Close"])
            df.columns = car_maker
            
            st.subheader('株価')
            all = st.checkbox("Select all")
            if all:
                selected_options = st.multiselect('株価データ(データフレーム)', 
                    sorted(df.columns),sorted(df.columns))
            else:
                selected_options =  st.multiselect('株価データ', 
                    sorted(df.columns), default=sorted(df.columns))
                
            st.dataframe(df[selected_options])
            
            st.text('株価データ(ラインチャート)')
            view_motor = df[selected_options]
            st.line_chart(view_motor,width=1000)

            
            st.text('ファイト〜！！')
            stc.html('<div class="flourish-embed flourish-bar-chart-race" data-src="visualisation/8529391"><script src="https://public.flourish.studio/resources/embed.js"></script></div>',height=1000)


    st.header('データ分析')
    agree = st.checkbox('機械学習')
    if agree == True :
        st.text('アイルビーバック！！')
    st.header('お勉強中')
    agree = st.checkbox('資格')
    if agree == True :
        st.text('いつやるの？')
if __name__ == '__main__':
    main()
