# Math Haxor #
App to generate math problems

* Run as a interractive terminal or GUI tool.
* Can output to CLI or PDF

## Windows Prerequesites
* Install [wkhtmltopdf](https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf) and add the bin directory to the PATH environement variable.
* Python ^3.10

## Windows Installation
```cmd
python3 -m venv venv
venv\Scripts\actiavate.bat
pip install -r requriements.txt
```

## Linux (Ubuntu 22) Installation
```bash
sudo apt install python3-tk
sudo apt install wkhtmltopdf
python3 -m venv venv
chmod +x venv/bin/activate
source venv/bin/activate
pip install -r requirements.txt 
```


## GUI tool
To use the GUI tool run it from the terminal, of execute from the file by double clicking on it.
```bash
python3 gui.py
```


## Interactive terminal tool
```bash
python3 cli.py
```

## Roadmap
Features I want to implement are:

### Binary Problem generator
- Binary number reading
- Binary addition
- Binary subraction
- Binary shift
- Binary to ASCII
- ASCII to binary

### Trigonometry problem generator
- Triangle angles
- Square angles

### PDF generator
- Swith from HTML2PDF to proper user of pdfkit without the use of webkit
- Logo, and credits on page
- Default filename to include problem type and creation date.
