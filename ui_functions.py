import streamlit as st


def get_user_input():
    st.title('Twitter返信ジェネレーター')

    # ユーザーからのツイートテキスト入力を受け取る
    tweet_text = st.text_area('ツイートテキストを入力してください', '')

    # ユーザーが画像をアップロードできるようにする
    uploaded_image = st.file_uploader('画像をアップロードしてください', type=['jpg', 'jpeg', 'png'])

    return tweet_text, uploaded_image
    
