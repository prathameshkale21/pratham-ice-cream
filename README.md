
# 🍦 Pratham Ice Cream – Django Web Application

A responsive *Ice Cream Shop web application* built using *Python Django and Bootstrap. The application allows users to log in, explore ice cream flavors, and submit suggestions through a contact form. The project demonstrates **user authentication, database integration, and dynamic web pages using Django templates*.

---

# 🚀 Features

* 🔐 *User Authentication* (Login / Logout)
* 🏠 *Protected Home Page* accessible only after login
* 🍨 *Ice Cream Flavor Showcase* with images, descriptions, and prices
* 📩 *Contact Form* to collect customer suggestions
* 💬 *Django Messages Framework* for success notifications
* 📱 *Responsive UI* using Bootstrap
* 🗄 *Database Storage* for contact form data

---

# 🛠 Technologies Used

* *Python*
* *Django*
* *HTML*
* *CSS*
* *Bootstrap*
* *SQLite*
* *Django Templates*

---

# 📂 Project Structure


Pratham-IceCream
│
├── manage.py
├── db.sqlite3
│
├── home
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates
│   ├── base.html
│   ├── index.html
│   ├── contact.html
│   └── login.html
│
└── static
    └── img


---

# ⚙️ Installation & Setup

### 1️⃣ Clone the repository

bash
git clone https://github.com/yourusername/pratham-icecream.git


### 2️⃣ Navigate to the project folder

bash
cd pratham-icecream


### 3️⃣ Install dependencies

bash
pip install django


### 4️⃣ Run migrations

bash
python manage.py migrate


### 5️⃣ Run the development server

bash
python manage.py runserver


### 6️⃣ Open in browser


http://127.0.0.1:8000

