from curses.ascii import HT
from locust import HttpUser, task, between
from random import randint
import json

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    
    @task(2)
    def view_products(self):
        print('view products')
        collection_id = randint(2, 6)
        self.client.get(
        f'/shop/products/?colllection_id={collection_id}',
        name='/shop/products')

    @task(4)
    def view_product(self):
        print('view product details')
        product_id = randint(1, 1000)
        self.client.get(
            f'/shop/products/{product_id}/',
            name = '/shop/products/:id')
        
    @task(1)
    def add_to_cart(self):
        print('add to cart')
        product_id = randint(1, 10)
        self.client.post(
            f'/shop/cart/{self.cart_id}/items/',
            name='/shop/cart/items/',
            json={'product_id': product_id, 'quantity': 1}
        )

    def on_start(self):
        response = self.client.post('/shop/cart/')
        result = response.json()
        self.cart_id = result['id']