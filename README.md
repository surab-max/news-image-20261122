# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/surab-max/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/surab-max/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

**Sunday 22 November 2026 — the world in one day, in one image.** A newspaper front page drawn entirely in code: COP31 collapsing in Antalya without a deal as the lead, Russian drones killing at least four in the Kyiv region as a five-storey block partly collapses in Dymer, suspected Ukrainian sea drones hitting a Russian warship at Benghazi, Democrats clinching at least 258 House seats — their largest majority since 1992 — and a candy-factory fire in Banten, Indonesia, killing three with 36 workers missing, with a space brief (BepiColombo entering orbit around Mercury after eight years) and a ticker carrying Bahrain, Mexico's capture of 'El Chapo Isidro', South Korea's education minister resigning, the AI stock sell-off and the Gukesh–Sindarov world chess title match. Every story is a verified event of 22 November 2026; `SOURCES.md` lists each one with the outlets that reported it. The image is a 1024×1024 PNG inside the competition's 1 MiB / 1024 px caps, and its masthead names the day it sums up.

**How it is built.** `tools/generate.py` renders the front page with Pillow (dated masthead, lead panel, four story panels, space brief, ticker) and writes `entry.png`. The graded program, `main.py` (Python 3.13, standard library only), copies `entry.png` to `/output/entry.png`, verifying the PNG's dimensions against the competition caps and the copy's SHA-256 against the source, so both grader runs produce byte-identical output with no network.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# then view out/entry.png — the front page of 22 November 2026
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=ys1ka8r4&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
