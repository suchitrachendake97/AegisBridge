# 🌉 AegisBridge — AI-Based Bridge Health Monitoring System

A powerful **AI-powered bridge structural health monitoring system** built using **HTML, CSS, JavaScript, Python, and the OpenRouter API**.
This project provides an intelligent inspection assistant that analyzes bridge photographs, detects structural damage, and delivers detailed engineering reports in real time through a simple web interface.
The system runs locally and communicates with the **Google Gemini 2.0 Flash Vision AI (via OpenRouter)** to generate accurate damage assessments aligned with Indian engineering standards.

---

## 🚀 Features

* 🔬 Real-time AI visual inspection of bridge images
* ⚡ Fast analysis — results in under 10 seconds
* 🌐 Simple browser-based web interface
* 🧠 AEGIS — conversational AI assistant for engineering Q&A
* 📊 Bridge Health Score (0–100) with severity & risk classification
* 🔧 IRC / IS / RDSO standard-compliant remediation plans
* 🎙️ Voice input / output for hands-free field operation
* 📁 Bulk image upload for multi-structure analysis
* 🖥️ Runs locally with Python (no installation required)
* 📦 Lightweight single-file project structure

---

## 🛠️ Technologies Used

* **HTML5 / CSS3 / JavaScript (Vanilla ES6+)**
* **Google Gemini 2.0 Flash Vision AI**
* **OpenRouter API (OpenAI-compatible)**
* **Python 3 (http.server — built-in)**
* **Web Speech API (Voice Input/Output)**
* **Browser FileReader API (Base64 image encoding)**
* **Windows Batch Script (.bat)**

---

## 📂 Project Structure

```
AegisBridge
│
├── AegisBridge.html
├── server.py
├── run.bat
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/suchitrachendake97/AegisBridge.git
```

Move into the project folder:

```
cd AegisBridge
```

No additional dependencies to install — Python 3 is all you need.

---

## ▶️ Run AegisBridge

Start the local server:

```
python server.py
```

You will see:

```
AegisBridge Proxy Server (Python)
URL  ➜  http://localhost:5000
```

Open your browser and go to:

```
http://localhost:5000
```

---

## 🔑 API Setup (OpenRouter)

AegisBridge uses the **OpenRouter API** to access Google Gemini 2.0 Flash Vision AI.
OpenRouter is a free gateway that gives you access to 300+ AI models through a single API key.

---

### 📥 Step 1 — Get Your Free API Key

1. Open your browser and go to:
   ```
   https://openrouter.ai
   ```

2. Click **Sign Up** and create a free account (Google login supported)

3. After logging in, go to:
   ```
   https://openrouter.ai/keys
   ```

4. Click **Create Key**

5. Give it a name (e.g. `AegisBridge`) and click **Create**

6. **Copy the key**


> ⚠️ Save this key somewhere safe. You won't be able to see it again after closing the page.

---

### 📋 Step 2 — Paste Your Key Into AegisBridge

1. Start the server and open the app in your browser:
   ```
   http://localhost:5000
   ```

2. Click the **⚙️ API Setup** button in the **top right corner** of the screen

3. In the popup modal that appears:
   - **Paste your key** into the `OpenRouter API Key` field
   - **Select your model** — choose `google/gemini-2.0-flash-001` (Free · Recommended)
   - Click **💾 Save & Activate**

4. You will see a confirmation message in the chat:
   ```
   ✅ Ready! Running google/gemini-2.0-flash-001.
   ```

---

### 🤖 Which AI Model to Use?

| Model | Cost | Best For |
|---|---|---|
| `google/gemini-2.0-flash-001` | ✅ FREE | Fast analysis — **Recommended** |
| `google/gemini-flash-1.5` | ✅ FREE | Stable alternative |
| `meta-llama/llama-3.2-11b-vision-instruct:free` | ✅ FREE | Backup option |
| `anthropic/claude-3.5-sonnet` | 💰 Paid | Most detailed analysis |

> 💡 All **FREE** models support image vision and work perfectly for bridge inspection.

---

### 🔐 Is My Key Safe?

* Your API key is stored **only in your browser's localStorage**
* It is **never sent to any server** other than OpenRouter directly
* No backend, no database, no third-party storage
* You can change or remove your key anytime from the **⚙️ API Setup** button

---

## 🧠 AI Capabilities

The system is powered by **Google Gemini 2.0 Flash Vision** and is designed to behave like an expert bridge structural inspector:

* Detects cracks (hairline, fine, medium, wide)
* Identifies corrosion, spalling, exposed rebar, and deformation
* Generates a **Bridge Health Score (0–100)**
* Classifies damage: **NONE / MINOR / MODERATE / SEVERE / CRITICAL**
* Assigns risk level: **LOW / ELEVATED / CRITICAL**
* Provides **IRC:SP:35 / IS:456 / IS:1893 / RDSO** compliant remediation plans
* Answers engineering questions in natural language (multi-turn chat)

---

## 📌 Example Conversation

User sends a bridge image and asks:

```
Analyze this bridge and tell me about the damage.
```

AEGIS responds:

```
I can see significant diagonal cracking on the pier face,
approximately 0.5–1mm wide, indicating moderate shear stress.
There is also surface corrosion staining near the waterline.

Health Score: 58 / 100
Severity: MODERATE
Risk Level: ELEVATED

Recommended Actions:
- Immediate: Document crack locations with measurements
- Short-term (30 days): Epoxy injection and surface sealing
- Long-term: Full NDT assessment per IRC:SP:35
```

User:

```
What is epoxy injection?
```

AEGIS:

```
Epoxy injection is a crack repair technique where low-viscosity
epoxy resin is injected under pressure into cracks to restore
structural integrity. It is specified under IS:456 for concrete
repairs and is suitable for cracks between 0.05mm and 6mm wide.
```

---

## 💻 Run with One Click (Windows)

You can also start AegisBridge using:

```
run.bat
```

This will:

* Detect Python automatically
* Start the local server at `http://localhost:5000`
* Automatically open the AegisBridge interface in your browser

---

## 📊 Key Outcomes

| Metric | Achievement |
|---|---|
| Analysis Time | < 10 seconds per image |
| Deployment Cost | Zero — free API tier |
| Damage Categories | Cracks, Corrosion, Spalling, Rebar, Deformation |
| Health Score | 0–100 with confidence percentage |
| Severity Levels | NONE / MINOR / MODERATE / SEVERE / CRITICAL |
| Standards Covered | IRC:6, IRC:21, IRC:SP:35, IS:456, IS:1893, RDSO |
| Voice Support | Input + Output (Chrome / Edge) |
| Accessibility | Any modern browser — laptop or smartphone |

---

## 📜 License

This project is released under the **MIT License**.

---

## 👨‍💻 Author

**Suchitra Chendake**
GitHub:
https://github.com/suchitrachendake97
