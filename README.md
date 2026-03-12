# AI-Enabled Parametric Insurance Platform for Gig Workers

## 1. Problem Statement

India’s platform-based delivery partners (Swiggy, Zomato, Zepto, Amazon, Dunzo etc.) are the backbone of the country’s fast-paced digital economy. However, their income is **directly dependent on working hours and delivery availability**.

External disruptions such as:

* Extreme rainfall
* Heat waves
* Flooding
* Cyclones
* Severe pollution (high AQI)
* Road closures or natural disasters

can significantly reduce delivery activity. When these events occur, gig workers often **lose 20–30% of their weekly income** because they are unable to work or because customer demand drops.

Currently, **there is no insurance product designed to protect gig workers from temporary income loss caused by environmental disruptions**. Traditional insurance products do not cover such scenarios.

Our solution proposes an **AI-enabled parametric insurance platform** that automatically compensates gig workers when external disruptions reduce their ability to work.

---

# 2. Persona-Based Scenario

### Persona: K. Suresh

* Age: 35
* Occupation: Delivery Partner
* Platform: Swiggy
* City: Vijayawada
* Average Weekly Income: ₹6,500 – ₹7,500
* Working Hours: ~8–10 hours/day

### Real Issue Identified

During the interview with K. Suresh, he highlighted that **extreme weather conditions significantly reduce his working hours**.

Examples:

**Scenario 1 – Heavy Rainfall**

Heavy rainfall for an entire day leads to:

* Reduced delivery orders
* Unsafe driving conditions
* Temporary road flooding

Result:

* He works only **3–4 hours instead of 8–10 hours**
* Income drops by **₹600–₹900 for that day**

---

**Scenario 2 – Severe Heatwave**

During extreme heat:

* Many delivery workers reduce outdoor working hours
* Demand fluctuates
* Workers stop working during afternoon peak heat

Result:

* Lost deliveries
* Reduced income for that day

---

**Scenario 3 – Cyclone or Flood Warning**

Platforms sometimes temporarily halt delivery operations for safety.

Result:

* Entire day income lost

---

### Core Need

Gig workers require a **simple protection mechanism that compensates them when environmental disruptions reduce their ability to work.**

---

# 3. Solution Overview

We propose an **AI-Enabled Parametric Insurance Platform** specifically designed for gig workers.

Key characteristics:

* Automated policy enrollment
* Weekly premium pricing aligned with gig worker income cycles
* Parametric triggers based on environmental disruptions
* Automatic claim generation
* Instant payouts without manual claim filing

This system ensures that **workers receive compensation when predefined external conditions occur**, without needing to submit claims manually.

---

# 4. Platform Choice (Web vs Mobile)

For the MVP we propose a **Web Platform**.

### Reasons

1. Faster development and deployment
2. Easier integration with backend APIs
3. Suitable for demonstration and analytics dashboards
4. Accessible across devices without app installation

In the future, the system can evolve into a **mobile application** since delivery partners primarily use smartphones.

---

# 5. Weekly Premium Model

Gig workers are typically paid **weekly or daily**, therefore the insurance pricing must match their earnings cycle.

### Premium Calculation Logic

Weekly premium is calculated based on:

* Average weekly income
* Environmental disruption risk
* Expected income loss probability

Formula:

Weekly Premium = (Expected Weekly Income Loss × Risk Margin)

Example:

Average Weekly Income: ₹7000
Predicted Income Loss Risk: 20%

Expected Loss:

₹7000 × 0.20 = ₹1400

If the risk margin is 10%:

Weekly Premium:

₹1400 × 0.10 = ₹140 per week

This model ensures:

* Affordable pricing
* Fair risk distribution
* Alignment with worker income cycles

---

# 6. Parametric Triggers

Parametric insurance relies on **predefined environmental triggers** rather than manual claims.

### Example Trigger Conditions

| Event                | Trigger Condition                |
| -------------------- | -------------------------------- |
| Heavy Rainfall       | Rainfall > 60mm/day              |
| Severe Air Pollution | AQI > 400                        |
| Cyclone Alert        | Government disaster alert issued |
| Flood Warning        | Regional flood advisory          |
| Extreme Heatwave     | Temperature > 45°C               |

When these conditions occur within the worker’s operational zone, the system automatically triggers a **claim event**.

---

# 7. Automated Workflow

The application workflow operates as follows:

### Step 1 — Worker Onboarding

Worker registers and provides:

* City
* Platform (Swiggy, Zomato etc.)
* Average weekly income
* Working hours

---

### Step 2 — Risk Profiling

AI models analyze:

* Regional weather history
* Pollution levels
* Disaster frequency
* Traffic conditions

A **risk score** is generated for that worker’s region.

---

### Step 3 — Weekly Policy Creation

Based on risk score:

* Weekly premium is calculated
* Coverage limits are defined
* Policy is activated

---

### Step 4 — Real-Time Monitoring

The system continuously monitors:

* Weather APIs
* AQI data
* Disaster alerts
* Traffic conditions

---

### Step 5 — Parametric Trigger Detection

If predefined trigger thresholds are crossed:

Example:

Heavy rainfall detected in the worker’s delivery zone.

The system automatically identifies affected policies.

---

### Step 6 — Automatic Claim Creation

Claims are generated automatically without requiring manual submission.

---

### Step 7 — Fraud Detection

AI models validate claims using:

* Worker location verification
* Activity validation
* Duplicate claim detection
* Anomaly detection

---

### Step 8 — Instant Payout

