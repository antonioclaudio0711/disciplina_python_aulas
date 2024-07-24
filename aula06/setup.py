from cx_Freeze import Executable, setup

executables = [Executable('main.py')]

setup(
    name="CalculatorApp",
    version="1.0",
    description="Simple Calculator App",
    executables=executables
)