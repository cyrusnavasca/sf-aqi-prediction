customer-satisfaction-mlops-main/
│
├── README.md
├── requirements.txt
├── config.yaml
├── run_pipeline.py
├── run_deployment.py
├── streamlit_app.py
├── data/
│   └── olist_customers_dataset.csv
├── materializer/
│   └── custom_materializer.py
├── model/
│   ├── __init__.py
│   ├── data_cleaning.py
│   └── model_dev.py
├── pipelines/
│   ├── __init__.py
│   ├── deployment_pipeline.py
│   └── utils.py
├── saved_model/
│   └── model.pkl
├── steps/
│   ├── __init__.py
│   ├── clean_data.py
│   ├── config.py
│   ├── evaluation.py
│   ├── ingest_data.py
│   └── model_train.py
├── tests/
├── _assets/
│   ├── feature_importance_gain.png
│   ├── high_level_overview.png
│   └── training_and_deployment_pipeline_updated.png
└── .zen/
    └── config.yaml

Design & Implementation Summary

Pipeline Architecture:
The project uses ZenML to orchestrate a modular ML pipeline. Steps are defined for data ingestion, cleaning, model training, evaluation, and deployment.

Data Handling:
Data is loaded from olist_customers_dataset.csv.
Data cleaning is performed using strategy classes in data_cleaning.py (DataPreprocessStrategy, DataDivideStrategy, DataCleaning), which handle missing values, drop unnecessary columns, and split data for training/testing.

Model Development:
Multiple model classes are implemented in model_dev.py (RandomForest, LightGBM, XGBoost, LinearRegression), all inheriting from an abstract Model base class.
Hyperparameter tuning is supported via Optuna.

Pipeline Steps:
Each pipeline step is implemented in the steps directory as a ZenML step, e.g., clean_data, train_model, evaluation.

Materialization:
Custom serialization/deserialization of models and data is handled by cs_materializer.

Deployment:
Deployment logic is in deployment_pipeline.py, using MLflow for model serving and experiment tracking.

Streamlit UI: streamlit_app.py provides a user interface for predictions and visualizations.

Configuration:
Pipeline and experiment settings are managed via YAML files (config.yaml, .zen/config.yaml).

Summary:
The project is designed for modularity and reproducibility, leveraging ZenML for pipeline management, MLflow for tracking/deployment, and Streamlit for user interaction. Data strategies and model abstractions allow for easy extension and experimentation.