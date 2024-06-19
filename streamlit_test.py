#pip install streamlit
import streamlit as st
from PIL import Image

#터미널에 streamlit run 파일명

#로그인화면 만들기 사이드바
st.sidebar.header("로그인")
user_id = st.sidebar.text_input("아이디 입력", value='', max_chars=15)
user_pw = st.sidebar.text_input("비밀번호 입력", value='', type="password", max_chars=15)

if user_pw == "1234" and user_id =="hi":

    #이미지 목록을 콤보상자 셀렉트박스로 만들기
    st.sidebar.header("그림 목록")
    sel_options = ['','진주 귀걸이를 한 소녀','별이 빛나는 밤','절규','생명의 나무','월하정인']
    user_opt = st.sidebar.selectbox("좋아하는 작품은?",sel_options,index=0)
    st.sidebar.write('*선택한 그림은',user_opt)

    #메인화면
    st.subheader(user_opt)
    image_files = ['welcome.jpg','Vermeer.png','Gogh.png','Munch.png','Klimt.jpg','ShinYoonbok.png']
    sel_index = sel_options.index(user_opt)
    img_file = image_files[sel_index]
    img_local =Image.open(f'img/{img_file}')
    st.image(img_local,caption=user_opt)

