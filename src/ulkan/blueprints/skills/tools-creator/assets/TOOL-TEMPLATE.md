---
name: {tool-name}
type: {script | mcp | util}
description: {Short description}
---

## Checklist

- [ ] **Script**: 
    - [ ] `#!/bin/bash` header
    - [ ] `set -e` for safety
    - [ ] Helpful usage/help text (`-h`)
    - [ ] `chmod +x` applied

- [ ] **MCP**:
    - [ ] `import mcp` (or relevant lib)
    - [ ] Defined tools/resources
    - [ ] STDIO communication
    - [ ] Config for checking/restarting

- [ ] **Util**:
    - [ ] Clean function signatures
    - [ ] Type hints
    - [ ] Docstrings

## Snippets

### Bash Script Start

```bash
#!/bin/bash
set -e

# {Description}

function show_help {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -h, --help    Show this help message"
}

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    show_help
    exit 0
fi

# Main logic here
```

### Python Utility Start

```python
#!/usr/bin/env python3
"""
{Description of the utility}
"""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="{Description}")
    # Add arguments
    args = parser.parse_args()

    # Logic
    print("Running utility...")

if __name__ == "__main__":
    main()
```
