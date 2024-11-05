import click
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.console import Console
import speedtest
from typing import Tuple
from src.utils.helper import log_info
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
        log_info(f"Speed test failed: {str(e)}", error=True)
        log_info("Please ensure you have a working internet connection and try again.", error=True)
        sys.exit(1)

@click.command()
@click.option("--token", help="Discord bot token", required=True)
@click.option("--skip-speedtest", is_flag=True, help="Skip the internet speed test")
def main(token: str, skip_speedtest: bool):
    """Launch the Discord bot with optional internet speed testing."""
    console = Console()

    if not token.strip():
        log_info("Invalid token provided.", error=True)
        log_info("Usage: python launcher.py --token <token>", error=True)
        raise click.Abort()

    if not skip_speedtest:
        log_info("Running Internet Speed Test", startup=True)
        log_info("This may take a minute...\n", startup=True)

        download, upload, ping, server = run_speed_test(console)

        log_info("Speed Test Results:", startup=True)
        log_info(f"Download: {format_speed(download)}", startup=True)
        log_info(f"Upload: {format_speed(upload)}", startup=True)
        log_info(f"Ping: {ping:.1f} ms", startup=True)
        log_info(f"Server: {server}\n", startup=True)

        if download < 5_000_000 or upload < 1_000_000:  
            log_info("Your internet connection appears to be slow, which might affect bot performance.", warning=True)

    from src.bot import Memo

    try:
        log_info("Starting Discord Bot", startup=True)
        Memo.run(token)
    except Exception as e:
        log_info(f"Failed to start bot: {str(e)}", error=True)
        raise click.Abort()
    
main()