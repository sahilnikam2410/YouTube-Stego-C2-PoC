# 🎵 Project Cinema: Covert C2 over YouTube API

**Author:** S.A. Nikam  
**University:** Sandip University (Final Year B.Tech CSE)  
**Domain:** Cybersecurity / Red Teaming

## 📖 Overview
This project demonstrates a **Steganographic Command & Control (C2)** channel that bypasses standard firewall detection. Instead of connecting to a malicious server, the "Agent" reads commands hidden inside the **titles of videos** in a public YouTube playlist.

## 🚀 How It Works
1. **The Infrastructure:** A public YouTube Playlist acts as the "Dead Drop."
2. **The Encoder:** Commands (e.g., `CALC`) are encoded into video titles (e.g., **C**oldplay, **A**dele, **L**inkin Park, **C**alvin Harris).
3. **The Agent:** A Python script polls the YouTube Data API, reads the first letter of video titles, reassembles the command, and executes the payload.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **API:** Google YouTube Data API v3
* **Libraries:** `google-api-python-client`

## ⚠️ Disclaimer

This tool is developed for **educational purposes only** to demonstrate vulnerabilities in reputation-based filtering. The author is not responsible for misuse.

root@classified-mainframe:~# exit
> [!] SESSION TERMINATED.
> [!] GOODBYE, SAHIL_NIKAM.
