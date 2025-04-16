# LangChecker

Web サイトの技術スタックを分析する Web アプリケーション

## 概要

LangChecker は、指定された Web サイトの URL から、そのページが使用しているプログラミング言語やフレームワーク、ライブラリなどを自動的に判別する Web アプリケーションです。

## 主な機能

- URL を入力して Web サイトの技術スタックを分析
- 以下の要素を検出：
  - フロントエンドフレームワーク（React, Vue.js, Angular など）
  - JavaScript ライブラリ（jQuery, Bootstrap など）
  - バックエンド技術（Node.js, PHP, Python など）
  - データベース（MySQL, PostgreSQL など）
  - CMS（WordPress, Drupal など）
  - その他の技術要素

## 技術スタック

### バックエンド

- Python 3.x
- FastAPI（Web フレームワーク）
- BeautifulSoup4（HTML 解析）
- Requests（HTTP リクエスト）
- Uvicorn（ASGI サーバー）
- aiohttp（非同期 HTTP リクエスト）
- python-dotenv（環境変数管理）

### フロントエンド

- Vanilla JavaScript
- CSS
- Axios（HTTP クライアント）

## プロジェクト構成

```
langChecer/
├── backend/
│   ├── app/          # バックエンドアプリケーション
│   │   ├── main.py           # FastAPIアプリケーション
│   │   ├── analyzer.py       # 技術スタック分析ロジック
│   │   └── utils/            # ユーティリティモジュール
│   │       ├── header_analyzer.py  # HTTPヘッダー分析
│   │       └── html_parser.py      # HTML解析
│   ├── venv/         # Python仮想環境
│   └── requirements.txt
├── frontend/
│   ├── index.html    # メインHTMLファイル
│   ├── script.js     # フロントエンドロジック
│   ├── styles.css    # スタイルシート
│   ├── package.json  # フロントエンド依存関係
│   └── node_modules/ # 依存パッケージ
└── readme.md
```

## セットアップ方法

### バックエンドのセットアップ

1. Python のインストール確認

```bash
python --version
```

- Python 3.8 以上がインストールされていることを確認してください
- インストールされていない場合は、[Python 公式サイト](https://www.python.org/downloads/)からダウンロードしてインストールしてください

2. バックエンドディレクトリに移動

```bash
cd backend
```

3. Python 仮想環境の作成と有効化

```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境の有効化
# macOS/Linuxの場合
source venv/bin/activate
# Windowsの場合
venv\Scripts\activate
```

- 仮想環境が有効化されると、ターミナルのプロンプトの先頭に`(venv)`と表示されます
- 仮想環境から抜ける場合は、`deactivate`と入力してください

4. 依存関係のインストール

```bash
pip install -r requirements.txt
```

- このコマンドは、プロジェクトに必要な Python パッケージを全てインストールします
- インストールが完了するまで数分かかる場合があります
- エラーが発生した場合は、エラーメッセージを確認して必要な対応を行ってください

5. サーバーの起動

```bash
uvicorn app.main:app --reload
```

- サーバーが起動すると、`http://127.0.0.1:8000`でアクセスできます
- `--reload`オプションは、コードの変更を自動的に検知してサーバーを再起動します
- サーバーを停止する場合は、`Ctrl + C`を押してください

### フロントエンドのセットアップ

1. フロントエンドディレクトリに移動

```bash
cd frontend
```

2. 依存関係のインストール

```bash
npm install
```

3. 開発サーバーの起動

```bash
npm start
```

## 使い方

1. アプリケーションを起動
2. 分析したい Web サイトの URL を入力
3. 「分析開始」ボタンをクリック
4. 分析結果が表示されます

## 開発予定の機能

- [ ] 詳細な分析レポート生成
- [ ] 履歴機能
- [ ] ブックマーク機能
- [ ] 分析結果のエクスポート機能

## ライセンス

MIT License
