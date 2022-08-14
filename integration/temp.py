from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATE_DIR = "/home/lava/Рабочий стол/Work/integration/integration/templates" 
print(TEMPLATE_DIR)
#print(os.path.abspath(__file__) )