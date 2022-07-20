from flask import Flask, render_template, request, redirect
from helper_functions import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shorten_url', methods=['POST'])
def shorten_url():
    data = request.values

    url = data['url'].strip()
    custom_alias = data['custom_alias'].strip()

    if url[:7] != 'http://' and url[:8] != 'https://':
        url = 'http://' + url


    if not valid_url(url):
        return render_template("index.html", err_response='Invalid URL provided!')

    shortened = ''

    if custom_alias != '':
        if not valid_alias(custom_alias):
            return render_template("index.html", err_response='Custom alias provided can only be alphanumeric and have a maximum of 16 characters!')

        if check_alias_exist(custom_alias):
            return render_template("index.html", err_response='Custom alias already exists, please choose another one!')

        shortened = custom_alias
    else:
        num = get_counter()
        shortened = shorten(num, url)

    deletion_url = create_delete_url(shortened)

    add_new_shortened_url(shortened, url, deletion_url)

    return render_template("index.html", shortened_url=request.host_url + shortened, deletion_url=request.host_url + "delete_url/" + deletion_url)


@app.route('/shorten_url', methods=['GET'])
def reject():
    return render_template("index.html", err_response='Please use a post request!')


@app.route('/<shorten_id>', methods=['GET'])
def redirect_to_original(shorten_id):
    if not check_alias_exist(shorten_id):
        return render_template("index.html", err_response='Unable to find site URL to redirect to!')

    url = get_original_url(shorten_id)[0]

    return redirect(url, code=302)

@app.route('/delete_url/<deletion_url>', methods=['GET'])
def delete_url(deletion_url):
    if not check_deletion_url_exist(deletion_url):
        return render_template("index.html", err_response='Unable to find the URL to delete!')
    print(deletion_url)
    delete_url_from_db(deletion_url)

    return render_template("index.html", deletion_success="URL successfully deleted")