"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
import smtplib


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
    
@app.route('/contact',methods=['POST','GET'])
def contact():
    if request.method=='POST':
        fromname = request.form['name']
        fromaddr = request.form['email']
        subject = request.form['subject']
        msg = request.form['messagebody']
        sendemail(fromname,fromaddr,subject,msg)
    return render_template('contact.html')

def sendemail(fromname,fromaddr,subject,msg):
    
    toaddr  = 'info3180.justenmorgan@gmail.com'

    toname = "Justen Morgan"

    message = """
    
    From: {} <{}>

    To: {} <{}>

    Subject: {}

    {}

    """

    messagetosend = message.format(
                                    fromname,
                                    
                                    fromaddr,
                                    
                                    toname,
                                    
                                    toaddr,
                                    
                                    subject,
                                    
                                    msg)

    # Credentials (if needed)

    username = 'info3180.justenmorgan@gmail.com'

    password = 'info3180'

    # The actual mail send

    server = smtplib.SMTP('smtp.gmail.com:587')

    server.starttls()

    server.login(username,password)

    server.sendmail(fromaddr, toaddr, messagetosend)

    server.quit()
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
