#!/usr/bin/python
#!/usr/bin/python2.3
#!/usr/bin/python2.4
#!c:\Python24\python.exe
#!c:\Python25\python.exe
#!h:\Python27\python.exe
import cgitb
import pdfval
import pdfgen

# cgitb.enable(display=0, logdir="/tmp")
cgitb.enable()

print "Content-Type: text/html"
print
print """\
<html>
<body>
<h2>Hello World!</h2>
</body>
</html>
"""

form = cgi.FieldStorage()
# if "name" not in form or "addr" not in form:
#     print "<H1>Error</H1>"
#     print "Please fill in the name and addr fields."
#     return
# print "<p>name:", form["name"].value
# print "<p>addr:", form["addr"].value

data = {}
files = {}
name = 0
value = 0

def printError(show):
    print "<p>The <strong>", show, "</strong> field is not properly filled.</p>"

# A safe function!
dangerous = ['/', '\\', '*'] # TODO
def GetValue(form, name):
    global dangerous
    global form
    if name not in form:
        return -1
    value = form.getlist(name)
    ret = ",".join(value)
    if len(ret) > 65535:
        print "<p>The aragraph is too long.</p>"
        return -1
    for d in dangerous:
        if d in ret:
            print "<p>Please do not include \'<strong>", d, "</strong>\' in any fields.</p>"
            return -1
    return ret

# TODO
# Return: 1: complete. -1: incomplete.
def GetFile(realname, formname):
    global name = realname
    fileitem = form[formname]
    if fileitem.file:
        # It's an uploaded file; count lines
        # print "file: "+name;
        linecount = 0
        while 1:
            line = fileitem.file.readline()
            if not line: break
            linecount = linecount + 1
            # print "line: ",linecount
        if fileitem.done == -1:
            print "<p>File", realname,"is broken.</p>"
        if pdfval.isPDF(fileitem)
        return fileitem.done;


def GetRequired(realname, formname):
    global name = realname
    global value = GetValue(formname)
    if value == -1:
        printError(name)
        return -1
    data[name] = value
    return 0

def GetOptional(realname, formname):
    global name = realname
    global value = GetValue(formname)
    if value == -1:
        value = "None"
    data[name] = value
    return 0

def GetMultiple(realname, array):
    global name = realname
    global value = ""
    for formname in array:
        avalue = GetValue(formname)
        if avalue != -1:
            value += ", "+avalue
    data[name] = value
    return 0


# Get Data

if GetRequired("Name", "Field1") == -1:
    return -1
if GetRequired("Email", "Field4") == -1:
    return -1
if GetRequired("Available", "Field1342") == -1:
    return -1
if value != "Yes"
    GetOptional("Explain", "Field1342_other_No (please explain)")
GetOptional("Website", "Field10")
if GetRequired("Phone", "Field9") == -1:
    return -1
if GetRequired("Major", "Field6") == -1:
    return -1
GetOptional("University", "Field1345")

GetMultiple("Experience", ["Field635", "Field636"])
GetMultiple("Familiar concepts", ["Field529", "Field532", 
    "Field533", "Field534"]);
GetMultiple("Plan", ["Field1038"]);
if GetRequired("Work Samples", "Field116") == -1:
    return -1

if GetFile("Resume", "Field3") == -1:
    return -1
if GetFile("Transcript", "Fieldt") == -1:
    return -1
if GetFile("CoverLetter", "Fieldc") == -1:
    return -1
if GetRequired("Motivation", "Field12") == -1:
    return -1
if GetRequired("Ideas", "Field126") == -1:
    return -1

GetMultiple("Experience", ["Field836", "Field837", "Field838", "Field839", "Field840", "Field841", "Field842"])



