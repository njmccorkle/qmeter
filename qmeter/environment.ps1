$name = $env:COMPUTERNAME

if ($name -eq "DESKTOP-DBH6673") {
	$env:PATH = "c:\git\qmeter\qmeter\venv\Scripts"
	$env:FLASK_APP = "C:\git\qmeter\qmeter\runserver.py"
}
elseif ($name -eq "W0209066") {
	$env:PATH = "c:\Users\a8n90zz\source\repos\njmccorkle\qmeter\qmeter\venv\Scripts"
	$env:FLASK_APP = "c:\Users\a8n90zz\source\repos\njmccorkle\qmeter\qmeter\runserver.py"
}