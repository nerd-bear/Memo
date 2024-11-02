import click
from rich import print as rich_print
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.console import Console
import speedtest
from typing import Tuple
import sys

def format_speed(speed_bps: float) -> str:
    """Convert speed from bits per second to a human-readable format."""
    speed_mbps = speed_bps / 1_000_000
    return f"{speed_mbps:.2f} Mbps"

def run_speed_test(console: Console) -> Tuple[float, float, float, str]:
    """
    Run the speed test with progress indicators and error handling.
    Returns download speed, upload speed, ping, and server details.
    """
    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            init_task = progress.add_task("Initializing speed test...", total=1)
            st = speedtest.Speedtest()
            progress.update(init_task, advance=1, description="Speed test initialized ✓")
            
            server_task = progress.add_task("Finding best server...", total=1)
            st.get_best_server()
            server_info = f"{st.best['host']} ({st.best['country']})"
            progress.update(server_task, advance=1, description="Best server found ✓")
            
            download_task = progress.add_task("Testing download speed...", total=1)
            download = st.download()
            progress.update(download_task, advance=1, description=f"Download: {format_speed(download)} ✓")
            
            upload_task = progress.add_task("Testing upload speed...", total=1)
            upload = st.upload()
            progress.update(upload_task, advance=1, description=f"Upload: {format_speed(upload)} ✓")
            
            ping = st.results.ping

            return download, upload, ping, server_info

    except Exception as e:
        rich_print(f"[bold red]ERROR:[/bold red] Speed test failed: {str(e)}")
        rich_print("Please ensure you have a working internet connection and try again.")
        sys.exit(1)

@click.command()
@click.option("--token", help="Discord bot token", required=True)
@click.option("--skip-speedtest", is_flag=True, help="Skip the internet speed test")
def main(token: str, skip_speedtest: bool):
    """Launch the Discord bot with optional internet speed testing."""
    console = Console()

    if not token.strip():
        rich_print("[bold red]ERROR:[/bold red] Invalid token provided.")
        rich_print("Usage: python launcher.py --token <token>")
        raise click.Abort()

    if not skip_speedtest:
        rich_print("\n[bold blue]Running Internet Speed Test[/bold blue]")
        rich_print("This may take a minute...\n")

        download, upload, ping, server = run_speed_test(console)

        rich_print("\n[bold green]Speed Test Results:[/bold green]")
        rich_print(f"🔽 Download: {format_speed(download)}")
        rich_print(f"🔼 Upload: {format_speed(upload)}")
        rich_print(f"📡 Ping: {ping:.1f} ms")
        rich_print(f"🖥️  Server: {server}\n")

        if download < 5_000_000 or upload < 1_000_000:  
            rich_print("[bold yellow]Warning:[/bold yellow] Your internet connection appears to be slow, "
                      "which might affect bot performance.\n")

    from src.bot import Memo

    try:
        rich_print("[bold blue]Starting Discord Bot[/bold blue]")
        Memo.run(token)
    except Exception as e:
        rich_print(f"[bold red]ERROR:[/bold red] Failed to start bot: {str(e)}")
        raise click.Abort()

if __name__ == "__main__":
    main()