# 🛠️ Data Science Environment Setup Guide

Follow these steps to set up your development environment.

---

## **1. Setup Environment**

### 🌀 Step 1: Clone the Repository
Start by cloning the project repository to your local machine:
```bash
git clone https://github.com/Mannerow/ds-env-setup.git
cd ds-env-setup
```

### 💻 Step 2: Create a Virtual Environment

Create a virtual environment using Python 3.12:

```bash
py -3.12 -m venv venv
```

### 🔑 Step 3: Activate the Virtual Environment

```bash
source venv/Scripts/activate
```

You’ll know the environment is active when your terminal prompt changes to something like:

```bash
(venv) user@machine ~/project
```

### 📦 Step 4: Upgrade pip

Upgrade pip to ensure you have the latest version:

python -m pip install --upgrade pip

### 🛠️ Step 5: Install Dependencies

Install all project dependencies listed in requirements.txt:

```bash
python -m pip install -r requirements.txt
```

2. Install PostgreSQL and PostGIS

### 🐘 Step 1: Install PostgreSQL

1. Download PostgreSQL from the official website: [PostgreSQL Downloads](https://www.postgresql.org/download/). 
2. Follow the installation instructions for your operating system:
    * During installation, ensure that you also install the **Stack Builder** tool.

### 🌍 Step 2: Enable PostGIS

1. Open the PostgreSQL client (pgAdmin).
2. Connect to your database and enable PostGIS:

```sql
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
```

3. Verify postgis version:

```sql
SELECT postgis_full_version();
```