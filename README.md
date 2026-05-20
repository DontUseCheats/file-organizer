# 📁 File Organizer

A command-line tool that automatically sorts files in a folder by **type** and/or **size** — with full undo support.

---

## Features

- Sort files into subfolders by category (Images, Documents, Videos, Code, etc.)
- Sort files by size (Tiny, Small, Medium, Large, Huge)
- Combine both: organize by type, then by size within each category
- Dry run mode — preview changes before committing
- Undo support — reverse the last organize operation

---

## Requirements

- Python 3.7+
- No external dependencies — uses only the standard library

---

## Installation

```bash
git clone https://github.com/DontUseCheats/file-organizer.git
cd file-organizer
```

---

## Usage

```bash
python main.py <folder_path> [options]
```

### Options

| Flag | Description |
|------|-------------|
| `--sort-by type` | Group files by category |
| `--sort-by size` | Group files by size |
| `--sort-by both` | Sort by type, then size *(default)* |
| `--dry-run` | Preview without moving files |
| `--undo` | Reverse the last organize operation |

### Examples

```bash
# Organize Downloads (type + size)
python main.py ~/Downloads

# Sort by file type only
python main.py ~/Downloads --sort-by type

# Preview without moving anything
python main.py ~/Downloads --dry-run

# Undo the last run
python main.py ~/Downloads --undo
```

---

## File Categories

| Category | Extensions |
|----------|-----------|
| Images | `.jpg`, `.png`, `.gif`, `.svg`, `.webp` … |
| Videos | `.mp4`, `.mov`, `.avi`, `.mkv` … |
| Audio | `.mp3`, `.wav`, `.flac`, `.aac` … |
| Documents | `.pdf`, `.doc`, `.docx`, `.txt` … |
| Spreadsheets | `.xls`, `.xlsx`, `.csv` … |
| Code | `.py`, `.js`, `.html`, `.css`, `.go` … |
| Archives | `.zip`, `.tar`, `.gz`, `.rar` … |
| Other | Anything not matched above |

## Size Buckets

| Label | Range |
|-------|-------|
| Tiny | < 1 KB |
| Small | 1 KB – 1 MB |
| Medium | 1 MB – 100 MB |
| Large | 100 MB – 1 GB |
| Huge | > 1 GB |

---

## How Undo Works

After each run, a `.organizer_log.json` file is saved in the target folder. Running `--undo` reads that log, moves every file back to its original location, then deletes the log.

---

## License

MIT