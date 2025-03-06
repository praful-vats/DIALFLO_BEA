# DIALFLO_BEA

A high-performance, scalable backend system for handling customer support queries. The system classifies user queries, fetches responses, caches frequent requests, and stores interactions efficiently.

---

## Tech Stack

- **Backend:** FastAPI (async API framework)
- **Database:** PostgreSQL (via SQLAlchemy)
- **Caching:** Redis (ElastiCache for AWS)
- **Task Queue:** Celery (for async order processing)
- **Deployment:** Docker, AWS (EC2, RDS, ElastiCache)
- **Logging & Testing:** Structured logs, unit tests with pytest

---

## Setup & Installation

### **1️⃣ Clone Repository**
```sh
git clone https://github.com/praful-vats/Diaflo_BEA.git
cd diaflo_bea
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file and add the following:
```env
DATABASE_URL=your_database_url
REDIS_URL=your_redis_url
```

### **5️⃣ Start the Server**
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
The server will run at: **http://localhost:8000**

---

## API Documentation

### **🔹 Process Query**
- **Endpoint:** `POST /query`
- **Description:** Classifies the query and returns a response.
- **Request Body:**
```json
{
  "customer_id": 1,
  "query": "Where is my order?"
}
```
- **Response:**
```json
{
  "customer_id": 1,
  "query": "Where is my order?",
  "query_type": "order_status",
  "response": "Your order is on the way!"
}
```

### **🔹 Get Interaction History**
- **Endpoint:** `GET /interactions/{customer_id}`
- **Description:** Fetches past interactions for a customer.
- **Response:**
```json
[
  {
    "id": 1,
    "customer_id": 1,
    "query": "Where is my order?",
    "query_type": "order_status",
    "response": "Your order is on the way!",
    "timestamp": "2024-03-06T12:00:00"
  }
]
```

---

## Running Tests

### **1️⃣ Install Test Dependencies**
```sh
pip install pytest httpx pytest-asyncio
```

### **2️⃣ Run Tests**
```sh
pytest -v
```

---

## Deployment

### **1️⃣ Build Docker Image**
```sh
docker build -t diaflo .
```

### **2️⃣ Run with Docker**
```sh
docker run -p 8000:8000 --env-file .env diaflo
```

### **3️⃣ Deploy on AWS EC2**
- Push the image to **AWS ECR**
- Run on **EC2 instance**
- Connect to **RDS (PostgreSQL)** & **ElastiCache (Redis)**
