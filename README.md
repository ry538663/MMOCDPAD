# MMOCDPAD-DRL: Anomaly Detection in Zero Trust Security

An enterprise-grade, research-paper-based cybersecurity platform implementing **Matyas-Meyer Oseas (MMO)** compression-based device profiling and **Deep Reinforcement Learning (DRL)** for anomaly detection in IIoT Zero Trust Networks.

## 🚀 Latest Production Enhancements
- **Real Dataset Integration**: Full support for **X-IIoTID** and **CIC IoT 2022** datasets. The system now trains and predicts based on real Kaggle data patterns.
- **Dynamic Analytics**: Real-time graphs for **False Positive Rate (FPR)**, **Latency**, **Integrity**, and **Confidentiality** connected directly to system logs.
- **Secure Admin Panel**: A dedicated `/admin` dashboard to manage devices, upload datasets, and retrain AI models in the background.
- **WebSocket Live Feed**: Instantaneous "Security Alert" notifications and packet flow updates using `Flask-SocketIO`.
- **Advanced Reporting**: Programmatic PDF report generation with professional formatting and security metrics.
- **High-Contrast UI**: Optimized visibility for dark-themed dashboard with bright cyan and white text elements.
- **Multi-Port Support**: Configured to run on **Port 5005** to avoid conflicts with macOS AirPlay (Port 5000).

## 🛠️ Core Architecture
1. **Device Input**: Real-time ingestion of IoT traffic patterns (X-IIoTID based).
2. **MMO Module**: Compression-based hashing using **SPN block cipher** for data integrity.
3. **Profiling Engine**: **Random Forest** classification to generate behavioral trust scores.
4. **DRL Module**: **DQN (Deep Q-Network)** agent making autonomous "Allow/Deny" access decisions.
5. **SOC Dashboard**: Enterprise-grade monitoring of AI decisions, trust trends, and network health.

## 📦 Installation & Setup

### Prerequisites
- Python 3.9+
- Pip (Python Package Manager)

### Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ry538663/MMOCDPAD.git
   cd MMOCDPAD
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the AI models (Initial):
   ```bash
   python train.py
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Access the dashboard at **`http://127.0.0.1:5005`**
   - **Admin User**: `admin`
   - **Password**: `admin123`

## 📊 Analytics
The system provides 4 key research metrics:
1. **False Positive Rate (FPR)**: Demonstrates AI learning progress (Graph goes down over time).
2. **Data Confidentiality Rate**: Achieved via MMO-SPN construction.
3. **Data Integrity Rate**: Success rate of cryptographic verification.
4. **Network Access Time**: Actual system latency (ms) for authentication and AI decision making.

## 🐳 Docker Deployment
```bash
docker-compose up --build
```

## 📖 Research Reference
Based on the IEEE paper: *“Matyas-Meyer Oseas Compression-Based Device Profiling for Anomaly Detection via Deep Reinforcement Learning in Zero Trust Security Network (MMOCDPAD-DRL)”*
