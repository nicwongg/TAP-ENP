import sqlite3
import re
import string
from urllib.parse import unquote
import hashlib


def get_db_connection():
    conn = sqlite3.connect("db/shorturls.db")
    conn.row_factory = sqlite3.Row
    return conn


def valid_url(url):
    return re.match(regex, url) is not None


def get_counter():
    conn = get_db_connection()
    counter = conn.execute("SELECT MAX(id) FROM urls").fetchone()[0] + 1
    conn.close()
    return counter


def shorten(num, url):
    url = unquote(url)
    _divmod = divmod

    shortened = ""
    while num:
        num, rem = _divmod(num, BASE)
        shortened += ALPHANUMERICS[rem]
    return shortened


def add_new_shortened_url(shortened, url, deletion_url):
    conn = get_db_connection()
    conn.execute(
        f"""INSERT INTO urls (shorten_id, original_url, deletion_url) VALUES (?, ?, ?);""", (shortened, url, deletion_url))
    conn.commit()
    conn.close()


def valid_alias(custom_alias):
    return custom_alias.isalnum() and len(custom_alias) <= 16


def check_alias_exist(custom_alias):
    conn = get_db_connection()
    res = conn.execute(
        f"SELECT * from urls where shorten_id = '{custom_alias}'").fetchall()
    conn.close()
    return len(res) > 0

def check_deletion_url_exist(deletion_url):
    conn = get_db_connection()
    res = conn.execute(
        f"SELECT deletion_url from urls where deletion_url = '{deletion_url}'").fetchone()
    conn.close()
    return len(res) > 0

def delete_url_from_db(deletion_url):
    conn = get_db_connection()
    conn.execute(f"DELETE FROM urls WHERE deletion_url = (?);", (deletion_url,))
    conn.commit()
    conn.close()

def get_original_url(custom_alias):
    conn = get_db_connection()
    url = conn.execute(
        f"SELECT original_url from urls where shorten_id = '{custom_alias}'").fetchone()
    conn.close()
    return url


def create_delete_url(shortened_url):
    result = hashlib.md5(shortened_url.encode()).hexdigest()
    print(result)
    return result


ALPHANUMERICS = string.digits + string.ascii_letters
BASE = len(ALPHANUMERICS)

regex = re.compile(
    r'^(?:http|ftp)s?://'
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r'(?::\d+)?'
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
