start:
	docker-compose up --build -d
test:
	docker-compose exec web python manage.py test invoices
