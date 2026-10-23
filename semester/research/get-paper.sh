#!/bin/sh
# Downloads the open-access reading for vignette 3 next to this script.
# Eloundou, Manning, Mishkin and Rock, "GPTs are GPTs: An Early Look at the Labor
# Market Impact Potential of Large Language Models", arXiv:2303.10130.
# Kept out of git; run this once before the session.
cd "$(dirname "$0")" && curl -sL -o eloundou-2023-gpts-are-gpts.pdf https://arxiv.org/pdf/2303.10130 && ls -la eloundou-2023-gpts-are-gpts.pdf
