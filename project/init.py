docker-compose build
docker-compose up
docker ps
docker exec 596 python3 manage.py makemigrations shop
docker exec 596 python3 manage.py migrate

docker exec 596 python3 seed_fs.py

curl "http://localhost:8000/shop/api/products?page_no=1&page_size=10"
curl "http://localhost:8000/shop/api/orders?page_no=1&page_size=10"
curl "http://localhost:8000/shop/api/related_products?id=3"
