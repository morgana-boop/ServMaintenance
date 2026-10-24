# ServMaintenance

Daily uptime/latency check of listed URLs via GitHub Actions. Results in [STATUS.md](STATUS.md).

## Usage
Add URLs to `urls.txt` (one per line). Runs daily at 06:00 UTC, or manually via Actions > daily > Run workflow.

## Local
`python3 check.py`
