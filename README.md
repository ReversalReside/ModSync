
# ModSync

Lightweight Python utility for verifying directory contents against a reference list. Automatically strips numbering and generates detailed comparison reports.

## ✨ Features
- 🔍 **Smart Comparison**: Matches actual files in a folder against a `.txt` reference list.
- 🔢 **Numbering Auto-Strip**: Ignores leading numbering (e.g., `1. `, `100. `) in both the reference list and filenames.
- 🖥️ **Interactive CLI**: Auto-detects available `.txt` lists or accepts manual input.
- 📊 **Clear Console Output**: Real-time stats on missing, extra, and matched files.
- 📄 **Detailed Report**: Exports a timestamped `comparison_result.txt` with full categorized lists.
- 🐍 **Zero Dependencies**: Built entirely with Python's standard library.

## 🚀 Quick Start
1. Place the script in the target directory.
2. Ensure a reference list file exists (e.g., `reference_list.txt`). Format: one filename per line (numbering optional).
3. Run the script:
   ```bash
   python ModSync.py
   ```
4. Select a list from the prompt or type a custom filename.
5. View results in the console and find the detailed report in `comparison_result.txt`.

## ⚙️ How It Works
1. Parses the reference `.txt` file, cleaning numbering and skipping metadata lines.
2. Scans the working directory (excludes the script itself, the reference list, and output report).
3. Compares file sets and categorizes them:
   - ❌ **Missing**: In list, not in folder.
   - ⚠️ **Extra**: In folder, not in list.
   - ✅ **Matched**: Present in both.
4. Prints a summary and saves a comprehensive `comparison_result.txt`.

## 📋 Requirements
- Python 3.6+
- No external packages required

## 📄 License
MIT

---
💡 *Tip: Ideal for mod pack verification, backup integrity checks, or automated CI/CD validation.*
