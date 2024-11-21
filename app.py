# 예측 모델 웹앱 만들기
import streamlit as st

# 1.기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model.pkl')

# 2.모델 설명
st.title('우울도 예측 모델')
st.subheader('모델 설명')
st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
st.write(' - 훈련    데이터 : 337건')
st.write(' - 테스트 데이터 : 144건')
st.write(' - 인공지능 모델 정확도 : 0.23')


def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://blog.kakaocdn.net/dn/ljADE/btr9QT40dZB/tzTVb1j4Jav4NptCdmfZMk/img.jpg");  # 여기에 복사한 링크를 붙여넣기
            background-attachment: fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()

# 3.데이터 시각화
col1, col2, col3 = st.columns(3)  
with col1:
      st.subheader('데이터시각화1')
      st.image('시각화1.png' )   # 이미지 불러오기
with col2:
      st.subheader('데이터시각화2')
      st.image('시각화2.png' )   # 이미지 불러오기
with col3:
      st.subheader('데이터시각화3')
      st.image('시각화3.png')   # 이미지 불러오기

# 4.모델 활용
st.subheader('모델 활용')
st.write('** 다음을 입력하세요.. 인공지능이 당신의 우울도를 예측해 드립니다.** (입력한 값은 저장되지 않습니다.)')

a = st.selectbox(' 하루동안 SNS 사용시간 (0:1시간 미만 / 1: 1시간-2시간 / 2: 2시간-3시간 / 3: 3시간-4시간 / 4: 4시간-5시간 / 5: 5시간 이상) ', [0,1,2,3,4,5])      #초기값은 0
b = st.selectbox(' 목적없는 SNS 사용 정도 ', [0,1,2,3,4,5] )     # 초기값은 0.0
c = st.selectbox(' SNS에게 방해받는 정도 ', [0,1,2,3,4,5] )
d = st.selectbox(' SNS 의존도 ', [0,1,2,3,4,5] )
e = st.selectbox(' SNS를 통한 비교 ', [0,1,2,3,4,5] )
f = st.selectbox(' SNS 확인빈도 ', [0,1,2,3,4,5])
                                                            # 사용자가  0,1 중에 선택

if st.button('우울도 예측'):            # 사용자가 '점수예측' 버튼을 누르면
        input_data = [[a,b,c,d,e,f]]     # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model.predict(input_data)         # model이 예측한 값을 p에 저장한다
        st.write(f"인공지능 예측점수는 {p}점 입니다.")
