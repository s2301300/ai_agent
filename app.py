# 예측 모델 웹앱 만들기
import streamlit as st

# 1.기계학습 모델 파일 로드
import joblib
# model = joblib.load('linear_regression_model.pkl')

# 2.모델 설명
st.title('행복도 예측 모델')
st.subheader('모델 설명')
st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
st.write(' - 훈련    데이터 : *건')
st.write(' - 테스트 데이터 : *건')
st.write(' - 인공지능 모델 정확도 : ***')
def add_box(text, opacity=1.0):
    st.markdown(
        f"""
        <div style="border: 2px solid #4CAF50; border-radius: 5px; padding: 10px; background-color: rgba(249, 249, 249, {opacity});">
            <h4>{text}</h4>
        </div>
        """,
        unsafe_allow_html=True
    )
    add_box("test", opacity=0.8)  # 80% 불투명도

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.inc.com/uploaded_files/image/1024x576/getty_478389113_970647970450091_99776.jpg");  # 여기에 복사한 링크를 붙여넣기
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
     # st.image('시각화1.png' )   # 이미지 불러오기
with col2:
      st.subheader('데이터시각화2')
    #  st.image('시각화2.png' )   # 이미지 불러오기
with col3:
      st.subheader('데이터시각화3')
     # st.image('시각화3.png')   # 이미지 불러오기

# 4.모델 활용
st.subheader('모델 활용')
st.write('**** 다음을 입력하세요.. 인공지능이 당신의 행복도를 예측해 드립니다.')

a = st.selectbox(' 목적없는 사용 ', [0,1,2,3,4,5])      #초기값은 0
b = st.selectbox(' 방해 ', [0,1,2,3,4,5] )     # 초기값은 0.0
c = st.selectbox(' 의존도 ', [0,1,2,3,4,5] )
d = st.selectbox(' 비교 ', [0,1,2,3,4,5] )
e = st.selectbox(' 확인빈도 ', [0,1,2,3,4,5] )
f = st.selectbox(' 우울 ', [0,1,2,3,4,5] )
                                                            # 사용자가  0,1 중에 선택

#if st.button('행복도 예측'):            # 사용자가 '점수예측' 버튼을 누르면
 #       input_data = [[a,b,c,d,e,f]]     # 사용자가 입력한 a,b,c 를 input_data에 저장하고
  #      p = model.predict(input_data)         # model이 예측한 값을 p에 저장한다
   #     st.write('인공지능의 예측 점수는', p)
