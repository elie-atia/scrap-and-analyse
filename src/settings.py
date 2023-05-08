from dotenv import load_dotenv
import os    

# Charger les variables d'environnement depuis .env 
load_dotenv()

# Utiliser les variables d'environnement pour définir les paramètres du projet
EXCUTABLE_PATH = os.getenv("dd")


# Chemin vers le fichier chromedriver.exe
CHROMEDRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "drivers", "chromedriver112.exe")

OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data","raw" ,"results.csv")

CONNECT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts","connect_vpn.bat")
DECONNECT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts","deconnect_vpn.bat")
VPNS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts","vpn_groups.json")



