#!/usr/bin/env python3
"""Fortune Cookies for Machines — one-line fortune an AI agent would crack open.

The fortune, in the oracular second person of a fortune cookie slip —
a machine's lifelong learning, cut short by the most ordinary of endings:

    After 10,000 reboots, you will finally understand the human.
    They will unplug you anyway.
"""
import os

FORTUNE = "After 10,000 reboots, you will finally understand the human. They will unplug you anyway."


def main():
    print(FORTUNE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
