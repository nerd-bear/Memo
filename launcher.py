import click
from rich import print as rich_print


@click.command()
@click.option("--token", help="Discord bot token", required=True)
def main(token: str):
    if not token.strip():
        rich_print("[bold red]ERROR:[/bold red] Invalid token provided.")
        rich_print("Usage: python3 ./launcher.py --token <token>")
        raise click.Abort()

    from src.bot import CRAC

    try:
        CRAC.run(token)
    except Exception as e:
        rich_print(f"[red]{e}[/red]")
        click.Abort()


if __name__ == "__main__":
    main()

# python ./launcher.py --token "MTI4OTkyMTQ3NjYxNDU1MzY3Mg.GNo3VX.kjVPN-1ri34TtfuWZ-ADqhSeW56fARaLu7pMnk"
