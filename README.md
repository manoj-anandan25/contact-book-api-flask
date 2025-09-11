Contact Book API – Flask + SQLAlchemy

A simple RESTful API to manage contact details — built with **Flask** and **SQLAlchemy**.
This project allows you to **store, retrieve, update, and delete contact information** in a database, accessible through easy-to-use HTTP endpoints.

---

##  Features

* **Create** new contact entries
* **Read** all contacts or a specific contact by ID or name
* **Update** contact information (full or partial updates)
* **Delete** contacts from the database
* SQLite database integration for persistent storage

---

##  Tech Stack

* **Backend:** Flask (Python)
* **Database:** SQLite (via SQLAlchemy ORM)
* **API Testing:** Postman / cURL

---

## Installation

1. **Clone this repository:**

```bash
git clone https://github.com/your-username/contact-book-api-flask.git
cd contact-book-api-flask
```

2. **Create and activate a virtual environment:**

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install flask flask_sqlalchemy
```

4. **Initialize the database:**

```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

5. **Run the API server:**

```bash
flask run
```

The API will start at: **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 📡 API Endpoints

| Method | Endpoint           | Description                |
| ------ | ------------------ | -------------------------- |
| GET    | `/contacts`        | Get all contacts           |
| GET    | `/contacts/<id>`   | Get a contact by ID        |
| GET    | `/contacts/<name>` | Get a contact by name      |
| POST   | `/contacts`        | Create a new contact       |
| PUT    | `/contacts/<id>`   | Fully update a contact     |
| PATCH  | `/contacts/<id>`   | Partially update a contact |
| DELETE | `/contacts/<id>`   | Delete a contact           |

---

# Example API Usage (Python SDK style)

```python
import requests

BASE_URL = "http://127.0.0.1:5000"

# Create a new contact
new_contact = {
    "name": "John Doe",
    "phone": 9876543210,
    "email": "john@example.com",
    "address": "123 Main Street"
}
response = requests.post(f"{BASE_URL}/contacts", json=new_contact)
print(response.json())

# Get all contacts
response = requests.get(f"{BASE_URL}/contacts")
print(response.json())

# Get a contact by ID
contact_id = 1
response = requests.get(f"{BASE_URL}/contacts/{contact_id}")
print(response.json())

# Update a contact (full update)
updated_contact = {
    "name": "John Updated",
    "phone": 111222333,
    "email": "johnupdated@example.com",
    "address": "456 New Street"
}
response = requests.put(f"{BASE_URL}/contacts/{contact_id}", json=updated_contact)
print(response.json())

# Partially update a contact
partial_update = {"phone": 999888777}
response = requests.patch(f"{BASE_URL}/contacts/{contact_id}", json=partial_update)
print(response.json())

# Delete a contact
response = requests.delete(f"{BASE_URL}/contacts/{contact_id}")
print(response.json())
```

---

For Non-Technical Users

Think of this **Contact Book API** like a **digital notebook** for storing names, phone numbers, emails, and addresses.
Instead of flipping through pages, you **ask the server** (via API requests) to:

* Add a new contact
* Look up an existing contact
* Update contact details
* Remove a contact you no longer need

If you don’t write code, you can still use tools like **Postman** to interact with the API by simply clicking and sending requests.

---

 Testing with Postman

1. Open Postman
2. Set the request URL to `http://127.0.0.1:5000/contacts`
3. Choose the HTTP method (GET, POST, PUT, PATCH, DELETE)
4. For POST/PUT/PATCH, go to **Body → raw → JSON** and enter your data:

```json
{
  "name": "Jane Doe",
  "phone": 1234567890,
  "email": "jane@example.com",
  "address": "456 Another Street"
}
```

5. Send the request and see the response instantly.


**Postman collection file **
Contact Book API so any developer (or even non-technical user) can test it instantly without having to set up everything from scratch.

---

##  contact-book-api-flask.postman\_collection.json**

```json
{
  "info": {
    "name": "Contact Book API - Flask",
    "_postman_id": "12345678-abcd-efgh-ijkl-1234567890ab",
    "description": "Postman collection for testing the Contact Book API built with Flask + SQLAlchemy",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Get All Contacts",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "http://127.0.0.1:5000/contacts",
          "protocol": "http",
          "host": ["127.0.0.1"],
          "port": "5000",
          "path": ["contacts"]
        }
      }
    },
    {
      "name": "Get Contact by ID",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "http://127.0.0.1:5000/contacts/1",
          "protocol": "http",
          "host": ["127.0.0.1"],
          "port": "5000",
          "path": ["contacts", "1"]
        }
      }
    },
    {
      "name": "Get Contact by Name",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "http://127.0.0.1:5000/contacts/John",
          "protocol": "http",
          "host": ["127.0.0.1"],
          "port": "5000",
          "path": ["contacts", "John"]
        }
      }
    },
    {
      "name": "Add New Contact",
      "request": {
        "method": "POST",
        "header": [
          { "key": "Content-Type", "value": "application/json" }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"name\": \"John Doe\",\n  \"phone\": 9876543210,\n  \"email\": \"john@example.com\",\n  \"address\": \"123 Main Street\"\n}"
        },
        "url": {
          "raw": "http://127.0.0.1:5000/contacts",
          "protocol": "http",
          "host": ["127.0.0.1"],
          "port": "5000",
          "path": ["contacts"]
        }
      }
    },
    {
      "name": "Update Contact (PUT)",
      "request": {
        "method": "PUT",
        "header": [
          { "key": "Content-Type", "value": "application/json" }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"name\": \"John Updated\",\n  \"phone\": 111222333,\n  \"email\": \"johnupdated@example.com\",\n  \"address\": \"456 New Street\"\n}"
        },
        "url": {
          "raw": "http://127.0.0.1:5000/contacts/1",
          "protocol": "http",
          "host": ["127.0.0.1"],
          "port": "5000",
          "path": ["contacts", "1"]
        }
      }
    },
    {
      "name": "Partial Update Contact (PATCH)",
      "request": {
        "method": "PATCH",
        "header": [
          { "key": "Content-Type", "value": "application/json" }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"phone\": 999888777\n}"
        },
        "url": {
          "raw": "http://127.0.0.1:5000/contacts/1",
          "protocol": "http",
          "host": ["127.0.0.1"],
          "port": "5000",
          "path": ["contacts", "1"]
        }
      }
    },
    {
      "name": "Delete Contact",
      "request": {
        "method": "DELETE",
        "header": [],
        "url": {
          "raw": "http://127.0.0.1:5000/contacts/1",
          "protocol": "http",
          "host": ["127.0.0.1"],
          "port": "5000",
          "path": ["contacts", "1"]
        }
      }
    }
  ]
}
```

---

##  How to Use This Postman Collection**

1. Save the JSON above as:

   ```
   contact-book-api-flask.postman_collection.json
   ```
2. Open **Postman**.
3. Go to **File → Import → Upload Files**.
4. Select the saved JSON file.
5. You’ll now see all your API calls ready to test.
6. Make sure your Flask app is running:

   ```bash
   flask run
   ```
7. Hit **Send** in Postman for any request.

---


