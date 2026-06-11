from locust import HttpUser, task, between


class ShopUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://www.demoblaze.com"

    @task(3)
    def open_home(self):
        self.client.get("/")

    @task(2)
    def open_cart(self):
        self.client.get("/cart.html")

    @task(1)
    def open_contact(self):
        self.client.get("/contact.html")