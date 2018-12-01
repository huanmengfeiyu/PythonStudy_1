import cgi, shelve, sys, os

shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage()
print('Content-type:text/html')
sys.path.insert(0, os.getcwd())

replyhtml = """
<html>
<title>People Input Form</title>
<body>
<form method='POST' action='peoplecgi.py'>
<table>
<tr><th>Key<td><input type='text' name='key' value='%(key)s'>
$ROWS$
</table>
<p>
<input type='submit' value='Fetch' name='action'>
<input type='submit' value='Update' name='action'>
</form>
</body></html>
"""

rowhtml = '<tr><th>%s<td><input type="text" name=%s value="%%(%s)s">\n'
rowshtml = ''
for fieldname in fieldnames:
    rowshtml += (rowhtml % ((fieldname,) * 3))
replyhtml = replyhtml.replace('$ROWS$', rowshtml)


def htmlize(adict):
    new = adict.copy()
    for field in fieldnames:
        value = new[field]
        new[field] = cgi.escape(repr(value))
    return new


def fetchRecord(db, form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__
        fields['key'] = key
    except:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing or invalid key!'
    return fields
