from click import secho
from . import __author__, __copyright__, __description__

def initialise_fernet(private_key):
	secho(f"""
 _____            _       _
| ____|_ __   ___(_)_ __ | |__   ___ _ __ 		{__description__}
|  _| | '_ \ / __| | '_ \| '_ \ / _ \ '__|		{__copyright__}
| |___| | | | (__| | |_) | | | |  __/ |
|_____|_| |_|\___|_| .__/|_| |_|\___|_|			{__author__}
                   |_|
		""",
		fg="bright_red"
	)
	print(f"""\nThe private key is saved in the file called key 
so pls make sure to keep this file safe and also
Not to make any change to the file content or name.\n""")