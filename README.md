# TechDealsHub - Production-Ready Django Affiliate Website

A complete, production-ready MVP affiliate website built with Django, PostgreSQL, and Tailwind CSS.

## Features

### Public Site
- **Homepage** with featured and top-rated products
- **Category Pages** with products organized by category
- **Product Detail Pages** with:
  - Product images and pricing
  - Ratings and reviews
  - Pros and cons lists
  - Affiliate redirect links
- **Blog System** with published articles and SEO optimization
- **Search Functionality** to find products
- **Responsive Design** using Tailwind CSS
- **404 & 500 Error Pages**

### Admin Dashboard
- Full CRUD operations for:
  - Products with image upload
  - Categories
  - Blog posts with featured images
  - Click tracking logs
- Slug auto-generation for products and posts
- Click count statistics per product
- Status management and filtering

### SEO & Performance
- Dynamic meta tags and descriptions
- OpenGraph tags for social media sharing
- JSON-LD structured data for products
- Sitemap.xml generation
- Robots.txt configuration
- Clean, semantic URL structure
- Pagination for better performance

### Security
- CSRF protection on all forms
- Secure affiliate redirects
- Environment-based configuration
- Production-ready settings
- SQL injection prevention through ORM

## Project Structure

```
techdealshub/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore file
├── init_dirs.py            # Initialize required directories
│
├── config/                   # Project configuration
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI application
│   └── asgi.py              # ASGI application
│
├── products/                 # Products app
│   ├── models.py            # Product, Category, Click models
│   ├── views.py             # Product views
│   ├── urls.py              # Product URLs
│   ├── admin.py             # Admin configuration
│   ├── apps.py
│   └── migrations/
│
├── blog/                     # Blog app
│   ├── models.py            # BlogPost model
│   ├── views.py             # Blog views
│   ├── urls.py              # Blog URLs
│   ├── admin.py             # Admin configuration
│   ├── apps.py
│   └── migrations/
│
├── core/                     # Core app
│   ├── models.py            # SiteConfig model
│   ├── views.py             # Core views
│   ├── urls.py              # Core URLs
│   ├── admin.py             # Admin configuration
│   ├── apps.py
│   ├── utilities.py         # Helper functions
│   ├── sitemaps.py          # Sitemap configuration
│   └── migrations/
│
├── templates/               # HTML templates
│   ├── base/
│   │   └── base.html       # Base template
│   ├── includes/
│   │   ├── navbar.html
│   │   ├── footer.html
│   │   └── product_card.html
│   ├── products/
│   │   ├── home.html
│   │   ├── category_list.html
│   │   ├── category_detail.html
│   │   ├── product_detail.html
│   │   └── search_results.html
│   ├── blog/
│   │   ├── blog_list.html
│   │   └── blog_detail.html
│   ├── core/
│   │   ├── about.html
│   │   ├── privacy.html
│   │   ├── terms.html
│   │   └── contact.html
│   ├── errors/
│   │   ├── 404.html
│   │   └── 500.html
│   └── robots.txt
│
├── static/                  # Static files (CSS, JS, images)
├── media/                   # User-uploaded media files
└── logs/                    # Application logs
```

## Database Models

### User
Django's built-in User model with authentication

### Category
- name (CharField)
- slug (SlugField)
- description (TextField)
- icon (CharField) - Font Awesome icon
- created_at
- updated_at

### Product
- name (CharField)
- slug (SlugField)
- description (TextField)
- price (DecimalField)
- original_price (DecimalField, optional)
- rating (DecimalField 0-5)
- image (ImageField)
- affiliate_url (URLField)
- pros (TextField)
- cons (TextField)
- category (ForeignKey)
- is_featured (BooleanField)
- click_count (PositiveIntegerField)
- views_count (PositiveIntegerField)
- created_at
- updated_at

### BlogPost
- title (CharField)
- slug (SlugField)
- content (TextField)
- featured_image (ImageField)
- excerpt (TextField, optional)
- meta_description (CharField)
- author (ForeignKey to User)
- is_published (BooleanField)
- views_count (PositiveIntegerField)
- created_at
- updated_at
- published_at (DateTimeField)

### Click
- product (ForeignKey)
- ip_address (GenericIPAddressField)
- user_agent (TextField)
- referrer (URLField)
- created_at

### SiteConfig
- site_name
- site_description
- logo, favicon, og_image (ImageFields)
- contact_email, phone, address
- Social media URLs
- Google Analytics ID
- Keywords

