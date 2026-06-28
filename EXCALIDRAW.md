# Excalidraw Notes

## Automatic Flow

Drop Excalidraw drawings directly into the matching LeetCode problem folder:

```text
0001-two-sum/1.excalidraw
0001-two-sum/0001.excalidraw
0001-two-sum/two-sum.excalidraw.png
```

The Codex local automation checks this repo hourly. When it sees changed drawing
files inside problem folders, it commits and pushes them with:

```text
Sync Excalidraw notes
```

Supported file endings are `.excalidraw`, `.excalidraw.png`,
`.excalidraw.svg`, `.png`, and `.svg`.

## Inbox Flow

If you prefer exporting into one staging folder first, save or export Excalidraw
files into `excalidraw-inbox/`, then run:

```sh
python3 scripts/sync_excalidraw.py
```

The script copies each supported drawing into the matching LeetCode solution
folder. Match files by problem number or slug:

```text
excalidraw-inbox/1.excalidraw
excalidraw-inbox/0001.excalidraw
excalidraw-inbox/0001-two-sum.excalidraw
excalidraw-inbox/1-two-sum.excalidraw.png
excalidraw-inbox/two-sum.svg
```

Those examples copy into:

```text
0001-two-sum/
```

The simplest convention is to title/export each drawing with only the LeetCode
problem number. Both `1.excalidraw` and `0001.excalidraw` match
`0001-two-sum/`.

Supported file endings are `.excalidraw`, `.excalidraw.png`,
`.excalidraw.svg`, `.png`, and `.svg`.

By default the original file name is preserved in the problem folder. Use
`--dest-name diagram.excalidraw` if you want every raw Excalidraw file to land
with the same name.

The GitHub Actions workflow also runs this script before syncing LeetCode. That
is useful only for drawing files that already exist in the workflow checkout.
For normal local Excalidraw exports, run the script locally first, then commit
the copied files in the problem folders.

## Local Auto-Push

The auto-push script only stages drawing files that are already inside LeetCode
problem folders. It leaves solution code and unrelated local changes alone.

Run it once manually with:

```sh
python3 scripts/auto_push_excalidraw.py
```

The active Codex automation is named `Auto-push LeetCode Excalidraw notes`.
