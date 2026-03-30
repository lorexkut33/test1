import psutil
import time, os

cpu = psutil.cpu_percent(interval=1)

GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
RESET  = "\033[0m"

def processor():
    cpu = psutil.cpu_percent(interval=1)
    bar = make_bar(cpu)
    if cpu < 60:
        print(f"CPU: {GREEN}[{bar}] {cpu}%" + RESET)
    elif 60 <= cpu < 85:
        print(f"CPU: {YELLOW}[{bar}] {cpu}%" + RESET)
    else:
        print(f"CPU: {RED}[{bar}] {cpu}%" + RESET)

def ram():

    mem = psutil.virtual_memory()
    gb_total = mem.total / (1024 ** 3)
    gb_available = mem.available / (1024 ** 3)
    gb_used = mem.used / (1024 ** 3)
   
    print(f"Всего оперативной памяти: {gb_total:.2f} ГБ")
    print(f"Доступно оперативной памяти: {gb_available:.2f} ГБ")
    print(f"Использовано оперативной памяти: {gb_used:.2f} ГБ")

def process_raiting():

    processes = []
    for proc in psutil.process_iter(['name', 'cpu_percent']):
        if proc.info['name'] != "System Idle Process":
            processes.append(proc.info)

    sorted_processes = sorted(processes, key=lambda p: p['cpu_percent'], reverse=True)
    top3 = sorted_processes[:3]

    for proc in top3:
         print(f"{proc['name']}: {proc['cpu_percent']}")

def make_bar(percent):

    filled = int(percent / 100 * 16)
    bar = "█" * filled + "░" * (16 - filled)
    return bar

try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        processor()
        print("===============================================================")
        ram()
        print("===============================================================\n")
        process_raiting()
        time.sleep(1.5)

except KeyboardInterrupt:
    print(f"\nВыход из цикла")