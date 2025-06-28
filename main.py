import subprocess

def main():
    print("Testando o Módulo IdentifierMain")
    subprocess.run(["python", "routines/IdentifierMain.py", "abc"])

    print("Execuando o Teste test_validate")
    subprocess.run(["python", "-m", "pytest", "-v", "routines/tests/test_validate.py"])

    print("Execuando o Teste test_validate")
    subprocess.run(["python", "-m", "pytest", "-v", "routines/tests/test_validate.py"])

    print("Medidando a Cobertura")
    subprocess.run(["coverage", "run", "-m", "pytest", "routines/tests"])
    subprocess.run(["coverage", "report"])
    subprocess.run(["coverage", "html", "-d", "coverage"])
    subprocess.run(["coverage", "run", "--branch", "-m", "pytest", "routines/tests"])

if __name__ == "__main__":
    main()
