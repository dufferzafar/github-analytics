
# github-analytics

Analysis of GitHub data (GHTorrent) using Hadoop & Spark

## Code

We used Jupyter Lab notebooks to run Spark queries.

The code ran on cluster is in file: `src/cluster-queries.ipynb`, while testing code that we ran on our machines is in `src/testing.ipynb`.

## Other directories

* `charts/`
    - Contains the code used to generate charts
    - We used `d3.js` for maps and `Bokeh` for other charts

* `cluster-setup/`
    - Contains hadoop & spark config along with the commands we ran on each machine
    - There is also a `Makefile` that has commands to control the cluster
        + Starting / Stopping Hadoop etc.

* `initial-document/` , `final-document`
    - The .tex for the project reports

* `outputs/`
    - The output of queries
        + Is in a bunch of formats: CSV, JSON, Markdown Tables etc.
