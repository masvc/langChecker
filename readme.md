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

1. バックエンドディレクトリに移動

```bash
cd backend
```

2. Python 仮想環境の作成と有効化

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 依存関係のインストール

```bash
pip install -r requirements.txt
```

4. サーバーの起動

```bash
uvicorn app.main:app --reload
```

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
