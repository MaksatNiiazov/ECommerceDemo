### **English**

# Django E-Commerce Platform

This is a robust e-commerce platform built with Django and Django REST Framework. The project includes a fully functional API and a responsive web interface, making it an excellent tool for real-time demonstrations. Leveraging cutting-edge technologies such as Elasticsearch for full-text search, Redis for caching, and Celery for asynchronous task processing, it is a perfect showcase for backend expertise and scalable architecture design.

---

### **Features**

#### **1. User Authentication**
- Supports both API-based authentication using JWT tokens and web forms for a seamless user experience.
- Includes features for user registration, login, password reset, and profile management.

#### **2. Product Catalog**
- Comprehensive product catalog with hierarchical categories.
- Implements full-text search powered by Elasticsearch for fast and accurate results.
- Includes filtering (by category, price, availability) and sorting options (e.g., price, popularity).

#### **3. Shopping Cart**
- Real-time cart management:
  - Add, update, or remove items.
  - Automatic recalculation of total price.
- Persistent cart data for authenticated users.

#### **4. Order Management**
- End-to-end order lifecycle management:
  - Place orders from the shopping cart.
  - Integration with payment gateways (Stripe or PayPal).
  - Order history and tracking for users.
  - Admin capabilities for managing order statuses (e.g., "Pending", "Shipped", "Delivered").

#### **5. Reviews and Ratings**
- Users can leave reviews and rate products.
- Average ratings are displayed on product pages.

#### **6. Query Caching**
- Redis is utilized for caching frequently accessed queries, improving application performance and reducing database load.

#### **7. Asynchronous Task Processing**
- Celery handles background tasks such as:
  - Sending email notifications (e.g., order confirmation, password reset).
  - Cleaning up old data (e.g., abandoned carts).

---

### **Technologies Used**

#### **Backend**
- **Framework**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Search Engine**: Elasticsearch
- **Caching**: Redis
- **Task Queue**: Celery with Redis as the message broker

#### **Frontend**
- **Templates**: Django Templates
- **CSS Frameworks**: Bootstrap and TailwindCSS for styling and responsive design

#### **Deployment**
- **Containerization**: Docker, Docker Compose
- **Web Server**: Nginx with Gunicorn for production

---

### **How to Run Locally**

#### **Prerequisites**
- Python 3.9+
- PostgreSQL
- Redis
- Elasticsearch
- Docker (optional)

#### **Steps**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file and add the following:
   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/db_name
   REDIS_URL=redis://localhost:6379
   ELASTICSEARCH_URL=http://localhost:9200
   ```

5. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Start Redis and Elasticsearch**:
   Ensure Redis and Elasticsearch services are running locally.

8. **Run Celery Worker**:
   ```bash
   celery -A your_project_name worker --loglevel=info
   ```

---

### **Deployment**

#### **Using Docker**
1. Build and start containers:
   ```bash
   docker-compose up --build
   ```

2. Access the app at `http://localhost`.

---

### **Русский**

# Платформа интернет-магазина на Django

Эта масштабируемая платформа интернет-магазина разработана на основе Django и Django REST Framework. Проект включает полноценное API и адаптивный веб-интерфейс, идеально подходящий для демонстрации функциональности. Используются современные технологии, такие как Elasticsearch для поиска, Redis для кеширования и Celery для обработки задач в фоновом режиме.

---

### **Функционал**

#### **1. Аутентификация пользователей**
- Поддержка аутентификации через API с использованием JWT токенов и через веб-формы.
- Возможности: регистрация, вход, восстановление пароля, управление профилем.

#### **2. Каталог товаров**
- Иерархический каталог с категориями.
- Полнотекстовый поиск через Elasticsearch.
- Фильтры (по цене, наличию, категории) и сортировка (по цене, популярности).

#### **3. Корзина**
- Управление корзиной в реальном времени:
  - Добавление, обновление, удаление товаров.
  - Автоматический подсчет итоговой суммы.
- Сохранение данных корзины для авторизованных пользователей.

#### **4. Управление заказами**
- Полный цикл управления заказами:
  - Оформление заказа из корзины.
  - Интеграция с платежными системами (Stripe/PayPal).
  - История заказов для пользователей.
  - Возможность администратора управлять статусами заказов.

#### **5. Отзывы и оценки**
- Оставление отзывов и оценок.
- Отображение среднего рейтинга на странице товара.

#### **6. Кеширование запросов**
- Используется Redis для кеширования популярных запросов, что повышает производительность и снижает нагрузку на базу данных.

#### **7. Асинхронные задачи**
- Фоновые задачи через Celery:
  - Отправка уведомлений (e.g., подтверждение заказа).
  - Удаление старых данных (e.g., брошенные корзины).

---

### **Технологии**
- **Бэкенд**: Django, DRF
- **База данных**: PostgreSQL
- **Поиск**: Elasticsearch
- **Кеширование**: Redis
- **Очередь задач**: Celery
- **Фронтенд**: Django Templates, Bootstrap, TailwindCSS
- **Деплой**: Docker, Gunicorn, Nginx

---

