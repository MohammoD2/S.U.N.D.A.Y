from AppOpener import open
def desktop(text):
    try:
       open(text, match_closest=True)
    except Exception as e:
        print(f"Failed to open {text}: {e}")
    else:
        pass
