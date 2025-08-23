# Network Security Website Classification ML Project

**End-to-End Machine Learning Project with MLOps & Cloud Deployment**

This project predicts whether a website is **malicious or safe** based on multiple features. It implements a **full ML lifecycle**, from **data ingestion** to **deployment**, and demonstrates **MLOps practices** including experiment tracking, API serving, containerization, and CI/CD.

---

## **Features** ✅

- **Data Ingestion & Validation**  
  - Fetches data from a **MongoDB cluster**.  
  - Implements **schema validation** for data integrity.  

- **Exploratory Data Analysis & Feature Engineering**  
  - Performs comprehensive **EDA**.  
  - Applies **data transformations** and **feature engineering** to enhance model performance.  

- **Model Development**  
  - Trains multiple ML algorithms with **hyperparameter tuning**.  
  - Selects the **best-performing model** based on evaluation metrics.  

- **Experiment Tracking**  
  - Uses **MLflow** & **DagsHub** to log experiments, track metrics, and manage model versions.  

- **Model Serving & APIs**  
  - Provides a **FastAPI REST interface** for real-time predictions.  
  - Allows model inference through HTTP requests.  

- **Cloud Deployment & MLOps**  
  - Stores models in **AWS S3**.  
  - Builds **Docker images** and pushes to **AWS ECR**.  
  - Deploys the application on **AWS EC2** with **GitHub Actions CI/CD** automation.  

---

## **Tech Stack**

- **Programming Languages & Libraries:** Python, Pandas, NumPy, Scikit-Learn, FastAPI  
- **Databases:** MongoDB  
- **Experiment Tracking & Versioning:** MLflow, DagsHub  
- **Cloud & Deployment:** AWS (S3, ECR, EC2), Docker  
- **CI/CD:** GitHub Actions  

---

## **Project Workflow**

1. **Data Ingestion:** Pull raw data from MongoDB.  
2. **Validation:** Check schema and ensure data quality.  
3. **EDA & Feature Engineering:** Explore, clean, and transform data.  
4. **Model Training:** Train multiple algorithms and tune hyperparameters.  
5. **Experiment Tracking:** Log metrics and track models with MLflow & DagsHub.  
6. **Model Serving:** Create REST endpoints using FastAPI for real-time predictions.  
7. **Deployment:** Push model to AWS S3, Dockerize, push image to AWS ECR, and deploy on EC2.  
8. **CI/CD:** Automate deployment and updates using GitHub Actions.  

---

## **Outcome**

- Fully implemented **end-to-end ML lifecycle** from **data ingestion → validation → EDA → model development → API serving → deployment**.  
- Practiced **MLOps principles**, including experiment tracking, containerization, cloud deployment, and automated CI/CD.  
- Built a **production-ready ML application** with real-time prediction capabilities.

---

## **Takeaways**

- Practical understanding of **ML pipelines in production**.  
- Hands-on experience with **FastAPI for model serving**.  
- Expertise in **cloud deployment (AWS), Docker containerization, and CI/CD automation**.  
- Improved skills in **experiment tracking, model versioning, and MLOps best practices**.
