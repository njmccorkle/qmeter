$name = $env:COMPUTERNAME

if ($name = "DESKTOP-DBH6673") {
	$env:PATH = "c:\git\qmeter\qmeter\venv\Scripts"
	$env:FLASK_APP = "C:\git\qmeter\qmeter\runserver.py"
}
elseif ($name = "WSXXX") {
	$env:PATH = "c:\Users\a8n90zz\source\repos\njmccorkle\qmeter\qmeter\venv\Scripts"
	$env:FLASK_APP = "c:\Users\a8n90zz\source\repos\njmccorkle\qmeter\qmeter\$appName"
}