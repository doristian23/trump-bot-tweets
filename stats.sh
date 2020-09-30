#!/bin/bash

echo `wc -l < $1`
fline=`head -n 1 $1`
echo $fline
last10kpotus=`tail -n 10000 $1 | grep -c 'potus'`
echo $last10kpotus
fake=`sed -n '100,200p;201q' $1 | grep -c 'fake'`
echo $fake

