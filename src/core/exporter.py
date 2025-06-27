# exporter.py
import csv
import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def export_to_csv(cursor, results, filename=None):
    # Create results directory if it doesn't exist
    os.makedirs("../results", exist_ok=True)

    # Generate a timestamped filename if not provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"results/output_{timestamp}.csv"

    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([col[0] for col in cursor.description])
            writer.writerows(results)

        logger.info(f"Data successfully exported to '{filename}'")

    except Exception as e:
        logger.error(f"Failed to export data to CSV: {e}")
