import pytest


def setup_module(module):
    print("Creating DB Connection")


def teardown_module(module):
    print("Clsing DB Connection")


def setup_function(function):
    print("Launching Browser")


def teardown_function(function):
    print("Quitting the Browser")


def test_do_login():
    print("Executing Login Test")


def test_user_reg():
    print("Executing User registration Test")
