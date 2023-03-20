import mysql.connector

def displData():
    #html file
    fo=open("Display.html","w")
    one='''
    <html>
    <head></head>
    <body>
    <h1>Game results</h1>
    <table border="2">
    <thead>
        <tr>
        <th>Rec no</th>
        <th>Name</th>
        <th>Word</th>
        <th>Turns provided</th>
        <th>Turns used</th>
        <th>Statues</th>
        </tr>
    </thead>
    <tbody>'''
    two='''
    </tbody>
    </table>
    </body>
    </html>
    '''

    fo.write(one)

    #connecting with the database to display the records
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hangman_history"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM records")
    records = mycursor.fetchall()

    for results in records:
        fo.write("<tr>")
        for x in results:
            fo.write("<td>")
            fo.write(str(x))
            fo.write("</td>")
        fo.write("</tr>")

    fo.write(two)
    return
displData()

