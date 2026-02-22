# Production Deployment Checklist for TechDealsHub

## Pre-Deployment ✓

### Code & Database
- [ ] All code committed to git
- [ ] No debug print statements
- [ ] No hardcoded secrets
- [ ] All migrations created and tested locally
- [ ] Database backups configured

### Environment Configuration
- [ ] Generate secure SECRET_KEY
  ```bash
  python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
  ```
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Setup database credentials
- [ ] Configure email backend
- [ ] Setup media storage (S3 optional)

### Security
- [ ] X-Frame-Options header configured
- [ ] CSRF protection enabled
- [ ] XSS protection enabled
- [ ] HTTPS certificate obtained
- [ ] Security headers configured
- [ ] CORS properly configured

### Performance
- [ ] Static files configuration verified
- [ ] Database optimized (indexes, queries)
- [ ] Caching configured
- [ ] Compression enabled
- [ ] CDN configured (optional)

## Deployment Steps

### 1. Server Setup
```bash
# SSH into server
ssh ubuntu@your_server_ip

# Update system
sudo apt update
sudo apt upgrade -y

# Install dependencies
sudo apt install -y python3.10 python3-pip python3-venv \
    postgresql postgresql-contrib nginx supervisor git
```

### 2. Application Setup
```bash
# Create app directory
sudo mkdir -p /var/www/techdealshub
sudo chown -R $USER:$USER /var/www/techdealshub

# Clone repository
cd /var/www/techdealshub
git clone <your-repo> .

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn psycopg2-binary
```

### 3. Database Setup
```bash
# Connect to PostgreSQL
sudo -u postgres psql

# Run setup commands
CREATE DATABASE techdealshub;
CREATE USER techdealshub_user WITH PASSWORD 'your_secure_password';
ALTER ROLE techdealshub_user SET client_encoding TO 'utf8';
ALTER ROLE techdealshub_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE techdealshub_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE techdealshub TO techdealshub_user;
\q
```

### 4. Environment Configuration
```bash
cd /var/www/techdealshub
cp .env.example .env
nano .env  # Edit with production values
```

### 5. Django Setup
```bash
source venv/bin/activate

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Verify settings
python verify_settings.py
```

### 6. Gunicorn Configuration
```bash
# Create config file
nano gunicorn_config.py
```

### 7. Supervisor Setup
```bash
# Copy supervisor config
sudo cp supervisor.conf /etc/supervisor/conf.d/techdealshub.conf

# Create log directory
sudo mkdir -p /var/log/techdealshub
sudo chown www-data:www-data /var/log/techdealshub

# Start supervisor
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start techdealshub
sudo supervisorctl status
```

### 8. Nginx Setup
```bash
# Copy nginx config
sudo cp nginx.conf /etc/nginx/sites-available/techdealshub

# Enable site
sudo ln -s /etc/nginx/sites-available/techdealshub \
    /etc/nginx/sites-enabled/

# Test config
sudo nginx -t

# Restart nginx
sudo systemctl restart nginx
```

### 9. SSL Certificate
```bash
# Install Certbot
sudo apt install -y certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d techdealshub.example.com \
    -d www.techdealshub.example.com

# Auto-renewal
sudo systemctl enable certbot.timer
```

### 10. Firewall Configuration
```bash
# Enable firewall
sudo ufw enable

# Allow SSH, HTTP, HTTPS
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Status
sudo ufw status
```

## Post-Deployment ✓

### Verification
- [ ] Website accessible via HTTPS
- [ ] Admin panel working
- [ ] Static files loading
- [ ] Media files uploading
- [ ] Database queries fast
- [ ] Error pages displaying correctly
- [ ] Affiliate redirects working
- [ ] Email sending working

### Monitoring
- [ ] Setup error tracking (Sentry)
- [ ] Configure monitoring (New Relic)
- [ ] Setup log aggregation
- [ ] Configure automated backups
- [ ] Setup uptime monitoring
- [ ] Alert configuration

### Cleanup
- [ ] Remove DEBUG mode
- [ ] Delete test data
- [ ] Review security headers
- [ ] Verify SECRET_KEY rotation
- [ ] Check database size
- [ ] Review error logs

### Performance Tuning
- [ ] Monitor response times
- [ ] Check database performance
- [ ] Optimize slow queries
- [ ] Configure caching headers
- [ ] Test load capacity
- [ ] Setup auto-scaling (if needed)

## Maintenance Schedule

### Daily
- [ ] Monitor error logs
- [ ] Check disk space
- [ ] Monitor uptime

### Weekly
- [ ] Database backup
- [ ] Security updates
- [ ] Performance review

### Monthly
- [ ] Full backup
- [ ] Security audit
- [ ] Capacity planning
- [ ] Update dependencies

### Quarterly
- [ ] SSL certificate renewal (auto)
- [ ] Performance optimization
- [ ] Security patches

## Rollback Procedure

If deployment fails:

```bash
# Stop application
sudo supervisorctl stop techdealshub

# Revert code
cd /var/www/techdealshub
git checkout <previous-commit>

# Revert database (if needed)
# Restore from backup

# Restart
sudo supervisorctl start techdealshub
```

## Emergency Contacts & Access

- [ ] Admin SSH access: _______
- [ ] Database password: _______
- [ ] SSL certificate: _______
- [ ] GitHub access: _______
- [ ] Domain registrar: _______

## Documentation Links

- Django: https://docs.djangoproject.com/en/stable/
- Gunicorn: https://gunicorn.org/
- Nginx: https://nginx.org/
- PostgreSQL: https://www.postgresql.org/
- Supervisor: http://supervisord.org/

---

**Deployment Date**: ___________
**Deployed by**: ___________
**Notes**: ___________
