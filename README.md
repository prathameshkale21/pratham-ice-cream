<<<<<<< HEAD
# 🍦 Pratham Ice Cream — Django E-Commerce Website

A full-stack e-commerce web application for an ice cream brand, built with
Django. Customers can browse products, save favourites to a wishlist, add
items to a cart, check out, and view their order history. Deployable to
Render out of the box.

---

## ✨ Features

- **Product catalog** — categories, featured products, product detail
  pages, search, and sorting (price / name / latest)
- **Accounts** — register, login, logout (Django's built-in auth)
- **Cart** — add / increase / decrease / remove items, live totals
- **Wishlist** — save favourite products with a heart icon, view/remove
  them from a dedicated page
- **Orders** — checkout creates a real order record; customers can view
  their full order history
- **Reviews** — product review app
- **Toast notifications** — all success/error/info messages appear as
  auto-dismissing toast popups
- **Responsive UI** — Bootstrap 5 + custom CSS, consistent product-card
  design across the homepage and product listing page
- **Admin panel** — manage products, categories, carousel banners,
  orders, and wishlists via Django admin

---

## 🛠️ Tech Stack

- **Backend:** Django 6.0 (Python 3.12+)
- **Database:** SQLite locally, PostgreSQL in production
- **Static/Media:** WhiteNoise (static files), local filesystem (media)
- **Frontend:** Bootstrap 5, Bootstrap Icons, vanilla JS
- **Deployment:** Render (see `render.yaml` / `build.sh`)

---

## 📁 Project Structure

```
Prathamesh/          Project settings, root urls, wsgi/asgi
home/                Homepage, carousel, category & product models, about, privacy policy
products/            Product listing, detail, search & sort
accounts/            Register, login, logout
cart/                Cart & cart item logic
wishlist/            Wishlist model, add/remove, wishlist page
orders/              Order & OrderItem models, checkout, order history
reviews/              Product review app
templates/           All HTML templates (base, components, per-app pages)
static/              CSS, JS, images
media/               User-uploaded product images
build.sh             Render build script (install, collectstatic, migrate)
render.yaml          Render blueprint (web service + Postgres, one-click deploy)
requirements.txt     Python dependencies
```

---

## 🚀 Getting Started Locally

```bash
# 1. Clone the repo
git clone https://github.com/prathameshkale21/pratham-ice-cream.git
cd pratham-ice-cream

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create an admin user
python manage.py createsuperuser

# 6. Run the dev server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the storefront and
`http://127.0.0.1:8000/admin/` for the admin panel.

---

## 🌐 Deployment (Render)

This project is pre-configured for Render:

1. Push this repo to GitHub.
2. On [render.com](https://render.com): **New → Blueprint**, connect the
   repo. Render reads `render.yaml` and provisions a free web service +
   free Postgres database automatically.
3. Once deployed, open the web service's **Shell** and run:
   ```bash
   python manage.py createsuperuser
   ```

**Known free-tier limitations:**
- Uploaded product images don't persist across redeploys (ephemeral
  filesystem) — a future improvement would move media storage to
  Cloudinary or S3.
- The free web service spins down after ~15 minutes of inactivity, so
  the first request afterward takes 30–60 seconds to wake up.

---

## 📌 Roadmap / Ideas for Next Steps

- [ ] Persistent media storage (Cloudinary/S3)
- [ ] Payment gateway integration
- [ ] User profile / address book page
- [ ] Product ratings tied to actual review data (currently static stars)
- [ ] Email notifications on order placement

---

## 📄 License

This project is for personal/portfolio use.
=======

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

>>>>>>> ba7544ff156710e4dc07cadae0dbf170b1a65847
