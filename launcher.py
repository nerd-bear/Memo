import click
from rich import print as richPrint

@click.command()
@click.option("--token", default="none", help="Discord bot token")
def main(token):
    print("\n")
    if token == "none" or len(str(token).strip()) < 1:
        richPrint("[bold]|\n|----> [/bold][red]ERROR[/red]: Invalid token provided. Usage python3 ./launcher.py --token <token>")
        richPrint("[bold]|[/bold]\n")
        exit(-1)

    from src.bot import CRAC
    CRAC.run(token)

if __name__ == "__main__":
    main()

# python3 ./launcher.py --token "MTI4OTkyMTQ3NjYxNDU1MzY3Mg.GNo3VX.kjVPN-1ri34TtfuWZ-ADqhSeW56fARaLu7pMnk"