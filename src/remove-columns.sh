
# xsv - a fast csv parser written in rust
# https://github.com/BurntSushi/xsv/

# Remove Column 2 (sha)
xsv select '!2' -o commits_new.csv -- commits.csv

# Remove Column 4 (created_at)
xsv select '!4' -o project_languages_new.csv -- project_languages.csv

# Remove Column 4 (ext_ref_id)
xsv select '!4' -o project_membders_new.csv -- project_members.csv
