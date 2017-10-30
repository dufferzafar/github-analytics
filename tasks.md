
## Developer Countries

Map; Number of new users per country; per Year

* users.csv

## Active User Acquisition Rate

Month of Year vs Number of (active) Users

(frequency vs cumulative)

* users.csv

For active calculation, any unique activity in

* commits.csv; issues.csv; comments.csv; 

## Lifespan of a project

Average lifespan vs Language (histogram)

`lifespan = max(activity_time) - min(activity_time)`

Output: 

(after reduce)
```json
    {
        "language": "{average lifespan (days?)}"
    }
```

(after map)
```json
    projects = [
        {
            "owner":
            "name":
            "language": 
            lifespan: [
                "commits":
                "issues":
                "pull_request":
            ]
        }
    ]
```

* commits.csv
* issues.csv
* pull_requests.csv
* project.csv

## Correlation between time of day and activities?

Group the timestamp into Yearx24x7 matrix?

created_at column:

* commits.csv
* issues.csv
* pull_requests.csv

* commit_comments.csv
* issue_comments.csv
* pull_request_comments.csv

---

Top 1000 Repositories by commits will require the use of 90GB file: **project_commits.csv**

```sql
SELECT pid, COUNT (*)
GROUP BY project_id
```

---

## Tasks

* Is the data clean?

* Mapping of analyses and files (columns)

* Which files do we really need?

* Data Put
