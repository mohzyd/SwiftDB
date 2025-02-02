# SwiftDB

SwiftDB is a fast and simple key-value database for Python, designed for easy integration, high performance, and minimal setup. Whether you're building a small project or need lightweight storage for your application, SwiftDB is the perfect solution.

## Features

- Simple and intuitive key-value store
- Lightweight and fast
- Persistent storage (optional, using JSON or file-based storage)
- Designed for ease of use with minimal setup
- No external dependencies
- Written entirely in Python

## Installation

You can install SwiftDB via pip:

```bash
pip install swiftdb

Usage
Basic Usage
Once installed, you can use SwiftDB in your Python projects like this:

from swiftdb import SwiftDB

# Create a new database instance
db = SwiftDB()

# Store a key-value pair
db.set("name", "SwiftDB")

# Retrieve a value by key
print(db.get("name"))  # Output: SwiftDB

# Delete a key-value pair
db.delete("name")

# Retrieve a value after deletion
print(db.get("name"))  # Output: None
Persistent Storage
By default, SwiftDB stores data only in memory. If you want to persist data across sessions, you can enable file-based storage (e.g., saving to a JSON file):

from swiftdb import SwiftDB

# Create a persistent database instance
db = SwiftDB(file_path="data.json")

# Store data
db.set("username", "admin")
db.set("password", "securepassword")

# Retrieve data
print(db.get("username"))  # Output: admin

# Save changes to the file
db.save()
Advanced Usage
SwiftDB also supports more advanced use cases:

Batch Operations: Store or retrieve multiple key-value pairs at once.
Custom Serialization: Use custom methods to serialize/deserialize data for storage.

# Batch setting multiple key-value pairs
db.set_bulk([("key1", "value1"), ("key2", "value2")])

# Batch retrieving multiple values
keys = ["key1", "key2"]
values = db.get_bulk(keys)
print(values)  # Output: ['value1', 'value2']
Error Handling
If you attempt to get or delete a non-existent key, SwiftDB will return None:

result = db.get("nonexistent_key")  # Output: None
Clear All Data
You can clear all stored data from the database:

db.clear()  # Removes all key-value pairs
Functions
set(key, value): Adds a new key-value pair to the database or updates an existing one.
get(key): Retrieves the value for a given key. Returns None if the key doesn’t exist.
delete(key): Removes a key-value pair from the database.
set_bulk(pairs): Stores multiple key-value pairs at once.
get_bulk(keys): Retrieves multiple values at once for a list of keys.
clear(): Clears all data stored in the database.
save(): Persists the data to a file (if using file-based storage).
Contributing
Contributions are welcome! If you'd like to contribute to the development of SwiftDB, please follow these steps:

Steps to contribute:
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new pull request.
Please ensure your code follows Python’s PEP 8 style guide and includes tests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
If you have any questions, suggestions, or issues, feel free to open an issue or reach out directly:

Author: Your Name
Email: [your-email@example.com]
Acknowledgments
Thanks to the Python community for building such a great ecosystem of tools.
Special thanks to contributors for their efforts!