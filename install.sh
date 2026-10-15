#!/usr/bin/env bash
# install.sh - Install the Odoo agent skills for Claude Code, Antigravity and/or Codex.
# Usage: ./install.sh [--agent claude|antigravity|codex|all] [--scope project|user] [--target DIR] [--copy]
# Missing options are asked interactively.
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)"
AGENT=""; SCOPE=""; TARGET=""; MODE="link"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --agent) AGENT="$2"; shift 2;;
    --scope) SCOPE="$2"; shift 2;;
    --target) TARGET="$2"; shift 2;;
    --copy) MODE="copy"; shift;;
    -h|--help) sed -n '2,4p' "$0"; exit 0;;
    *) echo "Unknown option $1"; exit 1;;
  esac
done

if [[ -z "$AGENT" ]]; then
  echo "Which agent(s)?  1) Claude Code  2) Antigravity  3) Codex  4) All"
  read -rp "> " a; case "$a" in 1) AGENT=claude;; 2) AGENT=antigravity;; 3) AGENT=codex;; *) AGENT=all;; esac
fi
if [[ -z "$SCOPE" ]]; then
  echo "Install scope?  1) Project (inside a client/project folder)  2) User (global, all projects)"
  read -rp "> " s; [[ "$s" == "2" ]] && SCOPE=user || SCOPE=project
fi
if [[ "$SCOPE" == "project" && -z "$TARGET" ]]; then
  read -rp "Project folder [$(pwd)]: " TARGET; TARGET="${TARGET:-$(pwd)}"
fi

dest_for() {  # $1 agent
  if [[ "$SCOPE" == "user" ]]; then
    case "$1" in
      claude) echo "$HOME/.claude/skills";;
      antigravity) echo "$HOME/.gemini/antigravity/skills";;
      codex) echo "${CODEX_HOME:-$HOME/.codex}/skills";;
    esac
  else
    case "$1" in
      claude) echo "$TARGET/.claude/skills";;
      antigravity) echo "$TARGET/.agent/skills";;
      codex) echo "$TARGET/.agents/skills";;
    esac
  fi
}

install_one() {
  local d; d="$(dest_for "$1")"; mkdir -p "$d"
  for skill in "$SRC"/skills/*/; do
    local name; name="$(basename "$skill")"
    rm -rf "${d:?}/$name"
    if [[ "$MODE" == "copy" ]]; then cp -r "$skill" "$d/$name"; else ln -s "${skill%/}" "$d/$name"; fi
  done
  echo "✔ $1 → $d ($MODE)"
}

agents=("$AGENT"); [[ "$AGENT" == "all" ]] && agents=(claude antigravity codex)
for a in "${agents[@]}"; do install_one "$a"; done

if [[ "$SCOPE" == "project" ]]; then
  [[ -f "$TARGET/AGENTS.md" ]] || cp "$SRC/AGENTS.md" "$TARGET/AGENTS.md"
  [[ -f "$TARGET/CLAUDE.md" ]] || cp "$SRC/CLAUDE.md" "$TARGET/CLAUDE.md"
  [[ -f "$TARGET/GEMINI.md" ]] || cp "$SRC/GEMINI.md" "$TARGET/GEMINI.md"
  [[ -f "$TARGET/.env.example" ]] || cp "$SRC/.env.example" "$TARGET/.env.example"
  echo "✔ Instruction files and .env.example copied to $TARGET (existing files kept)"
fi
echo "Done. Copy .env.example to .env and fill in the Odoo credentials (never commit .env)."
