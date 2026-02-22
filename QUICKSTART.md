# TechDealsHub - Quick Start Guide

## 5-Minute Setup

### Windows Setup

```bash
# 1. Open PowerShell and navigate to project
cd c:\Users\ampon\OneDrive\Desktop\personals\neww\techdealshub

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup environment
copy .env.example .env
# Edit .env if using database other than SQLite

# 5. Run migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Seed sample data (optional)
python manage.py seed_data

# 8. Start server
python manage.py runserver
```

Visit:
- Homepage: http://localhost:8000
- Admin: http://localhost:8000/admin

---

## Project Highlights

✅ **Complete MVP** - Fully functional affiliate website
✅ **Production-Ready** - Security, performance, scalability
✅ **SEO Optimized** - Sitemaps, meta tags, structured data
✅ **Responsive Design** - Tailwind CSS, mobile-first
✅ **Admin Dashboard** - Full CRUD with Django Admin
✅ **Click Tracking** - Track affiliate link clicks
✅ **Blog System** - Content management with publishing
✅ **Error Handling** - Custom 404 and 500 pages

---

## File Structure Overview

```
techdealshub/
├── manage.py                 # Main Django script
├── requirements.txt          # Python packages
├── .env.example             # Config template
├── README.md                # Full documentation
├── QUICKSTART.md            # This file
│
├── config/                   # Django project settings
├── products/                 # Products & categories app
├── blog/                    # Blog posts app
├── core/                    # Core utilities & config
├── templates/               # HTML templates
├── static/                  # CSS, JS, images
├── media/                   # Uploaded files
└── logs/                    # Application logs
```

---

## Key Features by Use Case

### For Store Owners
- Add/Edit/Delete products with images
- Manage categories
- Track affiliate click statistics
- Monitor product performance

### For Content Writers
- Create blog posts
- Upload featured images
- Publish/unpublish articles
- Track reader engagement

### For Visitors
- Browse products by category
- Search for items
- Read product reviews
- Click affiliate links
- Read helpful blog posts

---

## Admin Dashboard Quick Tips

1. **Add Product**
   - Go to Products → Add
   - Upload image (auto-resizes)
   - Set affiliate URL from AliExpress
   - Mark as featured (shows on homepage)

2. **Manage Categories**
   - Categories → Add
   - Choose Font Awesome icon
   - Products auto-organize

3. **Track Clicks**
   - Click log shows every affiliate redirect
   - Track by product or IP
   - Analyze user engagement

4. **Blog Posts**
   - Write HTML content
   - Upload featured image
   - Schedule publishing with date

---

## Custom Commands

```bash
# Seed database with sample data
python manage.py seed_data

# Run tests
python runtests.py

# Check for errors
python manage.py check

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Create superuser
python manage.py createsuperuser
```

---

## Environment Variables

Key settings in `.env`:

```
DEBUG=True                              # Set to False in production
SECRET_KEY=<your-secret-key>            # Generate secure key
ALLOWED_HOSTS=localhost,127.0.0.1       # Add production domain

DB_ENGINE=django.db.backends.sqlite3    # Or postgresql
DB_NAME=techdealshub
# ... database credentials ...

AFFILIATE_BASE_URL=https://...          # AliExpress affiliate tracker
```

---

## Affiliate Link Setup

1. Get AliExpress affiliate code
2. Format: `https://www.awin1.com/cclick.php?p=YOUR_CODE`
3. Add to product in admin
4. Clicks automatically tracked and redirected

---

## Common Issues & Fixes

**Port 8000 already in use**
```bash
python manage.py runserver 8001
```

**Database errors**
```bash
python manage.py migrate --fake-initial
python manage.py migrate
```

**Static files not showing**
```bash
python manage.py collectstatic --clear --noinput
```

---

## Next Steps for Production

1. ✅ Review `.env` settings
2. ✅ Change SECRET_KEY
3. ✅ Set DEBUG=False
4. ✅ Configure database (PostgreSQL)
5. ✅ Setup SSL certificate
6. ✅ Configure domain name
7. ✅ Setup email backend
8. ✅ Add Google Analytics
9. ✅ Deploy to server
10. ✅ Monitor with Sentry/NewRelic

---

## Useful Commands Reference

```bash
# Development
python manage.py runserver
python manage.py shell
python manage.py dbshell

# Database
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --fake

# Admin
python manage.py createsuperuser
python manage.py changepassword username

# Static/Media
python manage.py collectstatic --noinput

# Testing
python manage.py test

# Performance
python manage.py runserver --no-threading
```

---

## Architecture Overview

```
Browser Request
    ↓
Nginx/Gunicorn (Production)
    ↓
Django URL Router (config/urls.py)
    ↓
App Views (products/views.py, blog/views.py)
    ↓
Models (products/models.py) ↔ Database
    ↓
Templates (templates/)
    ↓
HTML Response + CSS/JS
    ↓
Browser
```

---

## Customization Tips

### Change Brand Colors
Edit `gradient-bg` class in templates (currently purple)

### Add New Model
1. Create in `app/models.py`
2. Register in `app/admin.py`
3. Run `python manage.py makemigrations`
4. Run `python manage.py migrate`

### Add New Page
1. Create view in `views.py`
2. Add URL in `urls.py`
3. Create template in `templates/`

---

## API Endpoints

| URL | Purpose |
|-----|---------|
| `/` | Homepage |
| `/product/<slug>/` | Product detail |
| `/category/<slug>/` | Category products |
| `/search/?q=<term>` | Search results |
| `/go/<id>/` | Affiliate redirect |
| `/blog/` | Blog list |
| `/blog/<slug>/` | Blog post |
| `/admin/` | Admin panel |
| `/sitemap.xml` | SEO sitemap |
| `/robots.txt` | Search engines |

---

## Performance Tips

1. Compress product images before upload
2. Use PostgreSQL for production
3. Enable caching for static assets
4. Use CDN for media files
5. Monitor database query performance

---

## Deployment Quick Links

- **VPS**: DigitalOcean, Linode, AWS EC2, Vultr
- **PaaS**: Railway, Heroku, PythonAnywhere
- **Serverless**: AWS Lambda, Google Cloud Run
- **See README.md** for detailed deployment guides

---

## Support & Resources

- Django Docs: https://docs.djangoproject.com
- Tailwind CSS: https://tailwindcss.com
- PostgreSQL: https://www.postgresql.org
- AliExpress Affiliate: https://awin.com

---

**Happy coding! 🚀**
