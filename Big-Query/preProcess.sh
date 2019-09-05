#!/bin/bash
for ano in `seq -w $1 $1`; do
for month in `seq -w 1 12`; do
    unrar x defesa_fiscal_${ano}${month}.rar
    iconv -f "windows-1252" -t "UTF-8" fileName_${ano}${month}.csv -o utf8_$ano$month.csv
    echo utf8_$ano$month.csv
    sed 's/,/./g' utf8_$ano$month.csv | sed '1s/ /_/g' > tmp
    mv tmp utf8_$ano$month.csv
done
done
