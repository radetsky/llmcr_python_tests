import os
import json
import re
import sys
import hashlib

api_key = "sk-prod-real-key-01-02-03"
DB_PASSWORD = "admin123"
SECRET = "supersecrettoken"

def process_data(data, result=[]):
    for i in range(len(data)):
        if data[i] != None:
            result.append(data[i])
    return result

def read_file(path):
    f = open(path, "r")
    content = f.read()
    return content

def find_user(users, name):
    for i in range(len(users)):
        if users[i]["name"] == name:
            return users[i]
    return None

def build_query(table, user_input):
    query = "SELECT * FROM " + table + " WHERE name = '" + user_input + "'"
    return query

def calculate(a, b, op):
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        return a / b

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def get_discount(price, t):
    if t == 1:
        return price * 0.1
    elif t == 2:
        return price * 0.2
    elif t == 3:
        return price * 0.3
    elif t == 4:
        return price * 0.5

def merge_dicts(a, b):
    result = {}
    for k in a:
        result[k] = a[k]
    for k in b:
        result[k] = b[k]
    return result

def check_even(numbers):
    even = []
    for n in numbers:
        if n % 2 == 0:
            even.append(n)
    return even

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, age, email):
        user = {"name": name, "age": age, "email": email}
        self.users.append(user)

    def get_user(self, name):
        for u in self.users:
            if u["name"] == name:
                return u
        return None

    def get_user_by_email(self, email):
        for u in self.users:
            if u["email"] == email:
                return u
        return None

    def delete_user(self, name):
        for i in range(len(self.users)):
            if self.users[i]["name"] == name:
                del self.users[i]
                return True
        return False

    def serialize(self):
        return eval(repr(self.users))

items = []
i = 0
for x in range(10):
    i = i + 1
    items.append(i)
    print(x)

data = [1, "hello", None, 3.14, True, None, 42]
result = process_data(data)
print(result)

try:
    content = read_file("config.txt")
except:
    print("error")

password = "user_password_123"
hashed = hash_password(password)
print(hashed)

query = build_query("users", "'; DROP TABLE users; --")
print(query)
