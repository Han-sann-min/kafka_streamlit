import streamlit as st
import subprocess
import pandas as pd
from kafka import KafkaConsumer
import myconfig
import os.path

# 사용자 스크립트 매핑
user_scripts = {
    myconfig.customer_name1: {"producer": "Producer2.py", "consumer": "consumer2.py"},
    myconfig.customer_name2: {"producer": "Producer3.py", "consumer": "consumer3.py"},
    myconfig.customer_name3: {"producer": "Producer4.py", "consumer": "consumer4.py"},
}

# 초기에는 선택된 사용자가 없으므로 None으로 초기화
selected_user = None

# Create buttons for each customer
button_clicked1 = st.button(myconfig.customer_name1)
button_clicked2 = st.button(myconfig.customer_name2)
button_clicked3 = st.button(myconfig.customer_name3)

# Check if any button is clicked
if button_clicked1 or button_clicked2 or button_clicked3:
    # Set the selected_user based on which button is clicked
    if button_clicked1:
        selected_user = myconfig.customer_name1
    elif button_clicked2:
        selected_user = myconfig.customer_name2
    elif button_clicked3:
        selected_user = myconfig.customer_name3

    try:
        # 선택된 사용자에 대한 스크립트 실행
        subprocess.run(["python", f"./kafka_practice/{user_scripts[selected_user]['producer']}"])
        subprocess.run(["python", f"./kafka_practice/{user_scripts[selected_user]['consumer']}"])

        # 여기에서 사용자 정보를 생성하거나 가져오는 로직을 추가해야 합니다.
        user_info = user_scripts[selected_user]

        # 그 사용자가 어떤 장르의 영화를 좋아하고 그 장르에 해당하는 어떤 영화들을 보았는지 출력
        st.write(f"{selected_user}님의 정보: {user_info}")

    except Exception as e:
        st.error(f"오류 발생: {e}")
