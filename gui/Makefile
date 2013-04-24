ui:
	@pyuic4 core.ui -o coreui.py

build:
	@python pyinstaller-2.0/pyinstaller.py -w -F stexplorer.py

py2exe:
	@python setup.py py2exe

clean:
	@rm -rf dist build logdict*.log *.spec
