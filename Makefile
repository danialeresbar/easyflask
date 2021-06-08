bash:
	docker exec -it easyflask bash

init_db:
	docker exec -it easyflask flask db init

generate_migration:
	docker exec -it easyflask flask db migrate

apply_migration:
	docker exec -it easyflask flask db upgrade
