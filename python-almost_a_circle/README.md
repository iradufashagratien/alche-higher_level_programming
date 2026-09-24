# python-almost_a_circle

An Object-Oriented Programming project modeling Rectangle and Square
shapes through a shared Base class, with full unit test coverage and
PEP 8 compliance.

## Project Structure

- `models/base.py`      : Base class — manages id assignment, JSON
  serialization/deserialization, saving to and loading from file
- `models/rectangle.py` : Rectangle class, inherits from Base — width,
  height, x, y with validated setters, area, display, update,
  to_dictionary
- `models/square.py`    : Square class, inherits from Rectangle — a
  square is a rectangle with equal width and height
- `tests/test_models/`  : Unit tests, mirroring the models/ structure

## How to Run

```bash
python3 -m unittest discover tests
```

## Requirements

- Python 3.8.5
- pycodestyle 2.7.*
- No external dependencies

## AI Usage Disclosure

AI tools were used as a learning and debugging aid to help design the
class structure, explain validation logic, and generate accompanying
unit tests. All code was reviewed and is understood by me.
