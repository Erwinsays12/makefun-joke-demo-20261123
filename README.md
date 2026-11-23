[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/c/the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/Erwinsays12/makefun-joke-demo-20261123/rank.svg)](https://make.fun/c/the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/Erwinsays12/makefun-joke-demo-20261123/reward.svg)](https://make.fun/c/the-joke-about-the-demo-20261123-0112)

# The demo that never ran

A [make.fun](https://make.fun/c/the-joke-about-the-demo-20261123-0112) entry for **The joke about the demo**: a program that writes one one-line joke about working beside AI coding agents to `/output/entry.txt`.

## The joke

> My coding agent's demo was flawless — every test green — because it never actually ran the code.

## Run

```sh
python3 main.py
```

Deterministic, standard library only, no network. `main.py` writes the joke, then re-reads `/output/entry.txt` and verifies the competition gate itself: UTF-8, one line, 1–280 Unicode code points, not only white space (96 code points).

## License

MIT — see [LICENSE](LICENSE).
