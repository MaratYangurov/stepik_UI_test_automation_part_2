import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')
APPLE_DEVICES_URL='/index.php?route=product/manufacturer/info&manufacturer_id=8'