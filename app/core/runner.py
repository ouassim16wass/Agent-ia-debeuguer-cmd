import subprocess

def run_script(venv_python: str, script_path: str):
    """
    Exécute un script Python via l'interpréteur du venv
    et renvoie stdout + stderr (traceback).
    """
    result = subprocess.run(
        [venv_python, script_path],
        capture_output=True,
        text=True
    )

    stdout = result.stdout.strip()
    stderr = result.stderr.strip()

    return stdout, stderr