## Installation & Setup

### Prerequisites
- Python 3.8+
- PostgreSQL (or SQLite for development)
- pip or poetry
- Virtual environment

### Step 1: Clone or Download the Project

```bash
cd techdealshub
```

### Step 2: Create and Activate Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Copy `.env.example` to `.env` and update values:

```bash
cp .env.example .env
```

Edit `.env`:
```
DEBUG=True
SECRET_KEY=your-secret-key-change-this-in-production
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (PostgreSQL)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=techdealshub
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### Step 5: Create Database (PostgreSQL Setup)

**On Windows with PostgreSQL:**

```sql
-- Open PostgreSQL terminal
psql -U postgres

-- Create database
CREATE DATABASE techdealshub;

-- Create user
CREATE USER techdealshub_user WITH PASSWORD 'your_password';

-- Grant privileges
ALTER ROLE techdealshub_user SET client_encoding TO 'utf8';
ALTER ROLE techdealshub_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE techdealshub_user SET default_transaction_deferrable TO on;
ALTER ROLE techdealshub_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE techdealshub TO techdealshub_user;
```

### Step 6: Initialize Required Directories

```bash
python init_dirs.py
```

### Step 7: Run Migrations

```bash
python manage.py migrate
```

### Step 8: Create Superuser

```bash
python manage.py createsuperuser
```

### Step 9: Seed Initial Data (Optional)

```bash
python manage.py seed_data
```

This creates:
- Admin user (admin/admin123)
- Sample categories
- Sample products
- Sample blog posts

### Step 10: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Step 11: Run Development Server

```bash
python manage.py runserver
```

Access:
- **Website:** http://localhost:8000
- **Admin:** http://localhost:8000/admin

## API Endpoints

### Public URLs
- `/` - Homepage
- `/categories/` - List all categories
- `/category/<slug>/` - Category detail with products
- `/product/<slug>/` - Product detail page
- `/search/?q=<query>` - Search products
- `/go/<product_id>/` - Affiliate redirect (tracks click)
- `/blog/` - Blog list
- `/blog/<slug>/` - Blog post detail
- `/about/` - About page
- `/privacy/` - Privacy policy
- `/terms/` - Terms and conditions
- `/contact/` - Contact page
- `/admin/` - Database admin panel

### SEO URLs
- `/sitemap.xml` - Sitemap for search engines
- `/robots.txt` - Robots.txt for crawlers

## Production Deployment

### Option 1: VPS Deployment (DigitalOcean, Linode, AWS EC2)

#### 1. Server Setup
```bash
# SSH into your server
ssh root@your_server_ip

# Update system
apt update && apt upgrade -y

# Install dependencies
apt install -y python3.10 python3-pip python3-venv postgresql postgresql-contrib nginx supervisor git

# Create app directory
mkdir -p /var/www/techdealshub
cd /var/www/techdealshub

# Clone repository
git clone <your-repo> .
```

#### 2. Python Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn
```

#### 3. Database Setup
```sql
sudo -u postgres psql
CREATE DATABASE techdealshub;
CREATE USER techdealshub_user WITH PASSWORD 'secure_password';
ALTER ROLE techdealshub_user SET client_encoding TO 'utf8';
ALTER ROLE techdealshub_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE techdealshub_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE techdealshub TO techdealshub_user;
```

#### 4. Environment Setup
```bash
cp .env.example .env
# Edit .env with production values
nano .env
```

```
DEBUG=False
SECRET_KEY=<generate-a-secure-key>
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DB_ENGINE=django.db.backends.postgresql
DB_NAME=techdealshub
DB_USER=techdealshub_user
DB_PASSWORD=secure_password
DB_HOST=localhost
DB_PORT=5432
```

