#!/bin/zsh
# 重新產生兩校網頁並部署到 Cloudflare Pages（https://esl-school.pages.dev）
set -e
cd "$(dirname "$0")"
python3 build.py
D=$(mktemp -d)
cp -R index.html jiangong shekou "$D"/
npx -y wrangler@4 pages deploy "$D" --project-name esl-school --branch main --commit-dirty=true
rm -rf "$D"
