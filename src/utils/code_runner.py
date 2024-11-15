import subprocess
import random
import string
import os

def run_python_code(code: str) -> str:
    file_name = f"./temp/scripts/{''.join(random.choices(string.digits, k=12))}.tsm"

    with open(file_name, "w") as temp_file:
        temp_file.write(code)

    result = subprocess.run(
        ["python", file_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    os.remove(file_name)

    return (result.stdout, result.stderr)

# ----------------------------------------------------------------
# Currently not implemented and should be implemented or removed
# ----------------------------------------------------------------