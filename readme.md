# LangChecker

Web サイトの技術スタックを分析する Web アプリケーション

## 概要

LangChecker は、指定された Web サイトの URL から、そのページが使用しているプログラミング言語やフレームワーク、ライブラリなどを自動的に判別する Web アプリケーションです。

## MVP 仕様

### 検出機能

- **HTML 解析**

  - `<meta>`タグの分析
  - `<script>`タグと`<link>`タグの解析
  - 特定のクラス名や ID の検出
  - フレームワーク固有のパターン検出

- **レスポンスヘッダー分析**

  - `X-Powered-By`ヘッダー
  - `Server`ヘッダー
  - `Content-Type`ヘッダー
  - その他の技術関連ヘッダー

- **リソース URL 分析**
  - 画像、CSS、JS ファイルのパスパターン
  - API エンドポイントの構造
  - フレームワーク固有のリソースパス

### ユーザーインターフェース

- シンプルな URL 入力フォーム
- 検出結果のリスト表示
- 基本的なエラーメッセージ表示

### エラーハンドリング

- URL 形式のバリデーション
- 接続エラー時のメッセージ表示
- タイムアウト処理（30 秒）

### パフォーマンス

- 入力 URL の関連リソースを再帰的に分析
- 最大 3 階層までのリンク追跡
- 並列処理による効率化

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
- FastAPI
- BeautifulSoup4
- Requests
- Uvicorn
- aiohttp（非同期 HTTP リクエスト用）

### フロントエンド

- React.js
- TypeScript
- Tailwind CSS

## プロジェクト構成

```
langchecker/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── analyzer.py
│   │   ├── models.py
│   │   └── utils/
│   │       ├── html_parser.py
│   │       ├── header_analyzer.py
│   │       └── resource_analyzer.py
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── UrlInput.tsx
│   │   │   └── ResultDisplay.tsx
│   │   ├── pages/
│   │   │   └── Home.tsx
│   │   └── utils/
│   │       └── api.ts
│   ├── package.json
│   └── README.md
└── README.md
```

## セットアップ方法

### バックエンド

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### フロントエンド

```bash
cd frontend
npm install
npm run dev
```

## 開発予定の機能

- [x] 基本的な技術スタック検出
  - [x] HTML 解析
  - [x] ヘッダー分析
  - [x] リソース URL 分析
- [ ] 詳細な分析レポート生成
- [ ] 履歴機能
- [ ] ブックマーク機能
- [ ] 分析結果のエクスポート機能

## ライセンス

MIT License
