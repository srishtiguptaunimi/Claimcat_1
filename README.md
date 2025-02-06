# 📌 Project Name: Complaint Processing with AI-Powered Classification System

## 🚀 Overview
Claimcat_1 is an AI-driven complaint categorization system designed to assist **Bundesnetzagentur (BNetzA)** in classifying consumer complaints efficiently. The system utilizes **Natural Language Processing (NLP)** models deployed on **AWS SageMaker** to automate the categorization process, reducing response time and workload for employees.

## 📡 Features
✅ Automated complaint categorization into **Process, Type, and Content levels**  
✅ **Multi-label classification** for complaints covering multiple categories  
✅ **REST API-based integration** with existing BNetzA workflows  
✅ **AWS Lambda & SageMaker-based deployment**  

## 🏗 System Architecture
<img width="546" alt="image" src="https://github.com/user-attachments/assets/0f8355cc-d28e-4704-89c1-9a8af9019e3c" />
 
- **Frontend**: Users submit complaints via web forms, emails, or letters.  
- **Backend**: AWS Lambda processes the request and sends it to **SageMaker** for inference.  
- **AI Model**: NLP-based classifier predicts complaint categories with confidence scores.  
- **API Response**: Returns structured categorization results.  

## 📡 API Endpoints
| Endpoint | Description |
|----------|------------|
| `/process-categorization` | Classifies complaints as **Strom, Gas, Sostinges.** |
| `/type-categorization` | Identifies **** |
| `/content-categorization` | Categorizes **.** |

### 📥 Example API Request
```json
{
    "text": "I have issues with my electricity bill and connection."
}
```

### 📤 Example API Response
```json
{
    "process_category": "Energy",
    "type_category": "Inquiry",
    "content_categories": ["Electricity", "Billing", "Network Connection"],
    "confidence_scores": [98.3, 95.5, 92.1]
}
```

## 🔧 Installation & Setup
### 1️⃣ Clone the repository
```bash
git clone https://github.com/srishtiguptaunimi/Claimcat_1.git
cd Claimcat_1
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Deploy on AWS Lambda
1. Set up an AWS account.
2. Create an **IAM Role** with permissions for **SageMaker & Lambda**.
3. Deploy Lambda using AWS CLI or the console.
4. Update API Gateway to expose endpoints.

## 🛠 Model Training & Deployment
- The NLP model is trained using **consumer complaint data**.
- Fine-tuned using **SageMaker PyTorch models**.
- Supports **multi-class classification** with confidence scores.
- **Deployment:** The model is hosted on **AWS SageMaker Inference Endpoint**.

## 🧪 Running Tests
- **Unit Tests:**
```bash
pytest tests/
```
- **API Testing:**
Use **Postman** or `curl`:
```bash
curl -X POST "https://your-api-endpoint.com/process-categorization"      -H "Content-Type: application/json"      -d '{"text": "I have issues with my gas bill"}'
```

## 🤝 Contribution Guidelines
We welcome contributions! To contribute:
1. **Fork** this repository.
2. Create a new **feature branch**: `git checkout -b feature-name`
3. **Commit changes**: `git commit -m 'Add new feature'`
4. **Push**: `git push origin feature-name`
5. Create a **Pull Request**.

## 📜 License
This project is licensed under the **MIT License**.

## 📩 Contact & Support
For questions, reach out via **GitHub Issues** or email: `srishtigupta@studenti.unimi.it` 

## 🚀 Future Enhancements
- ✅ Improve **multi-label classification** for complex complaints.
- ✅ Build a **FastAPI frontend** for better integration.
- ✅ Add **automated model retraining** pipeline using AWS Lambda.

---
💡 **Developed by:** *ClaimCat Team* | *Powered by AWS SageMaker, Bedrock & Lambda* 🚀
