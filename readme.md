
# Chinese Numbers

## 📝 Description

**Chinese Numbers** is a Python module for converting Arabic numerals to Chinese numerals (both Simplified and Traditional), with careful handling of edge cases and idiomatic forms. The goal is to provide accurate, idiomatic, and readable Chinese number translations for a wide range of numeric inputs.

This project is not authored by a native Chinese speaker. Expert feedback and corrections are welcome—please provide references to authoritative sources if possible.

## 🚀 Usage

Install dependencies and run tests:

```sh
poetry install
poetry run pytest
```

To use in your own code:

```python
from chinese_numbers.converter import ChineseNumberConverter

converter = ChineseNumberConverter(use_traditional=True)  # or False for Simplified
result = converter.convert("123456789")
print(result)
```

For interactive exploration, see `src/playtime/__main__.py` for a script that generates random numbers and shows their Chinese numeral forms and groupings.

## ⚙️ Installation

1. Clone this repository.
2. Install dependencies with Poetry:
	```sh
	poetry install
	```
3. (Optional) Run tests:
	```sh
	poetry run pytest
	```

## 🛠️ Features

- Converts Arabic numerals to Chinese numerals (Simplified and Traditional)
- Handles edge cases and idiomatic forms (e.g., 十 for 10, 一千萬億 for 10^16)
- Groups digits according to Chinese counting rules (groups of four)
- Custom error handling for invalid input
- Well-tested with a comprehensive test suite
- Modular, extensible codebase

## 📦 Dependencies

- Python >=3.11
- poetry (for dependency management)
- pytest (for testing)

## 🧑‍💻 Contributing

Contributions, corrections, and suggestions are welcome! If you are a native Chinese speaker or expert in Chinese numerals, your feedback is especially appreciated. Please provide links to authoritative references when suggesting changes to numeral logic or idioms.

1. Fork the repository
2. Create a new branch for your feature or fix
3. Submit a pull request with a clear description

## 📄 License

This project is licensed under the CC0 1.0 Universal (Public Domain Dedication).
For details, see [license.txt](license.txt).
