# 🤖 WhatsApp Support Agent using Django & Meta Cloud API

An intelligent, automated WhatsApp chatbot built with Django and Meta's official WhatsApp Business Cloud API. It receives, processes, and responds to customer messages using rule-based logic or GPT integration. The system is modular, database-backed, and production-ready.

---

## 🚀 Features

- ✅ Webhook endpoint to receive WhatsApp messages (Django view)
- ✅ Meta Cloud API integration (message send/receive)
- ✅ Customizable response engine (rule-based or GPT/NLP)
- ✅ User state/session management
- ✅ Message logging & admin panel
- ✅ Supports message templates, auto-replies, and error handling

---

## 🛠️ Tech Stack

- **Backend**: Python, Django, Django REST Framework  
- **API Integration**: Meta WhatsApp Business Cloud API  
- **NLP (Optional)**: OpenAI GPT / Hugging Face Transformers  
- **Database**: PostgreSQL / SQLite  
- **Deployment**: Gunicorn + Nginx / Docker (optional)  

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Suhani867/Whatsapp-Support-Agent.git
cd whatsapp-support-agent
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure `.env` file

Create a `.env` file and add the following:

```env
DJANGO_SECRET_KEY=your_django_secret
DEBUG=True
META_WA_PHONE_NUMBER_ID=your_phone_number_id
META_WA_TOKEN=your_meta_access_token
META_VERIFY_TOKEN=your_meta_verify_token
GPT_API_KEY=your_openai_key  # Optional
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Run the server

```bash
python manage.py runserver
```

---

## 📡 Webhook Configuration

- Go to [Facebook Developer Portal](https://developers.facebook.com/)
- Add your webhook URL: `https://yourdomain.com/webhook/`
- Set your **verify token** to match `META_VERIFY_TOKEN` in `.env`
- Subscribe to the following fields:
  - `messages`
  - `message_deliveries`
  - `message_reads`

---

## 📤 Sending Replies

The system uses the Meta `/messages` endpoint to reply to users.

Supported message types:
- Text
- Templates (optional)
- Image/Media (extendable)

---

## 🧠 Smart Reply Engine

The reply engine is modular:
- **Default**: rule-based keyword matching
- **Optional**: GPT/NLP based smart reply (integrated via OpenAI API)

---

## 📁 Project Structure

```
whatsapp_support/
├── core/                  # Django app with webhook + logic
│   ├── views.py           # Handles incoming messages
│   ├── utils.py           # Message processing and NLP
│   ├── models.py          # User + message logs
│   └── api.py             # WhatsApp API send message helper
├── whatsapp_support/      # Django settings
├── manage.py
└── .env
```

---

## 🔐 Security & Notes

- Access tokens must be kept secure and rotated regularly
- Do not expose your webhook without HTTPS
- Rate limits and message templates may apply in production

---

## 📄 License

MIT License

---

## 👤 Author

- [Suhani Bansal](https://github.com/Suhani867)
- Built with ❤️ using Python and Django
