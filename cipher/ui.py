from click import secho
from . import __author__, __copyright__, __description__

def initialise_cipher():
	secho(f"""
  ____ _       _
 / ___(_)_ __ | |__   ___ _ __
| |   | | '_ \| '_ \ / _ \ '__|		{__description__}
| |___| | |_) | | | |  __/ |		
 \____|_| .__/|_| |_|\___|_|		{__copyright__}
        |_|
		""",
		fg="bright_red"
	)
	print(f"""\nThe private key is saved in the file called key 
so pls make sure to keep this file safe and also
Not to make any change to the file content or name.\n""")