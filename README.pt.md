[English](README.md) | [Português](README.pt.md) | [日本語](README.ja.md) | [Русский](README.ru.md)

# 🏨 Bookin – Painel de Administração de Reservas de Hotel

**Bookin** é um painel administrativo poderoso e intuitivo construído com **Streamlit** e **MongoDB**, que permite aos administradores de hotéis gerenciar reservas de forma simples e eficiente.

![BookinDemonstração](https://github.com/KrishBharadwaj5678/Bookin/raw/main/BookinDemo.png)

## ✨ Funcionalidades

| Funcionalidade                      | Descrição                                                        |
| ----------------------------------- | ---------------------------------------------------------------- |
| ✅ **Adicionar novas reservas**      | Adicione facilmente dados dos hóspedes e preferências de quartos |
| 📝 **Editar reservas existentes**   | Modifique reservas de forma rápida e eficiente                   |
| 👀 **Visualizar todas as reservas** | Exibe todas as reservas em um layout organizado e limpo          |
| ❌ **Excluir reservas**              | Remova reservas quando não forem mais necessárias                |
| 📊 **Banco de dados em tempo real** | Conectado ao MongoDB para atualizações em tempo real             |
| 🚀 **Interface com Streamlit**      | Interface web leve, interativa e responsiva                      |

---

## 🛠️ Tecnologias Utilizadas

| Ferramenta       | Finalidade                                               |
| ---------------- | -------------------------------------------------------- |
| 🚀 **Streamlit** | Framework frontend para criação da interface             |
| 🍃 **MongoDB**   | Banco de dados NoSQL para armazenar e gerenciar reservas |
| 🐍 **Pitão**    | Lógica de backend e controle da aplicação                |
| 🔗 **PyMongo**   | Conexão entre Python e MongoDB para operações de dados   |

---

## 🚀 Como Começar

### 1️⃣ Clone o repositório

```bash id="m3kq7v"
git clone https://github.com/KrishBharadwaj5678/Bookin.git
```

### 2️⃣ Navegue até o diretório do projeto

```bash id="x9p2ld"
cd Bookin
```

### 3️⃣ Instale as dependências

```bash id="c8v1aa"
pip install -r requirements.txt
```

### 4️⃣ Crie um arquivo `.env`

Crie um arquivo `.env` na raiz do projeto e adicione sua string de conexão do MongoDB:

```env id="z2q9mn"
MONGO_URI=your_mongodb_connection_string
```

### 5️⃣ Execute o aplicativo

```bash id="t7r4kp"
streamlit run app.py
```
