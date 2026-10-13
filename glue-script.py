
import sys
from datetime import datetime, timezone

print("Question 3 Glue job started")
print("Processing a sample data record")

record = {
    "record_id": "Q3-001",
    "status": "PROCESSED",
    "processed_at": datetime.now(timezone.utc).isoformat()
}

print("Processed record:", record)
print("Question 3 Glue job completed successfully")
