
# xsv - a fast csv parser written in rust
# https://github.com/BurntSushi/xsv/

# Remove Column 2 (sha)
xsv select '!2' -o commits_new.csv -- commits.csv

# Is this faster?
# xsv select '!2' -- commits.csv > commits_new.csv

# Remove Column 4 (ext_ref_id)
xsv select '!4' -o project_membders_new.csv -- project_members.csv

# Remove 'https://api.github.com/repos/' from projects.csv
# 15% reduction
# xsv select '!4' -- projects.csv | sed 's,https://api.github.com/repos/,,' > projects.csv
sed 's,https://api.github.com/repos/,,' projects.csv | csvcut -H -p "\\" -q '"' -C 4 >
