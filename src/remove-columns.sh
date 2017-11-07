
# xsv - a fast csv parser written in rust
# https://github.com/BurntSushi/xsv/

# Remove Column 2 (sha)
pv commits.csv | xsv select -n '!2' -o commits_new.csv

# Because the data is simpler, we can use cut - which will be fast?
# Actually, NO! xsv turned out to be way faster than even cut
# pv commits.csv | cut -d, --complement -f 2 > commits_new.csv
# pv commits.csv | sed "s/,[\"a-z0-9]*//" > commits_new.csv

# Remove Column 4 (ext_ref_id)
xsv select -n '!4' -o project_membders_new.csv -- project_members.csv

# Remove Column 5 (pull_request)
pv issues.csv | xsv select -n '!5' -o issues_new.csv

# projects.csv
# Remove 'https://api.github.com/repos/' from url, converting it to a slug
# Reduced size from 11 GB to 4.5 GB
pv projects.csv | sed 's,https://api.github.com/repos/,,' | xsv select -n '!4,5,10,11' > projects_new.csv
