# ds-env-setup

Follow these steps to set up your development environment.

---

## 🌀 Step 1: Clone the Repository
Start by cloning the project repository to your local machine:
```bash
git clone https://github.com/Mannerow/ds-env-setup.git
cd ds-env-setup
```

## 💻 Step 2: Create a Virtual Environment

Create a virtual environment using Python 3.12:

```bash
py -3.12 -m venv venv
```

## 🔑 Step 3: Activate the Virtual Environment

```bash
source venv/Scripts/activate
```

You’ll know the environment is active when your terminal prompt changes to something like:

```bash
(venv) user@machine ~/project
```

## 📦 Step 4: Upgrade pip

Upgrade pip to ensure you have the latest version:

python -m pip install --upgrade pip

## 🛠️ Step 5: Install Dependencies

Install all project dependencies listed in requirements.txt:

```bash
python -m pip install -r requirements.txt
```