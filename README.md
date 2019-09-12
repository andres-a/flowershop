# flowershop
Evaluation test

Few Django/PostgreSQL API-s in Docker containers for testing.
PostgreSQL database is served on localhost:5432

To use, download files.
In flowershop directory:
  # Compose containerized services 
  docker-compose up
  # Open new terminal window
  # Look up flowershop_web conatiner name (eg. flowershop_web_1) 
  docker ps
  # Initialize datamodel
  docker exec flowershop_web_1 python3 manage.py makemigrations shop
  # Deploy datamodel
  docker exec flowershop_web_1 python3 manage.py migrate
  # Seed mock data
  docker exec flowershop_web_1 python3 seed_fs.py
  # Test GET request for products
  curl "http://localhost:8000/shop/api/products?page_no=1&page_size=10"
  # Test GET request for orders
  curl "http://localhost:8000/shop/api/orders?page_no=1&page_size=10"
  # Test GET request for related products sales
  curl "http://localhost:8000/shop/api/related_products?id=3"
  
