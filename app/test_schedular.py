import asyncio
from app.scheduler import check_and_notify

# Test the notification function directly
print("Testing notification system...\n")
asyncio.run(check_and_notify())
print("\nTest complete!")