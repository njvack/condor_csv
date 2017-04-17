# condor_csv: Make HTCondor submit files from CSV files

Creating the submit files for HTCondor can be annoying. The [syntax is rather byzantine](http://research.cs.wisc.edu/htcondor/manual/current/condor_submit.html) and it's not so easy to find the lines you want to copy and change to add another job (or fifty) to your queue.

But! Scheduling jobs from a CSV file? That's an easier nut to crack. One row per job, one column per job parameter — that makes sense. And that's what this package provides.

## The file format

The input is a standard CSV file, as written by Excel. Here are the rules:

* Every row in the file (except the header) will be one job and generate one 'Queue' line in your submit file.
* Every column in the file is a value that'll go in your submit file.
* If a column has only one value, that value will go at the top of the file.
* Otherwise, the value will appear in every block, before the 'Queue' line.
* Columns are written in the order they appear in the file.
* Header columns that begin with # indicate comments, and will appear exactly where regular columns would go.
* The only specially-handled column is one called "#skip". If this column appears, rows where that is any value other than blank, "0", "false", or "n" (case insensitive) will be commented out when added to the submit file.

This ships with one command-line script, `csv_to_submit`

## `csv_to_submit`

```Create a HTCondor submit file from a CSV file.

Input is a file formatted as by Excel's CSV writing. We take this and, for
every row, write a job entry for an HTCondor submit file. Command names are
expected in the header row.

Columns with values that are the same in every row (often for universe,
executable, and getenv commands) will be written at the top before any per-job
clauses. This is only for human readability -- the submit file would work the
same either way.

The only specially-handled case is a column labeled "#skip". If this column
exists, anywhere it has a value other than blank, "0", "f, false", or "n"
the corresponding job clause will be commented out.

Documentation for submit file commands is available here:
http://research.cs.wisc.edu/htcondor/manual/current/condor_submit.html

Usage:
  condor_csv [options] <input_file>
  condor_csv -h

Options:
  -h                      Show this screen
  --version               Show version
  --output=<output_file>  Write to this file instead of standard output
  -v, --verbose           Print debugging information to standard error
```

## Example

The following CSV file:

<table>
<tr><th>Universe</th><th>Executable</th><th>#Subject</th><th>Arguments</th><th>Log</th><th>Output</th><th>Error</th><th>#Skip</th></tr>
<tr><td>vanilla</td><td>/usr/bin/ls</td><td>1</td><td>/tmp/1*</td><td>/tmp/1.log</td><td>/tmp/1.out</td><td>/tmp/1.err</td><td></td></tr>
<tr><td>vanilla</td><td>/usr/bin/ls</td><td>2</td><td>/tmp/2*</td><td>/tmp/2.log</td><td>/tmp/2.out</td><td>/tmp/2.err</td><td></td></tr>
<tr><td>vanilla</td><td>/usr/bin/ls</td><td>3p</td><td>/tmp/3p*</td><td>/tmp/3p.log</td><td>/tmp/3p.out</td><td>/tmp/3p.err</td><td>1</td></tr>
</table>

Will turn into:

```
Universe = vanilla
Executable = /usr/bin/ls

#Subject = 1
Arguments = /tmp/1*
Log = /tmp/1.log
Output = /tmp/1.out
Error = /tmp/1.err
Queue

#Subject = 2
Arguments = /tmp/2*
Log = /tmp/2.log
Output = /tmp/2.out
Error = /tmp/2.err
Queue

# #Subject = 3p
# Arguments = /tmp/3p*
# Log = /tmp/3p.log
# Output = /tmp/3p.out
# Error = /tmp/3p.err
# Queue

```


## Credits

Scorify packages the truly excellent [docopt](https://github.com/docopt/docopt) library.

docopt is copyright (c) 2013 Vladimir Keleshev, vladimir@keleshev.com
