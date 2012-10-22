#!/bin/bash


current=`ls | egrep 'problem_[0-9]{3}' | cut -d "_" -f 2 | cut -d "." -f 1 | sort | tail -n 1`

next=`echo $current + 1 | bc`
newnext=`printf '%03s\n' $next`



echo creating problem_$newnext.py...
cp problem_template.py problem_$newnext.py
sed -i s/NUMBER/$newnext/ problem_$newnext.py
