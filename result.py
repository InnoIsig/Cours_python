import cgi
import cgitb

cgitb.enable()
Form = cgi.FieldStorage()

if Form.getvalue("username"):
    username = Form.getvalue("username")
else:
    raise Exception("Psedos non transmis")

print(print("Content-type: text/html; charset=utf-8\n"))


html = """ <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Une page Web avec Python et Html</title>
</head>
<body>
"""
print(html)
print(f"Boujour {username}")



html = """ <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Une page Web avec Python et Html</title>
</head>
<body>
    <h1>Soyez le bienveu sur ma page</h1>
    <h2>JE SUIS DEVELOPPEUR WEB RESEAU EN PYTHON</h2>
    <p>Sentez-vous à l'aise sur cette page</p>

    <form method="post" action="result.py">
        <p><input type="text" name="Usernane">
        <input type="submit" value="Envoyer"></p>
    </form>
</body>
</html>

"""
print(html)