# Excalidraw Notes

## Manual Flow

Drop Excalidraw drawings directly into the matching LeetCode problem folder:

```text
0001-two-sum/1.excalidraw
0001-two-sum/0001.excalidraw
0001-two-sum/two-sum.excalidraw.png
```

Supported file endings are `.excalidraw`, `.excalidraw.png`,
`.excalidraw.svg`, `.png`, and `.svg`.

Raw `.excalidraw` files are editable JSON files, so GitHub displays them as
code. The manual scripts generate a `.excalidraw.png` preview beside each raw
file so GitHub can display the drawing.

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

There is no active Excalidraw automation. Run the scripts manually when you want
to sync and push drawings:

```sh
python3 scripts/sync_excalidraw.py --allow-unmatched
python3 scripts/auto_push_excalidraw.py
```

That second command also renders missing or outdated PNG previews for raw
`.excalidraw` files already inside problem folders.

The auto-push script only stages drawing files that are already inside LeetCode
problem folders. It leaves solution code and unrelated local changes alone.
