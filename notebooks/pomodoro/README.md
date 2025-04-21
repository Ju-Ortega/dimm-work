# Pomodoro Tracker

This tool helps you track your work sessions using the Pomodoro technique. It allows you to record daily work hours and generate statistics to monitor your productivity over time.

## Directory Structure
pomodoro/
- data
    - pomodoro_log.csv   #CSV file with all tracking data
    - pomodoro_stats.png # Generated statistics visualization
- scripts/
    - add_pomodoro.py    # script to add new pomodoro records
    - analyzed.py        # script to generate statistics

## How to Use

### Adding a Pomodoro Record

To add a new work session record, use the `add_pomodoro.py` script with the following parameters:

```bash
python notebooks/pomodoro/scripts/add_pomodoro.py --date DD/MM/YY --hours H --minutes M --notes "Optional notes"

Examples:

# Add 5 hours and 30 minutes for today
python notebooks/pomodoro/scripts/add_pomodoro.py --hours 5 --minutes 30

# Add 4 hours and 15 minutes for April 18, 2025
python notebooks/pomodoro/scripts/add_pomodoro.py --date 18/04/25 --hours 4 --minutes 15

# Add 6 hours with a note
python notebooks/pomodoro/scripts/add_pomodoro.py --hours 6 --minutes 0 --notes "Focused work on PINNs implementation"

Viewing Statistics 
python notebooks/pomodoro/scripts/analyze.py