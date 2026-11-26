"""Rewrites the list of operations in profile/README.md from the live catalog (https://api.lobstr.io/v2/catalog),
between the markers <!-- catalog:start --> and <!-- catalog:end -->. Run daily by .github/workflows/catalog.yml."""
import json
import pathlib
import re
import urllib.request

README = pathlib.Path(__file__).resolve().parents[1] / "profile" / "README.md"
CATALOG = "https://api.lobstr.io/v2/catalog"


def table(operations):
    """Every operation by its id, a source after another: the names say what they do."""
    by_source = {}
    for op in operations:
        by_source.setdefault(op["source"], []).append(op["id"])
    blocks = ["\n".join(sorted(ids)) for _, ids in sorted(by_source.items())]
    return "```text\n" + "\n\n".join(blocks) + "\n```"


def main():
    with urllib.request.urlopen(CATALOG, timeout=30) as answer:
        operations = json.load(answer)["data"]
    text = README.read_text()
    new = re.sub(r"(<!-- catalog:start -->).*?(<!-- catalog:end -->)",
                 lambda m: f"{m.group(1)}\n{table(operations)}\n{m.group(2)}", text, flags=re.S)
    if new != text:
        README.write_text(new)
    print(f"{len(operations)} operations")


if __name__ == "__main__":
    main()
