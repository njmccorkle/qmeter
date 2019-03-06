$name = $env:COMPUTERNAME

if ($name -eq "DESKTOP-DBH6673") {
	$env:PATH = "c:\git\qmeter\qmeter\venv\Scripts"
	$env:FLASK_APP = "qmeter.py"
	#$env:FLASK_APP = "c:\git\qmeter\qmeter\qmeter.py"
	#$env:FLASK_APP = "/c/git/qmeter/qmeter/qmeter.py"

}
elseif ($name -eq "W0209066") {
	$env:PATH = "c:\Users\a8n90zz\source\repos\njmccorkle\qmeter\qmeter\venv\Scripts"
	#$env:FLASK_APP = "c:\Users\a8n90zz\source\repos\njmccorkle\qmeter\qmeter\app.py"
	#$env:FLASK_APP = "/c/Users/a8n90zz/source/repos/njmccorkle/qmeter/qmeter/app.py"
	$env:FLASK_APP = "qmeter.py"
}

$env:FLASK_ENV="development"
#$env:FLASK_ENV="production"
#$env:FLASK_ENV="$null"