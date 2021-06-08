bash:
	docker exec -it easyflask bash

init_db:
	docker exec -it easyflask flask db init

generate_migrate:
	docker exec -it easyflask flask db migrate -m "Initial migration"

apply_migrate:
	docker exec -it easyflask flask db upgrade
