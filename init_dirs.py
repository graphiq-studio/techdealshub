import os
from pathlib import Path

# Create logs directory if it doesn't exist
logs_dir = Path(__file__).parent / "logs"
logs_dir.mkdir(exist_ok=True)

# Create media directory if it doesn't exist
media_dir = Path(__file__).parent / "media"
media_dir.mkdir(exist_ok=True)
