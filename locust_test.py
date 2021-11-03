from locust import HttpUser, task

class LocustUser(HttpUser):
  @task
  def ok(self):
    self.client.get("/")

  @task
  def not_found(self):
    self.client.get("/fail")
