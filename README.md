# 🚀 Spain Music Lifecycle Intelligence

**A data-driven analytics system to understand content maturity, lifecycle behavior, and playlist rotation dynamics in Spain’s Top 50 music charts.**

---

## 📌 Problem Statement

The Spanish music market behaves differently from global markets like the US/UK:

* Faster playlist rotation
* Strong preference for fresh releases
* Distinct behavior of explicit vs clean content
* Regional genre influence

Despite having daily Top 50 playlist data, there is **no lifecycle intelligence** to answer:

* How long do songs survive on the playlist?
* Do fresh releases dominate over mature tracks?
* What drives faster entry, peak, and decline?
* How does explicit content behave across lifecycle stages?
* Do singles outperform album tracks in longevity?

---

## 🎯 Objective

Build a **Content Lifecycle Intelligence System** to:

* Track song lifecycle from entry → peak → decline
* Measure playlist churn and rotation intensity
* Analyze content maturity patterns
* Identify drivers of retention and performance
* Enable data-driven release & marketing strategies

---

## 📂 Dataset Overview

| Column       | Description            |
| ------------ | ---------------------- |
| date         | Playlist snapshot date |
| position     | Rank (1–50)            |
| song         | Song title             |
| artist       | Artist name            |
| popularity   | Popularity score       |
| duration_ms  | Song duration          |
| album_type   | Single / Album         |
| total_tracks | Album size             |
| is_explicit  | Explicit content flag  |

---

## 🧠 Methodology

### 1. Data Preprocessing

* Standardized song & artist names
* Created unique `song_id`
* Ensured 50 entries per day
* Sorted time-series data

### 2. Lifecycle Engineering

For each song:

* Entry Date
* Exit Date
* Days on Playlist
* Peak Position
* Time to Peak

### 3. Lifecycle Stages

* **New Entry** → First 7 days
* **Growth Phase** → Improving rank
* **Peak Phase** → Top 10 stability
* **Mature Phase** → Stable mid ranks
* **Decline Phase** → Rank deterioration

### 4. Playlist Rotation Analysis

* Daily entry & exit tracking
* Churn Rate calculation
* Stability Index measurement
* Monthly rotation comparison

### 5. Content Maturity Analysis

* Explicit vs Non-explicit comparison
* Single vs Album lifecycle behavior
* Duration vs retention impact
* Album size vs stability

### 6. Popularity Dynamics

* Popularity vs lifecycle stage
* Peak popularity timing
* Growth & decay patterns

---

## 📊 Key Metrics (KPIs)

* **Average Days on Playlist** → Content longevity
* **Entry-to-Peak Time** → Growth speed
* **Playlist Churn Rate** → Rotation intensity
* **Retention Stability Index** → Durability
* **Explicit Content Lifecycle Score**
* **Single vs Album Longevity Ratio**

---

## 📈 Key Insights (Example)

* Spain playlists show **high churn → faster content turnover**
* Explicit songs tend to **peak faster but decay quicker**
* Singles dominate **early entry speed**
* Album tracks show **longer retention stability**
* Shorter songs tend to have **higher replay-driven retention**

---

## 🖥️ Streamlit Dashboard

Interactive analytics dashboard with:

* 📅 Date range selection
* 🔄 Playlist churn visualization
* 📊 Lifecycle stage distribution
* 🎵 Song lifecycle timeline
* ⚖️ Content comparisons (explicit, album type)

---

## 🛠️ Tech Stack

* Python (Pandas, NumPy)
* Streamlit


## 💡 Business Impact

This project enables:

* Smarter release timing strategies
* Optimized marketing investment windows
* Better balance between new vs catalog content
* Data-backed playlist pitching strategy

---

## 🔮 Future Improvements

* Genre-level lifecycle modeling
* Predictive survival analysis
* Hit probability scoring
* Cross-country comparison (Spain vs UK/US)

---

## 👤 Author

**Amit Kumar**
Aspiring Data Scientist | AI/ML Enthusiast
