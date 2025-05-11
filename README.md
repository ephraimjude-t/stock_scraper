# 📈 Stock Scraper (Top Gainers & Losers)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-06B6D4?style=for-the-badge&logo=tailwindcss)

---

## 🛠️ Built With
- FastAPI (Backend)
- React (Frontend)
- TailwindCSS
- yFinance API
- Axios (for API requests)

---

## 🚀 Features
- Scrapes Top Gainers and Top Losers from the stock market (live data)
- FastAPI serves the data through a REST API
- React frontend fetches and displays the data
- Clean, responsive UI with TailwindCSS

> ⚡ Note: This project does **NOT** use AI. It is purely a data scraper and display system.


---

## 📂 How to Run Locally

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
---
Frontend
cd frontend
npm install
npm run dev
