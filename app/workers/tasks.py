from celery import Celery
import os

# Initialize Celery app with broker and backend from environment variables
celery_app = Celery(
    "tasks",
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_RESULT_BACKEND"),
)

@celery_app.task(bind=True, max_retries=3)
def process_new_order(self, order_data):
    try:
        # Process the order and return the status with customer ID
        return {"status": "order_processed", "customer_id": order_data["customer_id"]}
    except Exception as e:
        # Retry the task in case of an exception, with exponential backoff
        self.retry(exc=e, countdown=5)
