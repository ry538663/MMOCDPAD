# MMOCDPAD-DRL: Anomaly Detection in Zero Trust Security

An enterprise-grade, research-paper-based cybersecurity platform implementing **Matyas-Meyer Oseas (MMO)** compression-based device profiling and **Deep Reinforcement Learning (DRL)** for anomaly detection in IIoT Zero Trust Networks.

## 🚀 Key Features
- **Matyas-Meyer-Oseas (MMO)**: Compression-based hashing using SPN block cipher for data integrity.
- **DQN-based Anomaly Detection**: Stable-Baselines3 DQN agent making autonomous access decisions.
- **Device Profiling**: RandomForestClassifier for generating trust-based behavioral profiles.
- **Production-Level Dashboard**: Modern, dark-themed, interactive SIH/IEEE-level dashboard.
- **Real-Time WebSockets**: Live packet monitoring and anomaly alerts without page refresh.
- **PDF Intelligence Reports**: Professional security report generation with data visualization.
- **Secure Authentication**: Bcrypt-hashed admin login and session management.

## 🛠️ Architecture
1. **Device Input**: Simulates IIoT devices sending traffic.
2. **Database Module**: Stores device metadata, trust scores, and anomaly logs.
3. **MMO Module**: Generates secure hashes for every data block.
4. **SPN Network**: Underlying block cipher for MMO construction.
5. **Profiling Engine**: Classifies device behavior.
6. **DRL Module**: Agent decides `Allow/Deny` based on current state (Trust, Traffic, Crypto).
7. **Dashboard**: Visualization of real-time decisions and historical analytics.

## 📦 Installation & Setup

### Prerequisites
- Python 3.9+
- Docker (Optional for containerized deployment)

### Local Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the AI models:
   ```bash
   python train.py
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Access the dashboard at `http://127.0.0.1:5000`
   - **User**: admin
   - **Pass**: admin123

### Docker Deployment
```bash
docker-compose up --build
```

## 📊 Analytics
The system provides 4 key research metrics:
1. **False Positive Rate (FPR)**: Comparison against traditional CNN models.
2. **Data Confidentiality Rate**: achieved via MMO-SPN encryption.
3. **Data Integrity Rate**: Successful integrity checks over time.
4. **Network Access Time**: Total latency in authentication and decision making.

## 📖 Research Reference
Based on: *“Matyas-Meyer Oseas Compression-Based Device Profiling for Anomaly Detection via Deep Reinforcement Learning in Zero Trust Security Network (MMOCDPAD-DRL)”*
