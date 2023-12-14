import streamlit as st 
import pandas as pd
import plotly.express as px

import os

# 현재 스크립트 파일의 경로
base_path = os.path.dirname(__file__)
file_path_year = os.path.join(base_path, '년도별 성적.csv')
file_path_day = os.path.join(base_path, '일자별성적.csv')

# 파일 존재 확인
if not os.path.exists(file_path_year) or not os.path.exists(file_path_day):
    st.error("파일을 찾을 수 없습니다.")
    # 파일이 없을 때 예외 처리
else:
    year = pd.read_csv(file_path_year)
    day = pd.read_csv(file_path_day)
    # 파일을 읽어오고 나머지 코드 실행


#노시환 개인프로필 
st.write('# 노시환 ')
# 선수 정보
player_info = {
    "이름": "노시환",
    "팀": "두산 베어스",
    "포지션": "외야수",
    "생년월일": "1999년 10월 10일",
    "신장/체중": "185cm / 90kg",
    "경력": "중앙대학교",
}

st.write(f"# {player_info['이름']} 선수 프로필")
st.write("## 선수 정보")
st.write("```")
for key, value in player_info.items():
    st.write(f"{key}: {value}")
st.write("```")

# 선수 이미지
st.image("nosi.jpeg", caption=f"{player_info['이름']} 선수 이미지")


#노시환 선수 연도별 성적 
st.write('# 노시환 성적 분석 ')
st.write('###  노시환 선수 연도별 성적 변화 table ')
year =pd.read_csv('년도별 성적.csv')
year_index = year.loc[0:4,['연도', 'AVG', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'SB', 'BB', 'E']]
year_index

year_index = year_index.rename(columns={'AVG' : '타율', 'G' : '경기', 'PA' : '타석', 'AB' : '타수', 'R' : '득점', 'H' : '안타', '2B' : '2루타', '3B' : '3루타', 'HR' : '홈런', 'SB' : '도루', 'BB' : '볼넷', 'E' : '에러'})

st.write('###  노시환 선수 연도별 성적 변화 line 그래프 ')

def update_graph(selected_columns):
    fig = px.line(year_index, x='연도', y=selected_columns, title='연도별 선수 성적 변화')
    st.plotly_chart(fig)

selected_columns = st.multiselect('원하는 열을 선택하세요.', year_index.columns)
if selected_columns:
    update_graph(selected_columns)


# 노시환선수 일자별 성적 
st.write('###  노시환 선수 일자별 성적 변화 table ')

day = pd.read_csv("일자별성적.csv")
day_index = day.loc[0:9,['일자', 'AVG', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'SB', 'BB']]
day_index = day_index.rename(columns={'AVG': '타율', 'PA': '타석', 'AB': '타수', 'R': '득점', 'H': '안타', '2B': '2루타', '3B': '3루타', 'HR': '홈런','SB': '도루', 'BB': '볼넷'})

st.dataframe(day_index)


st.write('###  노시환 선수 연도별 성적 변화 line 그래프 ')

def update_graph(selected_columns_day):
    fig = px.line(day_index, x='일자', y=selected_columns_day, title='일자별 선수 성적 변화')
    st.plotly_chart(fig)

selected_columns_day = st.multiselect('원하는 열을 선택하세요.', day_index.columns)
if selected_columns_day:
    update_graph(selected_columns_day)
