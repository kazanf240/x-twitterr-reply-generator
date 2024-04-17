# x-twitter-reply-generator


x-twitter-reply-generatorは、ユーザーのツイートに対して自動的に返信を生成するStreamlitベースのウェブアプリケーションです。このアプリは、OpenAIのGPT-4 VISIONモデルを利用して、テキストと画像の両方に基づいた返信を生成します。  

## 環境構築

1. [Pythonをインストールします](https://www.python.org/downloads/)（推奨バージョン：3.10.12 以上）
2. 以下のコマンドを実行して依存ライブラリをインストールします: `pip install -r requirements.txt`

## 環境変数の設定

OpenAIのAPIキーを環境変数"OPENAI_API_KEY"として設定してください。　
- Linux/macOS: `export OPENAI_API_KEY='your_api_key'`
- Windows: システムプロパティを通じて設定。

## アプリケーションの実行

アプリケーションを実行するには、以下のコマンドを実行します: `streamlit run test_app.py`

# x-twitter-reply-generator  
  
x-twitter-reply-generator is a Streamlit-based web application that automatically generates replies to user tweets. The application uses OpenAI's GPT-4 VISION model to generate replies based on both text and images.  
## Building the Environment  
1. Install Python (recommended version: 3.10.12 or higher)
2. InstallInstall dependent libraries by running the following command: pip install -r requirements.txt  
# Set environment variables  
Set the OpenAI API key as the environment variable "OPENAI_API_KEY".  
- Linux/macOS: export OPENAI_API_KEY='your_api_key'  
- Windows: set through system properties.  
## Running the Application  
To run the application, execute the following command:`streamlit run test_app.py`  



