IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive

def wait():
    if INTERACTIVE_MODE:
        input("Press enter to continue.")
        
wait()
print("Scanning")
