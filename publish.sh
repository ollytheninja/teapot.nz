#!/bin/bash
rm -rf output

pelican
ghp-import output -b gh-pages
git push origin gh-pages
