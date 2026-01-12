🚀 ***SaveSnap CLI***

SaveSnap CLI is a Python-based command-line snapshot and version management tool that allows users to track project changes locally and store commit metadata securely in Firebase Cloud Firestore.
It also provides an Educational Mode for learning basic version control concepts.


**✨ Features**

📁 Local project snapshot management

☁️ Real-time cloud commit storage using Firebase Firestore

🧠 Educational Mode for beginners

🕒 Commit history logging

🔄 Checkout and undo-checkout support


**🛠️ Tech Stack**

Python 3

Firebase Admin SDK

Firebase Cloud Firestore

Git & GitHub

VS Code


**📂 Project Structure**

SAVESNAP/

│

├── savesnap.py

├── firestoretest.py

├── firestore_bulk_commits.py

├── test.txt

├── test1.txt

├── .gitignore

└── README.md



**⚙️ Installation**

git clone https://github.com/Rin871-tech/SAVESNAP.git

cd SAVESNAP

pip install firebase-admin


**🔐 Firebase Setup**

Create a Firebase project

Enable Cloud Firestore

Generate a Service Account Key

Place it in the project folder as:

firebase_key.json


**▶️ Usage**

*-Initialize Repository*

  python savesnap.py init

*-Create a Commit*

  python savesnap.py commit "Added test file"

*-View Commit History*

  python savesnap.py log

*-Checkout a Commit*

  python savesnap.py checkout <commit_id>

*-Undo Checkout*

  python savesnap.py undo-checkout

*-Educational Mode*

  python savesnap.py edu



**☁️ Firebase Firestore Integration**

Each commit is saved as a document inside the savesnap_commits collection, storing:

Commit ID

Commit message

Modified files

Timestamp

✔ Confirms real cloud-based data storasge
