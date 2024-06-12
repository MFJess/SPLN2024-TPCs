# Name

 jjcli - python module for command-line filter

# Synopsis

as ascript:

    jjcli skel     ## a initial filter skeleton
    jjcli          ## manual

as a module: 

    from jjcli import *       ## re.* functions also imported
    cl=clfilter(opt="do:", doc=__doc__) 
                              ## options in cl.opt  (...if "-d" in cl.opt:)
                              ##    autostrip         (def=True)
                              ##    inplace           (def=False) 
                              ##    fs (for csvrow()) (def=",")
                              ##    doc=__doc__     (for --help)
                              ##    longopts=["op1",...]

    for line in cl.input():...    ## process one rstriped line at the time
    for txt in cl.text():...      ## process one striped text at the time
        ## process txt            ##   (end of line spaces and \\r also removed)
    for par in cl.paragraph():... ## process one striped paragraph at the time
    for tup in cl.csvrow():...    ## process one csv row at the time
    for tup in cl.tsvrow():...    ## process one tsv row at the time

    cl.lineno()         ## line number
    cl.filelineno()
    cl.parno()          ## paragraph number
    cl.fileparno()
    cl.filename()       ## filename or "<stdin>"
    cl.nextfile()
    cl.isfirstline()
    cl.args  cl.opt     ## command line arguments and options (after clfilter())

# Description

__jjcli__ is a opinioned Python module that tries to simplify the creation of
__unix__ filters. It is based on:

- getopt  (for command line options and args)
- fileinput (for [files/stdin] arguments)
- re (regular expressions should be native)
- glob (glob.glob should be native)
- csv  (for csv and tsv inputs)
- urllib.request (to deal with input argumens that are url)
- subprocess 

## Regular expressions

We want to have all re.* functions available (as if they were native
functions).

In order to enable __re__ flags, use: re.I re.X re.S  

## Subprocesses   (qx, qxlines, qxsystem)

    a=qx( "ls" )
    for x in qxlines("find | grep '\.jpg$'"): 
      ...
    qxsystem("vim myfile")

### Execute command return its stdout
    qx(*x)      →  returns    subprocess.getoutput(x)

### Execute command return its stdout lines
    qxlines(*x) →  returns    subprocess.getoutput(x).splitlines()

### Execute command -- system
    qxsystem(*x) →  calls     subprocess.call(x,shell=True)

## STDERR - warn, die

    warn(*args)  → print to stderr
    die(*args)   → warn and exit 1

## Other functions

    slurpurlutf8(self,f)

    filename    = lambda s : F.filename()      # inherited from fileinput
    lineno      = lambda s : F.lineno()
    filelineno  = lambda s : F.filelineno()
    parno       = lambda s : s.parno_          # paragraph number
    fileparno   = lambda s : s.fileparno_
    nextfile    = lambda s : F.nextfile()
    isfirstline = lambda s : F.isfirstline()
    isfirstpar  = lambda s : s.fileparno == 1
    close       = lambda s : F.close()
