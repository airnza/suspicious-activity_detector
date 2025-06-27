# 🛡️ Suspicious Activity Detector

Detect suspicious user behavior with Python 🐍, pandas 🧠, and visual analytics 📊. Built for aspiring Data Scientists and Trust & Safety professionals.

---

## 🚀 What This Project Does

✅ Detects multi-IP logins from same user within 5 minutes  
✅ Flags users making large transactions too soon after signing up  
✅ Highlights login trends by hour  
✅ Uses real-world patterns from fraud, abuse & moderation scenarios  
✅ Bonus notebook with 3 additional Trust & Safety rules

---

## 📁 Project Structure
```
SuspiciousActivityDetector/
├── data/                 # Sample CSVs: users, logins, payments
├── notebooks/            # Jupyter notebooks (EDA + logic)
│   ├── 01_EDA.ipynb
│   ├── 02_Suspicious_Patterns.ipynb
│   └── 03_Additional_Rules.ipynb
├── suspicious_activity.py # Standalone detection script
├── requirements.txt      # Python dependencies
├── README.md             # Project overview (you are here!)
├── LICENSE               # MIT License
└── .gitignore            # Files to exclude from Git
```

---

## 🧰 Tech Stack
- `Python` – scripting & analysis
- `pandas` – data manipulation
- `matplotlib / seaborn` – visualization
- `Jupyter Notebook` – interactive workflows
- `Git + GitHub` – version control & portfolio

---

## 🛠️ Setup Instructions

### 🐍 1. Clone and Install
```bash
git clone https://github.com/YOUR_USERNAME/SuspiciousActivityDetector.git
cd SuspiciousActivityDetector
pip install -r requirements.txt
```

### 🧪 2. Explore the Notebooks
```bash
jupyter notebook
```
Open these notebooks in order:
- `01_EDA.ipynb` → 📊 Explore login/payment patterns
- `02_Suspicious_Patterns.ipynb` → 🕵️‍♂️ Detect suspicious logins
- `03_Additional_Rules.ipynb` → ⚠️ Extra detection logic

### 🧾 3. Or Run Script (CLI mode)
```bash
python suspicious_activity.py
```

---

## 💡 Additional Rules (Notebook 3)
- Detect **fast large payments** after signup
- Find **shared IPs across accounts**
- Flag users using **>3 devices per day**

📁 Implemented in `03_Additional_Rules.ipynb`

---

## 📈 Sample Output Examples
```text

Suspicious users from IP-switching: [1]

⚠️ Users with fast large payments:
   user_id  amount           delay
0        1     999 0 days 00:08:00
1        2    1500 0 days 00:05:00

⚠️ Shared IPs used by multiple users:
    ip_address  num_users
0  80.100.24.1          2

⚠️ Users with more than 3 devices in a day:
   user_id        date  device
0        1  2023-01-05       4
```

---

## 📜 License
This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for full details.

---

## 🌟 Contribute or Star
If you found this helpful:
- ⭐ Star this repo on GitHub
- 🛠️ Fork it and build your own variant
- ✅ Try adding new rules, ML anomaly detection, or dashboards!