import string 
import random
from pathlib import Path
import secrets # this is suppose to generate cryptographically secure randomness
import click
import pyperclip
from datetime import datetime

timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")

@click.command()
@click.option('--length', default=12, help="Length of password (default: 12)")
def generate_password(length):
    try:
        length = int(length)
    except Exception:
        click.echo(click.style("❌ Error: Please enter a number greater than 8", fg='red', bold=True))
        return

    if length and length < 8:
        click.echo(click.style("❌ Error: Minimum length is 8 characters!", fg='red', bold=True))
        return 

    letters_lowercase = string.ascii_lowercase
    letters_uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+=-[]{}"

    # the password should contain at least one of the 4s
    password = (
        secrets.choice(letters_lowercase) +
        secrets.choice(letters_uppercase) +
        secrets.choice(digits) +
        secrets.choice(special_characters)
    )

    # fill the remaining length with secrets characters 
    min_length = 8
    password += "".join(secrets.choice(
        letters_lowercase + letters_uppercase + digits + special_characters) for _ in range(max(length, min_length) - 4 # because 4 characters have already been added)
        
    ))

    # finally shuffle once again and this is weird because secrets.shuffle will do in place
    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    click.echo(click.style("💪 Strong Password Generated Successfully!", fg='green', bold=True))
    click.echo(click.style('🔒 Your Password: ', fg='yellow') + click.style(password, fg='bright_blue', bold=True))

    # copy the password to the clipboard
    pyperclip.copy(password)
    click.echo(click.style(f"📋 Password copied to clipboard!", fg='cyan'))

    # message to save the password to a password manager
    click.echo(click.style("🤝 Please save the password to a secure password manager", fg='magenta'))
if __name__ == "__main__":
    generate_password()