import base64
import io
import os

import openai
import streamlit as st
from PIL import Image

from ui_functions import get_user_input


# 環境変数からOpenAI APIキーを読み込む
openai.api_key = os.getenv('OPENAI_API_KEY')

# 既存のコードをそのまま使用します
tweet_text, uploaded_image = get_user_input()

if st.button("返信を生成"):
    if tweet_text or uploaded_image is not None:
        try:
            # 画像をbase64にエンコード
            img_str = ""
            if uploaded_image is not None:
                image = Image.open(uploaded_image)
                buffered = io.BytesIO()
                image.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()

            # ユーザーメッセージの作成
            user_message = {
                "role": "user",
                "content": [{"type": "text", "text": tweet_text}]
            }

            # 画像がある場合は、ユーザーメッセージに画像を追加
            if img_str:
                user_message["content"].append({
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{img_str}"
                })

            # OpenAI APIリクエストの作成と送信
            response = openai.ChatCompletion.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "system",
                        "content": "以下のテキストと画像に対してフレンドリーに、簡潔に、かつ関連性のある返信を日本語で生成してください"
                    },
                    user_message
                ],
                max_tokens=280
            )

            # 返信を取得して表示
            reply_text = response.choices[0].message.content
            st.write('返信:', reply_text)

        except Exception as e:
            st.write("エラーが発生しました:", e)
    else:
        st.write('ツイートテキストを入力してください、または画像をアップロードしてください。')
        
