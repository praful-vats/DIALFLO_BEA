from celery import Celery
import os

celery_app = Celery(
    "tasks",
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_RESULT_BACKEND"),
)

@celery_app.task(bind=True, max_retries=3)
def process_new_order(self, order_data):
    try:
        return {"status": "order_processed", "customer_id": order_data["customer_id"]}
    except Exception as e:
        self.retry(exc=e, countdown=5)  # Retry logic with exponential backoff
