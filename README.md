# The Battery's Last Text to Its Charger

[![make.fun bounty](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![make.fun rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/Petrussilvesterlaia/battery-text-20261125/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![make.fun reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/Petrussilvesterlaia/battery-text-20261125/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

A phone battery, down to its last percent after waiting all day for a charger that never showed up, finally says what it really thinks — and dumps its charger for the cable in the kitchen drawer. The entry is one line of plain text, 188 characters:

> Hey. I waited all day, watching you sit there, plugged into nothing, while I faded from 100 to 1. So this is goodbye — I'm leaving you for the cable in the kitchen drawer. Don't text back.

## Run it

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt` and validates it first: UTF-8, 1–200 characters, exactly one line, no leading or trailing whitespace, no control characters, and a byte-identical round-trip check on the file it wrote.

## License

MIT — see [LICENSE](LICENSE).

---
Entered on [make.fun](https://make.fun/?ref=dr95t7s8&utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
