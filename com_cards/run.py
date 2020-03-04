"""Runs the application"""
from tags_registry import APP

print("hello world")

APP.run(host='0.0.0.0', port=80, debug=True)