If the claim is validated:

* Payout is automatically initiated
* Funds transferred via UPI or digital wallet

---

# 8. AI / Machine Learning Integration

Artificial Intelligence is integrated into multiple stages of the platform to improve **risk estimation, premium pricing, claim validation, and fraud detection**. The system uses different machine learning models for different tasks.

---

## 8.1 Risk Assessment Model

The Risk Assessment Model estimates the **probability that environmental conditions in a specific region will disrupt gig worker activity**.

### Algorithm Used

**XGBoost (Extreme Gradient Boosting)**

XGBoost is chosen because it performs very well on structured datasets such as environmental and operational data.

### Why XGBoost?

- Handles **non-linear relationships** between environmental variables and delivery disruptions.
- Works well with **tabular data** such as weather and pollution datasets.
- Provides **feature importance scores**, helping explain which factors affect disruption risk.
- Efficient and scalable for real-time prediction.

### Input Features

The model uses environmental and contextual features such as:

- Rainfall intensity (mm)
- Temperature
- Air Quality Index (AQI)
- Wind speed
- Historical disaster events
- Traffic congestion levels
- Seasonal indicators (month, monsoon period)
- City / delivery zone

### Model Output

The model produces a **Risk Score between 0 and 1**.

Example:

| City | Rainfall | AQI | Risk Score |
|------|----------|-----|-----------|
| Vijayawada | 70mm | 130 | 0.72 |
| Hyderabad | 15mm | 90 | 0.18 |

This score represents the **probability that environmental conditions will reduce delivery activity**.

The risk score is then used for **weekly premium calculation and disruption monitoring**.

---

## 8.2 Income Loss Prediction Model

The Income Loss Prediction Model estimates **how much income a gig worker is likely to lose during a disruption event**.

### Algorithm Used

**Random Forest Regressor**

Random Forest is used because it can capture complex relationships between environmental conditions and worker activity.

### Why Random Forest?

- Works well with **non-linear relationships**
- Robust against **overfitting**
- Performs well on **medium-sized tabular datasets**
- Provides stable predictions even with noisy data

### Input Features

The model considers both worker and environmental variables:

- Average weekly income
- Average deliveries per hour
- Working hours per day
- Rainfall intensity
- AQI levels
- Temperature
- Traffic congestion
- Disaster alerts
- Time of day / seasonal patterns

### Model Output

The model predicts the **expected income loss amount**.

Example:

| Weekly Income | Rainfall | AQI | Predicted Income Loss |
|--------------|----------|-----|-----------------------|
| ₹7000 | 65mm | 120 | ₹820 |

This value is used to:

- Calculate **weekly premiums**
- Determine **automatic payout amounts**

---

## 8.3 Fraud Detection System

The Fraud Detection System identifies **suspicious or abnormal claim patterns**.

### Algorithm Used

**Isolation Forest (Anomaly Detection)**

Isolation Forest is a machine learning algorithm specifically designed for detecting anomalies in datasets.

### Why Isolation Forest?

- Efficient for detecting **rare fraudulent events**
- Works well with **high-dimensional data**
- Requires **minimal labelled fraud data**
- Suitable for real-time anomaly detection

### Fraud Signals Monitored

The model evaluates several indicators:

- Duplicate claims in short time intervals
- Location mismatch between worker and disruption event
- Unusual claim frequency
- Claim amount anomalies
- Activity mismatch (worker inactive during disruption)

### Model Output

The model produces a **fraud probability score**.

Example:

| Claim ID | Fraud Score | Status |
|----------|-------------|--------|
| 1021 | 0.12 | Valid |
| 1045 | 0.87 | Suspicious |

Claims with high fraud scores are **flagged for additional verification before payout**.
# 9. Technology Stack

### Frontend

React (JSX)

Features:

* Worker onboarding
* Policy dashboard
* Claim history
* Risk alerts
* Analytics dashboard

---

### Backend

FastAPI (Python)

Handles:

* Business logic
* AI model integration
* API endpoints
* automation workflows

---

### Database

MySQL

Stores:

* Users
* Risk profiles
* Policies
* Claims
* Payouts
* Premium history

---

### External Integrations

* Weather APIs
* Pollution APIs
* Traffic APIs (mock)
* Payment gateway (sandbox/mock)

---

### AI Tools

* Python
* Scikit-Learn
* XGBoost
* Pandas
* NumPy

---

# 10. Development Plan

### Phase 1 — Core Platform

* User onboarding
* Policy creation
* Weekly premium calculation
* Dashboard UI

---

### Phase 2 — Parametric Monitoring

* Weather API integration
* Trigger detection system
* Automated claim creation

---

### Phase 3 — AI Integration

* Risk prediction model
* Income loss prediction model
* Fraud detection system

---

### Phase 4 — Automation

* Real-time monitoring engine
* Automatic payouts
* Analytics dashboard

---

# 11. Expected Impact

This platform can:

* Provide financial stability to gig workers
* Reduce economic vulnerability caused by climate events
* Enable scalable micro-insurance products
* Promote responsible AI-driven financial protection

---

# 12. Conclusion

Gig workers form a critical component of India's digital economy, yet they remain financially vulnerable to environmental disruptions.

This project proposes an **AI-driven parametric insurance system** that automatically compensates workers for income loss caused by extreme weather and environmental events.

By combining **AI risk modeling, parametric triggers, automated claims, and weekly pricing**, the system aims to deliver a scalable and accessible financial safety net for gig workers.

