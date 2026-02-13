# Simple Password Generator CLI 

This is a simple password generator command line tool written in python. It optionally takes in a length parameter. The default length of the password is 12. The minimum length is 8. It also copies the password to the clipboard automatically once the password is generated.

## Installation
```bash
pipx install git+https://github.com/yourusername/your-repo.git
```

Or with pip:
```bash
pip install git+https://github.com/yourusername/your-repo.git
```

## Examples

```bash
# Example 1: generate password with length 20
pgen --length 20
```

```bash
# Example 2: generate password with default length
pgen
```