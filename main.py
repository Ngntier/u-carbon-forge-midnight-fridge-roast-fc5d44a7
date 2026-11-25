import os

MAX_CHARS = 200

SETUP = "My fridge locks at midnight like it's guarding nuclear codes"
PUNCHLINE = "relax, you're a box of leftovers, not the Pentagon."
ENTRY_LINE = f"{SETUP} — {PUNCHLINE}"

assert 1 <= len(ENTRY_LINE) <= MAX_CHARS
assert ENTRY_LINE.strip()

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)

if __name__ == "__main__":
    main()
