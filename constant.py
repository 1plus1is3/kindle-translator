from dotenv import dotenv_values

config = dotenv_values("local.env")
OUTPUT_IMG_FOLDER = config.get("OUTPUT_IMG_FOLDER")
OUTPUT_TXT_FOLDER = config.get("OUTPUT_TXT_FOLDER")
TESSERACT_PATH = config.get("TESSERACT_PATH")
FONT_PATH = config.get("FONT_PATH")
DEEPL_API_KEY = config.get("DEEPL_API_KEY")
