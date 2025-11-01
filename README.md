# 🏨 HOTELREVAI  
### 💡 *AI-Driven Revenue Analysis for Hotels*

---

## 🌐 Overview  
**HOTELREVAI** is an **AI-powered Business Intelligence solution** that helps hotels **analyze, predict, and optimize** their performance.  
It tracks key KPIs like **Occupancy Rate, Revenue, and Guest Behavior**, using **Power BI** and **Python** to transform raw booking data into actionable insights and future forecasts.

> 🧭 *From data cleaning to forecasting — one platform for smarter hotel decisions.*

---

## ⚙️ Key Features  
✨ **Dynamic Power BI Dashboards** – Interactive visual analytics  
📊 **Real-Time KPI Tracking** – Occupancy %, ADR, RevPAR  
🧹 **Automated Data Cleaning & Modeling**  
🧠 **AI Forecasting (Prophet)** – Predict revenue & occupancy for 90 days  
🧍‍♀️ **Guest Segmentation** – Personas for targeted marketing  
💰 **Data-Driven Pricing & Promotion Suggestions**

---

## 🧠 Tech Stack  

| Category | Tools / Libraries |
|-----------|-------------------|
| 💻 Business Intelligence | Power BI |
| 🔄 Data Transformation | Power Query |
| 🐍 Programming | Python |
| 📦 Libraries | Pandas, NumPy |
| 🔮 Forecasting | Facebook Prophet |
| 🌐 Web App | Streamlit |

---

## 🧩 Data Workflow  

### 🧾 Dataset Overview  
- Booking ID, Customer ID, Room Type, Booking Dates, and Payment Details  
- Cleaned for **missing values**, **duplicates**, and **incorrect data types**

### 🧱 Star Schema Design  
- **Fact Table:** `Fact_Bookings` (transactions)  
- **Dimension Tables:** Guests, Rooms, Hotels, Dates, Booking Source  
- **Relationships:** One-to-Many for integrity & consistent analysis  

---

## 📈 Key Metrics  

| Metric | Description |
|---------|--------------|
| 🏠 **Occupancy %** | Percentage of rooms occupied |
| 💸 **ADR (Average Daily Rate)** | Avg. revenue per occupied room |
| 📊 **RevPAR** | Revenue per available room (ADR × Occupancy) |
| 📅 **Booking Duration** | Length of stay per guest |

---

## 🧱 Project Milestones  

### 🏁 **Milestone 1 – Data Foundation**
✔️ Cleaned and transformed hotel booking data  
✔️ Built **Star Schema** model and validated relationships  

### 📊 **Milestone 2 – Dashboard Creation**
✔️ Built **interactive Power BI dashboard**  
✔️ Displayed metrics: Occupancy %, ADR, RevPAR  
✔️ Seasonal and room-type trend analysis  

### 🧍 **Milestone 3 – Guest Segmentation**
✔️ Created **guest personas**: *Family Loyalist, Solo Explorer, Corporate Guest*  
✔️ Derived insights for **personalized marketing**  

### 🔮 **Milestone 4 – AI Forecasting**
✔️ Used **Facebook Prophet** to predict occupancy, cancellations & revenue  
✔️ Created **cancellation heatmaps** and **lead time analysis**  

### 💹 **Milestone 5 – Final Integration**
✔️ Combined insights into a **single dynamic dashboard**  
✔️ Added **pricing tiers, upsell offers & seasonal promotions**

---

## 🤖 AI Forecasting Module  
> *Powered by Facebook Prophet*

🔍 Loads and cleans booking data  
📆 Groups by reservation date for time-series modeling  
📈 Identifies **seasonal trends & patterns**  
📊 Displays forecasts in **Streamlit** with summary metrics and downloadable CSVs  

🧠 Helps hotel managers:  
- Adjust pricing dynamically  
- Predict demand peaks & lows  
- Reduce cancellations  
- Improve overall revenue efficiency  

---

## 💼 Business Impact  
💰 **Smarter Pricing & Promotions**  
📅 **Accurate Demand Forecasting**  
🎯 **Targeted Marketing Campaigns**  
🙌 **Higher Guest Satisfaction & Profitability**  
🚀 **Foundation for AI-Driven Dynamic Pricing**

---

## 🏆 Project Conclusion  
| Milestone | Achievement |
|------------|-------------|
| **1** | Cleaned & modeled booking data |
| **2** | Created Power BI dashboards |
| **3** | Built guest personas for marketing |
| **4** | Developed forecasting models |
| **5** | Integrated all dashboards & insights |

> 🎯 *End result: A fully functional BI + AI system enabling data-driven hotel management.*

---

## 🖼️ Dashboard Preview  
📷 *Add screenshots of Power BI dashboards & Streamlit app here*  
*(e.g., `![Dashboard Preview](images/dashboard.png)`)*
  
---

## 🧾 How to Run the Project  

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-username/HOTELREVAI.git
cd HOTELREVAI

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run the Streamlit app
streamlit run hotel_deshboard.py
