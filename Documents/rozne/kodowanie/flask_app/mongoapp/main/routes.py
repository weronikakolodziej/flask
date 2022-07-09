from crypt import methods
from re import I
from flask import Blueprint, render_template, redirect, url_for, request
from mongoapp.extensions import mongo



main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html', results_users='users', results_requests='requests', results_systems='systems')
