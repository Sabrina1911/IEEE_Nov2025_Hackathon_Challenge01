# 🌌 Echo of the North
**Preserving Northern Indigenous Languages through Digital Storytelling**

> “Echo of the North isn’t just preserving stories — it’s keeping the heartbeat of a culture alive.”

---

## 🧭 Overview
**Echo of the North** is an offline-first storytelling platform connecting **Elders and Youth** in remote Northern Indigenous communities.  
It captures **oral traditions**, transcribes them, and preserves them in both **Indigenous and English** languages — turning voices into living digital heritage.

Built during the **IEEE November 2025 Hackathon**, this prototype demonstrates how technology can act as a **bridge across generations**, ensuring that every story told keeps a language alive.

---

## 🎯 Problem We Address
| Challenge | Impact |
|------------|---------|
| **Language Endangerment** | Every two weeks, an Indigenous language disappears globally. All Indigenous languages in Canada are at risk. |
| **Geographic Displacement** | Youth moving to urban centers lose connection to language and cultural identity. |
| **Connectivity Barriers** | Remote communities experience poor or no internet connectivity. |
| **Elder Knowledge Loss** | Without digital preservation, oral traditions risk permanent loss. |

---

## 💡 Vision
To reconnect generations and empower Indigenous youth through accessible, offline-ready digital tools that honour **oral tradition** while embracing **modern AI technology**.

---

## ⚙️ Core Features (MVP)
| Feature | Description |
|----------|--------------|
| 🎙️ **Audio Capture** | Record oral stories using **Streamlit’s Audio Recorder** or HTML Audio API. Saves locally as `.wav`. |
| 🧾 **Transcription & Translation** | Automatic transcription and English translation using **OpenAI Whisper (small model)**. |
| 💾 **Local Storage** | Offline storage in SQLite/JSON for resilience in low-connectivity environments. |
| 📚 **Story Library** | Browse, play, and explore saved stories with metadata and playback controls. |
| 💬 **Community Reflections** | Add personal memories or reflections — audio or text — to shared stories. |
| 🔄 **Offline Sync** | Data accessible offline, with the ability to sync once connectivity returns. |

---

## 🧑‍🤝‍🧑 User Roles
### 👵 Elder
- Record stories → Save → Transcript & Translate → Reflect → Preserve  
- Add voice notes and share from anywhere.

### 🧒 Youth
- Listen to preserved stories.
- Add reflections or memories through text or voice.
- Stay connected to cultural roots — even from urban centers.

---

## 📱 App Demo Flow

Home → Record Story → Transcribe → Translate → Reflect → Preserve

**Elder & Youth Shared Actions:**
- View Story Library  
- Watch Journey (video stories)  
- Add Reflections  

Each action contributes to keeping ancestral wisdom alive.

---

## 🖥️ Prototype Tech Stack
| Layer | Technology |
|--------|-------------|
| Frontend | **Streamlit** |
| Backend | **Python 3.11**, **SQLite / JSON** |
| AI | **OpenAI Whisper (Small Model)** |
| Storage | Local / Offline |
| UI/UX | Light theme, rotating banner images, minimalist northern aesthetic |
| Assets | `assets/echo_cover_1.jpg`, `echo_cover_2.jpg`, `echo_cover_3.jpg` |

---

## 🧩 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Sabrina1911/IEEE_Nov2025_Hackathon_Challenge01.git
cd IEEE_Nov2025_Hackathon_Challenge01
```

### 2️⃣ Set Up Virtual Environment
```bash
python -m venv venv_echonorth
venv_echonorth\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App
```bash
streamlit run app.py
```

Then open the provided local URL (usually `http://localhost:8501`) in your browser.

---

## 📂 Project Structure
```
Challenge_01/
│
├── app.py                   # Main Streamlit app
├── assets/                  # Static images and cover photos
├── mock_data/               # Example story data
├── requirements.txt          # Dependency list
├── README.md                 # (You are here)
└── venv_echonorth/          # Virtual environment (ignored in Git)
```

---

## 🌍 Why It Matters
> “For every story saved, a language breathes again.”

* **Reconnection** — Youth rediscover roots through digital storytelling.
* **Representation** — Voices of the North are heard, respected, and preserved.
* **Resilience** — Technology serves culture, not the other way around.

---

## 🚀 Roadmap
| Phase | Description |
|--------|-------------|
| **1. Foundation** | MVP for Northern communities — offline storytelling with basic transcription. |
| **2. Expansion** | Integrate AI transcription for Indigenous languages; community co-design. |
| **3. Partnerships** | Collaborate with schools, museums, and heritage councils across Canada. |
| **4. National Archive** | Grow into a living repository of Canadian Indigenous voices. |

---

## 💰 Initial Funding & Impact Model
| Source | Amount (CAD) | Purpose |
|--------|---------------|----------|
| Government Grant (Indigenous Services Canada) | $50,000 | Launch + Infrastructure |
| Heritage Program (Museums Assistance) | $10,000 | Community Support |
| University Partnerships | In-kind | Development + Research |
| **Total Allocation:** | **$16,500** | Development, Equipment, Elder Honoraria, Maintenance |

---

## 📈 Sustainability Model
- **Free Access** for Indigenous communities  
- **Subscription Access** ($10–$500/month) for educators, researchers, and NGOs  
- **Partnerships & Grants** with heritage and culture councils  

---

## 🧭 Marketing & Outreach
- Social media campaigns (TikTok, Instagram, YouTube)  
- Community workshops and town halls  
- Academic collaborations and NGO presentations  

---

## 💬 Join Us
> “When a language dies, we lose unique ways of understanding the world.”

| For Communities | For Partners | For Funders | For Schools |
|-----------------|---------------|--------------|--------------|
| Preserve your stories | Collaborate on cultural programs | Invest in heritage tech | Engage students in living history |

---

## 🛠️ Contributors
- **Sabrina M.** — Project Lead / Developer  
- IEEE November 2025 Hackathon Team  
- Indigenous Elders & Youth collaborators  
- Technical support by Conestoga AIML community

---

## 🪶 Acknowledgements
We gratefully acknowledge the Indigenous storytellers and communities who inspire this project.  
Special thanks to IEEE Hackathon mentors, Streamlit open-source contributors, and all those keeping northern voices alive.

---

## 🪄 License
This project is released under the **MIT License** — freely available for educational and cultural use.

---

### 🌌 “Small actions keep big traditions alive.”
