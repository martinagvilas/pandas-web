#!/bin/bash
wget --no-check-certificate https://raw.githubusercontent.com/pandas-dev/pandas/master/.github/CODE_OF_CONDUCT.md -O source/community/coc.md

wget https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/source/development/roadmap.rst --no-check-certificate
pandoc -s -o roadmap.md roadmap.rst
printf "# Roadmap\n\n$(tail -n +5 roadmap.md | sed ':again;$!N;$!b again; s/{[^}]*}//g')" > source/community/roadmap.md
rm roadmap.rst roadmap.md

wget https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/source/ecosystem.rst --no-check-certificate
pandoc -s -o ecosystem.md ecosystem.rst
tail -n +5 ecosystem.md | sed ':again;$!N;$!b again; s/{[^}]*}//g' > source/community/ecosystem.md
rm ecosystem.rst ecosystem.md
