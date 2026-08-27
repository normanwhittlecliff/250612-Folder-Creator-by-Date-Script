import os
import re

# =========================================================
# CONFIG
# =========================================================

ROOT_FOLDER = r"C:\Users\norma\Pictures\Storage"
#ROOD_FOLDER = r"C:\Users\norma\Pictures\Storage\Storage\Filtering"
#ROOT_FOLDER = r"C:\Users\norma\Pictures\Storage\BN"
#ROOT_FOLDER = r"C:\Users\norma\Desktop\temp\a"


# =========================================================
# REGEX
# =========================================================
# Matches:
# (1)
# (2.)
# (3.14)
#
# Captures:
# group(1) = integer part
# group(2) = decimal part (optional)
#
# Examples:
# "(2.)"    -> int="2", decimal="."
# "(3.14)"  -> int="3", decimal=".14"
# "(12)"    -> int="12", decimal=None
#
pattern = re.compile(r"\((\d+)(\.\d*)?\)")

# =========================================================
# FUNCTION
# =========================================================

def fix_parentheses_numbers(filename):
    def replacer(match):
        integer_part = match.group(1)
        decimal_part = match.group(2) or ""

        # Add leading zero if number has only 1 digit
        padded_integer = integer_part.zfill(2)

        return f"({padded_integer}{decimal_part})"

    return pattern.sub(replacer, filename)

# =========================================================
# MAIN
# =========================================================

for root, dirs, files in os.walk(ROOT_FOLDER):
    for file in files:
        old_path = os.path.join(root, file)

        new_name = (fix_parentheses_numbers(file)).replace("-", "_")

        # Skip if nothing changed
        if new_name == file:
            continue

        new_path = os.path.join(root, new_name)

        print(f'Renaming: "{file}"  ->  "{new_name}"')

        os.rename(old_path, new_path)

input("Done. Press Enter to quit.")
