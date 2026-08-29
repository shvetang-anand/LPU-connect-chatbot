# 🎓 LPU Connect — FAQ Chatbot

A smart FAQ chatbot for **Lovely Professional University** that answers common student questions about admissions, fees, exams, hostel, library, timetable, scholarships, and more.

![Chatbot Preview](preview.png)

## ✨ Features

- 💬 **Natural language matching** — ask questions in your own words
- 🎯 **25+ FAQ entries** covering fees, exams, hostel, library, timetable, admissions, and scholarships
- 📱 **Responsive design** — works on mobile, tablet, and desktop
- 🖼️ **LPU campus background** — beautiful UI with the university's iconic architecture
- ⚡ **Instant responses** — no page reload, smooth chat experience

## 🚀 Quick Start

### Prerequisites
- Python 3.8+

### Run Locally

```bash
# Clone the repo
git clone https://github.com/shvetang-anand/LPU-connect-chatbot.git
cd LPU-connect-chatbot

# Install dependencies
pip install flask

# Start the server
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

## 📁 Project Structure

```
LPU-connect-chatbot/
├── app.py              # Flask web server
├── chatbot.py          # Fuzzy matching engine
├── faq_data.json       # FAQ knowledge base (25+ entries)
├── preview.png         # Chatbot preview screenshot
├── templates/
│   └── index.html      # Chat UI
├── static/
│   ├── style.css       # Responsive styles
│   ├── script.js       # Frontend logic
│   └── LPU-20.jpg      # Campus background image
└── .gitignore
```

## 🔧 How It Works

1. **User types a question** → sent as JSON to `/ask` endpoint
2. **Chatbot engine** matches the query against FAQ keywords using fuzzy string matching
3. **Best match returned** with the answer, or a clarification prompt if ambiguous

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Chat UI homepage |
| `/ask` | POST | Send a question, get an answer |

**Example request:**
```json
POST /ask
{ "question": "How do I check my fees?" }
```

**Example response:**
```json
{
  "answer": "Programme fees depend on the programme, semester, scholarship and student category. Check the official LPU programme page or student portal."
}
```

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## 👥 Team

- **Shvetang Anand** — Backend & Chatbot Engine
- **Sreedev A S** — Chat UI Design
- **Yaswanth A** — Knowledge Base Content
- **Aaroh Jaison** — Demo & Slides

---

Built with ❤️ for LPU students
