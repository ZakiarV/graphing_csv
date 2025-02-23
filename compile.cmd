if not exist build mkdir build
if exist GraphCSV.exe (
    echo GraphCSV.exe already exists. Skipping compilation.
    cls
    exit /b 0
)
if not exist GraphCSV.exe (
    echo Compiling GraphCSV...
    python -m nuitka --standalone --onefile --output-dir=build --output-filename=GraphCSV main.py --enable-plugin=tk-inter
    move build\GraphCSV.exe .
)
if exist GraphCSV.exe (
    echo Compilation successful.
) else (
    echo Compilation failed.
)

cls