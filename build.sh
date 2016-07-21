#!/usr/bin/env bash

# Generate darcula base 
pygmentize -f html -S darcula -a .highlight > darcula_base.css
# Generate darcula for properties
pygmentize -f html -S darcula_properties -a .highlight.properties > darcula_properties.css
# Remove prefixes on temp files for compute diff
sed 's/\.highlight\s*//g' darcula_base.css > darcula_base.css.tmp
sed 's/\.highlight\.[a-zA-Z0-9]* *//g' darcula_properties.css > darcula_properties.css.tmp
# Find commons
grep -F -f darcula_base.css.tmp darcula_properties.css.tmp > commons.css.tmp
# Remove commons
grep -vwF -f commons.css.tmp darcula_properties.css > darcula_properties.css.reduce
# Merge
cat <(echo -e "/* ----[ BASE ]---- */\n") darcula_base.css \
<(echo -e "\n/* ----[ PROPERTIES ]---- */\n") darcula_properties.css.reduce \
> darcula.css
# Delete tmp files
rm -f darcula_base.css*
rm -f darcula_properties.css*
rm -f commons.css.tmp