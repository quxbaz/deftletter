import os
from random import randint
from flask import Flask, render_template, redirect, request, url_for
from conf import conf
import stripe

stripe_keys = {
    'secret_key': os.environ['SECRET_KEY'],
    'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)
app.config.from_object(conf)

# TODO: If the form is empty, show a message that says you need to
# upload an image.
@app.route('/design', methods=['GET', 'POST'])
def design():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            filename = str(randint(10000, 99999))
            image_url = os.path.join(conf.UPLOAD_DIR, filename)[1:]
            file.save(image_url)
            return redirect(url_for('design_with_image', image_file=filename))
    return render_template('design.html')

# This is the same as The design view, but it passes an image file to
# the template.
@app.route('/design/<image_file>')
def design_with_image(image_file):
    image_url = os.path.join(conf.UPLOAD_DIR, image_file)
    return render_template('design.html', image_url=image_url)

@app.route('/shipping')
def shipping():
    return render_template('shipping.html')

@app.route('/customize')
def customize():
    return render_template('customize.html')

@app.route('/payment')
def payment():
    stripe_key = stripe_keys['publishable_key']
    return render_template('confirm.html', stripe_key=stripe_key, amount=100)

# Charges the user's credit card. Amount is in cents.
@app.route('/charge', methods=['POST'])
def charge():
    customer = stripe.Customer.create(
        email=request.form['email'],
        card=request.form['stripeToken']
    )
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=100,
        currency='usd',
        description='Test charge'
    )
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/our-cards')
def our_cards():
    return render_template('our-cards.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/')
def main():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
