# DJANGO MOVIE API BACKEND

### PROJECT STRUCTURE
```
MOVIE_BACKEND/
└───api/ 
│    │───migragtions/
│    │   __init__.py
│    │   admin.py
│    │   apps.py
│    │   models.py
│    │   test.py
│    │   urls.py
│    │   views.py
└───config/
│      │   __init__.py
│      │   asgi.py
│      │   settings.py
│      │   urls.py
│      │   wsgi.py
└───core/
│     │───crawl/
│     │     │   __init__.py
│     │     │   CGV_crawl.py
│     │     │   LOTTE_crawl.py
│     │     │   make_cgv_theater_list.py
│     │     │   MEGA_crawl.py
│     │───theater/
│     │      │───data/
│     │      │     │     json data in here 
│     │      │   __init__.py
│     │      │   lottecinema.py
│     │      │   cgv.py
│     │   __init__.py
│     │   boxoffice.py
│     │   location.py
└───templates/
│   .gitignore
│   db.sqlite3
│   manage.py
│   README.md
│   requirements.txt
│   run_mac.sh
│   run_window.sh
│   secrets.json 
```

