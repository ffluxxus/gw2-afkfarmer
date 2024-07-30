# SOURCE CODE CAN BE PURCHASED. CONTACT MY DISCORD FOR MORE INFO!

bold = Style.BRIGHT
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
purple = Fore.MAGENTA
white = Fore.WHITE

start = int(time.time())
VK_ALT = 0x12
VK_CONTROL = 0x11
VK_SHIFT = 0x10
VK_N = 0x78
Sleep = time.sleep

found_files = []
dirr = "C:\\\Program Files\\AutoHotkey\\"
names = ["AutoHotkeyU64.exe", "AutoHotkey64.exe"]
for root, _, files in os.walk(dirr):
    for file in files:
        if file in names:
            found_files.append((file, os.path.join(root, file)))
ahkPath = found_files[0][1]
pytesseract.pytesseract.tesseract_cmd = (os.getcwd()).replace("\\", "\\\\") + "\\tess\\tesseract.exe"

v = "0.0.1"
pvz = "Plants vs Zombies Garden Warfare 2"
startingDelay = 5
actionDelay = 2
pSelectDelay = 7.5

modeSetting = 5
mapSetting = 5
difficultySetting = 3

debugMode = False

def is_key_down(key_code):
    return user32.GetAsyncKeyState(key_code) & 0x8000 != 0

def key():
    while True:
        ctrl = is_key_down(VK_CONTROL)
        shift = is_key_down(VK_SHIFT)
        n = is_key_down(VK_N)
        
        if (ctrl and shift and n):
            debugMode = not debugMode
            if debugMode: 
                print(f"{purple}[Debug] Debug mode enabled.") 
                f = open("debug", "w")
                f.close()
                if debugMode: print(f"{purple}[Debug] \"debug\" file created.")
            else: 
                print(f"{purple}[Debug] Debug mode disabled.")
                if os.path.exists("debug"):
                    os.remove("debug")
                    if debugMode: print(f"{purple}[Debug] \"debug\" file removed.")

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    if debugMode: print(f"{purple}[Debug] Tasklist retrieved and checked for \"{process_name}\".")
    return last_line.lower().startswith(process_name.lower())

def rpc():
    RPC.update(
        large_image = "gw2logo",
        large_text = "Garden Warfare 2 | Steam",
        small_image = "logo",
        small_text = "by fluxxuss#0",
        details = f"GW2 Coin Farmer v{v}",
        state = f"Farmed Money: ",
        start = start,
        buttons = [{
            "label": "Preview Product",
            "url": "https://fluxus.000.pe/product-previews/gw2coins.png"
        },{
            "label": "Purchase Product",
            "url": "https://fluxxuss.mysellix.io/product/python-ahk-afk-farming-for-coins"
        }]
    )

def getPos():
    x, y = pyautogui.position()
    return x, y