#### 5. Run Migrations
```bash
cd /var/www/techdealshub
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

#### 6. Gunicorn Configuration
Create `/var/www/techdealshub/gunicorn_config.py`:
```python
bind = '127.0.0.1:8000'
workers = 4
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2
max_requests = 1000
max_requests_jitter = 50
```

#### 7. Supervisor Configuration
Create `/etc/supervisor/conf.d/techdealshub.conf`:
```ini
[program:techdealshub]
command=/var/www/techdealshub/venv/bin/gunicorn -c /var/www/techdealshub/gunicorn_config.py config.wsgi:application
directory=/var/www/techdealshub
user=www-data
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/techdealshub/gunicorn.log
```

```bash
mkdir -p /var/log/techdealshub
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start techdealshub
```

#### 8. Nginx Configuration
Create `/etc/nginx/sites-available/techdealshub`:
```nginx
upstream techdealshub_app {
    server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    client_max_body_size 20M;

    location /static/ {
        alias /var/www/techdealshub/staticfiles/;
    }

    location /media/ {
        alias /var/www/techdealshub/media/;
    }

    location / {
        proxy_pass http://techdealshub_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/techdealshub /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### 9. SSL Certificate (Let's Encrypt)
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

### Option 2: Railway Deployment

1. **Create Railway Account** at https://railway.app

2. **Connect GitHub Repository**
   - Create GitHub repo and push code
   - Link to Railway

3. **Configure Environment**
   - Add all `.env` variables in Railway dashboard

4. **Create PostgreSQL Database**
   - Add PostgreSQL plugin in Railway

5. **Deploy**
   - Railway automatically detects Django project
   - Runs: `python manage.py migrate && gunicorn config.wsgi`

### Option 3: Heroku Deployment

#### 1. Create Procfile
```
web: gunicorn config.wsgi
release: python manage.py migrate
```

#### 2. Create runtime.txt
```
python-3.10.12
```

#### 3. Deploy
```bash
heroku login
heroku create techdealshub
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

## Performance Optimization

1. **Database Indexing** - Already configured on frequently queried fields
2. **Caching** - Configured with Django's default cache
3. **CDN** - Use WhiteNoise middleware for static files
4. **Image Optimization** - Compress product images before upload
5. **Database**: Use PostgreSQL for production
6. **Monitoring**: Add New Relic or Sentry for error tracking

## Customization

### Add New Product Category
1. Go to Admin → Categories
2. Click "Add Category"
3. Fill in name, description, and icon
4. Save

### Add New Product
1. Go to Admin → Products
2. Click "Add Product"
3. Fill in all details
4. Upload image
5. Set affiliate URL
6. Save

### Add Blog Post
1. Go to Admin → Blog Posts
2. Click "Add Blog Post"
3. Write content (supports HTML)
4. Upload featured image
5. Mark as published
6. Save

### Modify Styling
- Colors are defined in Tailwind CSS classes in templates
- Edit `ACCENT_COLOR` in templates or use Tailwind config
- Create `tailwind.config.js` for more control

## Troubleshooting

### Database Connection Error
- Check PostgreSQL is running: `sudo systemctl status postgresql`
- Verify credentials in `.env` file
- Check DB_HOST is correct

### Static Files Not Loading
```bash
python manage.py collectstatic --clear --noinput
```

### Import Errors
```bash
pip install --upgrade -r requirements.txt
```

### Migration Issues
```bash
python manage.py migrate --fake-initial
python manage.py migrate
```

## SEO Checklist

- [x] Meta descriptions on all pages
- [x] OpenGraph tags for social sharing
- [x] JSON-LD structured data for products
- [x] Sitemap.xml
- [x] Robots.txt
- [x] Clean URL structure
- [x] Mobile responsive (Tailwind CSS)
- [x] Fast loading times
- [x] Blog content for keywords
- [ ] Google Analytics integration
- [ ] Google Search Console verification
- [ ] Social media links in footer

## Security Checklist

- [x] CSRF tokens on forms
- [x] SQL injection prevention (Django ORM)
- [x] XSS protection
- [x] Environment variables for secrets
- [x] HTTPS support
- [x] Secure password hashing
- [ ] Rate limiting on affiliate redirects
- [ ] DDOS protection
- [ ] Regular security updates

## Future Enhancements

1. **User Accounts** - Allow users to save favorite products
2. **Email Newsletter** - Subscribe to new products
3. **Product Recommendations** - AI-based suggestions
4. **Advanced Filters** - Price range, rating filters
5. **User Reviews** - Product reviews from visitors
6. **Analytics Dashboard** - Sales and click metrics
7. **Amazon Affiliate** - Support for Amazon affiliate links
8. **Payment Integration** - For premium features
9. **Multi-language** - Support for multiple languages
10. **Admin Notifications** - New order/click alerts

## License

This project is provided as-is for educational and commercial use.

## Support

For issues or questions, please create an issue in the repository or contact the development team.

---

**TechDealsHub** - Build by full-stack Django developers for full-stack Django developers.
