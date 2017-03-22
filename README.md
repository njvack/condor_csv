# condor_csv: Make HTCondor submit files from CSV

Creating the submit files for HTCondor can be annoying. The [syntax is rather byzantine](http://research.cs.wisc.edu/htcondor/manual/current/condor_submit.html) and it's not so easy to find the lines you want to copy and change to add another job to your queue.

But! Scheduling jobs from a CSV file? That's easier. One row per job, one column per job parameter — that makes sense. And that's what this package provides.

## The file format

The input is a standard CSV file, as written by Excel. Here are the rules:

* Every row in the file (except the header) will be one job and generate one 'Queue' line in your submit file.
* Every column in the file is a value that'll go in your submit file.
* If a column has only one value, that value will go at the top of the file
* Otherwise, the value will appear in every block, before the 'Queue' line.
* Columns are written in the order they appear in the file
* Header columns that begin with # indicate comments, and will appear exactly where regular columns would go
* The only specially-handled column is one called "#skip". If this column appears, rows where that is any value other than blank, "0", "false", or "n" (case insensitive) will not be added to the submit file.

That's it.

More documentation (including a command line reference and example) coming soon.
