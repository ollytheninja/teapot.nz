#!/bin/bash
rm -rf output

pelican
cp CNAME output
ghp-import output -b gh-pages
git push origin gh-pages
