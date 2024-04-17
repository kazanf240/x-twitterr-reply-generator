# Twitter返信ジェネレーター

Twitter返信ジェネレーターは、ユーザーのツイートに対して自動的に返信を生成するStreamlitベースのウェブアプリケーションです。このアプリは、OpenAIのGPT-4 VISIONモデルを利用して、テキストと画像の両方に基づいた返信を生成します。

## 環境構築

1. [Pythonをインストールします](https://www.python.org/downloads/)（推奨バージョン：3.10.12 以上）
2. 以下のコマンドを実行して依存ライブラリをインストールします: `pip install -r requirements.txt`

## 環境変数の設定

OpenAIのAPIキーを環境変数"OPENAI_API_KEY"として設定してください。　
- Linux/macOS: `export OPENAI_API_KEY='your_api_key'`
- Windows: システムプロパティを通じて設定。

## アプリケーションの実行

アプリケーションを実行するには、以下のコマンドを実行します: `streamlit run test_app.py`



