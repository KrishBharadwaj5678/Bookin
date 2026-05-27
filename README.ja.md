[English](README.md) | [Português](README.pt.md) | [日本語](README.ja.md) | [Русский](README.ru.md)

# 🏨 Bookin – ホテル予約管理パネル

**Bookin** は、**Streamlit** と **MongoDB** を使用して構築された、強力で直感的なホテル予約管理パネルです。ホテル管理者が予約を簡単かつ効率的に管理できるようサポートします。

![Bookinデモ](https://github.com/KrishBharadwaj5678/Bookin/raw/main/BookinDemo.png)

## ✨ 機能

| 機能                    | 説明                            |
| --------------------- | ----------------------------- |
| ✅ **新規予約の追加**         | 宿泊者情報や部屋の希望を簡単に追加             |
| 📝 **既存予約の編集**        | 予約情報を素早く効率的に変更可能              |
| 👀 **全予約の表示**         | すべての予約を整理された見やすいレイアウトで表示      |
| ❌ **予約の削除**           | 不要になった予約を削除可能                 |
| 📊 **リアルタイムデータベース**   | MongoDBと接続し、リアルタイムでデータ更新      |
| 🚀 **StreamlitベースUI** | 軽量でインタラクティブなレスポンシブWebインターフェース |

---

## 🛠️ 技術スタック

| ツール              | 用途                         |
| ---------------- | -------------------------- |
| 🚀 **Streamlit** | UI構築用フロントエンドフレームワーク        |
| 🍃 **モンゴDB**   | 予約データ保存・管理用NoSQLデータベース     |
| 🐍 **パイソン**    | バックエンドロジックおよびアプリ制御         |
| 🔗 **Pyモンゴ**   | PythonとMongoDBを接続しデータ操作を実現 |

---

## 🚀 はじめ方

### 1️⃣ リポジトリをクローン

```bash id="lmwd7z"
git clone https://github.com/KrishBharadwaj5678/Bookin.git
```

### 2️⃣ プロジェクトディレクトリへ移動

```bash id="uxu8lw"
cd Bookin
```

### 3️⃣ 依存関係をインストール

```bash id="vq7ik0"
pip install -r requirements.txt
```

### 4️⃣ `.env` ファイルを作成

プロジェクトのルートディレクトリに `.env` ファイルを作成し、MongoDB の接続文字列を追加してください。

```env id="7tk8xy"
MONGO_URI=your_mongodb_connection_string
```

### 5️⃣ アプリを実行

```bash id="7bxwli"
streamlit run app.py
```
