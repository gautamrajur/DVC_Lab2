# Data & Model Versioning with DVC

Version control for datasets and ML models using DVC with Google Cloud Storage.

##My Contribution: 
Added a new train.py and versioned a model.pkl and stored it in the gs (gs://data-versioning-dvc)

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install "dvc[gs]" pandas scikit-learn

git init
dvc init
dvc remote add -d myremote gs://<your-gcs-bucket>
dvc remote modify myremote credentialpath ./<service-account-key>.json
```

## Data Versioning

```bash
dvc add data/CC_GENERAL.csv
git add data/CC_GENERAL.csv.dvc data/.gitignore
git commit -m "Track dataset"
dvc push
```

## Model Versioning via Pipeline

`dvc.yaml` defines a pipeline (preprocess → train → save metrics). Run with:

```bash
dvc repro
git add dvc.yaml dvc.lock metrics.json train.py
git commit -m "Pipeline run"
dvc push
```

Model outputs under `outs` in `dvc.yaml` are automatically tracked — no `dvc add` needed.

## Reverting to a Previous Version

```bash
git checkout <commit-hash>
dvc checkout
# Return to latest:
git checkout main && dvc checkout
```

## Useful Commands

| Command | Description |
|---|---|
| `dvc repro` | Run pipeline, rerun changed stages |
| `dvc push` / `dvc pull` | Sync files with GCS |
| `dvc metrics show` | View model metrics |
| `dvc metrics diff` | Compare metrics across versions |
| `dvc status` | Check if files are in sync |