
---
# Pollution

## 1. Danh sách lệnh thường dùng:

- Start container: ```docker compose up -d```
- Stop container: ```docker compose down```
- Vào bên trong container để thực hiện lệnh: ```docker exec -it pollution-web-1 sh```
  - <span style="color: yellow">\### Các lệnh sau được thực hiện trong container sau khi chạy lệnh trên ###</span>
  - <span style="color: yellow">Lưu ý: Có thể sử dụng ```django-admin``` hoặc ```python manage.py``` và ```python manage.py``` phải được chạy ở thư mục app.</span>
  - Tạo Migrate: ```python manage.py makemigrations [app_label [app_label ...]]```
    - ```app_label``` là tên app tương ứng muốn tạo migrate(nên dùng).
    - Nếu không để thì mặc định sẽ tạo migrate cho tất cả các app.
  - Xem lệnh sql của migrate: ```python manage.py sqlmigrate migrate_name migrate_number```
  - Chạy Migrate: ```python manage.py migrate```
  - Tạo superuser: ```python manage.py createsuperuser```
    - Sau khi chạy lệnh thì sẽ nhập username, email, password theo hướng dẫn.
  - Tạo app: ```python manage.py startapp app_name```

## 2. Workflow
1. Copy `.env.example` to `.env`
1. Run: ```docker compose up -d```
1. Open new terminal then run: ```docker exec -it pollution-web-1 sh```
    - Create supperuser: ```python manage.py createsuperuser```
    - Migrate database: ```python manage.py migrate```
1. Code function ...
1. Run git command
    - Commit code
    - Pull develop
    - Fix conflict(optional)
    - Push
    - Create merge request
    - Check merge request and update code(optional)
1. Repeat from step 3 if you still working on this project
1. Run: ```docker compose down``` to stop container then go home :\)

## 3. Project structure
<!-- ─ ├ │ └ -->
```
.
├── .git
├── app
│   ├── backend
│   │   ├── static/
│   │   ├── templates/
│   │   ├── settings.py
│   │   └── urls.py
│   ├── app_1
│   ├── app_2
│   ├── app_3
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── managers.py
│   │   ├── schema.py
│   │   ├── serializers.py
│   │   └── views.py
│   ├── Dockerfile
│   ├── entrypoint.sh
│   ├── manage.py
│   ├── requirements.txt
│   └── [new_folder]
├── .env
├── .gitignore
├── compose.yaml
└── README.md
```

## 4. Database structure

## 5. Code rules

---