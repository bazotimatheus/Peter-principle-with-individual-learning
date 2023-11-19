#!/bin/bash

MAX_ITERATIONS=$(awk -F'=' '/MAX_ITERATIONS/ {gsub(/[[:space:]]/, "", $2); print $2}' ../peter/config.py)
MAX_EXECUTIONS=$(awk -F'=' '/MAX_EXECUTIONS/ {gsub(/[[:space:]]/, "", $2); print $2}' ../peter/config.py)

competences=(6 24)
strategies=(best worst random)
correlation_parameters=(0.2 0.8)

# Loop para iterar sobre os valuees das variáveis
for strategy in "${strategies[@]}"; do
  for competence in "${competences[@]}"; do
    for correlation_parameter in "${correlation_parameters[@]}"; do
      dir=$strategy"-skills_"$competence"-correlation_"$correlation_parameter

      cd $dir

      output_file="mean_efficiency-"$strategy"-skills_"$competence"-correlation_"$correlation_parameter".csv"

      [ -e "$output_file" ] && rm "$output_file"

      for ((iteration=0; iteration<MAX_ITERATIONS; iteration++)); do
        sum=0
        count=0
        for ((i=0; i<MAX_EXECUTIONS; i++)); do
          file="efficiency/output_${i}.csv"

          if [ -e "$file" ]; then
            value=$(grep "^${iteration};" "$file" | cut -d ';' -f 2)

            if [ -n "$value" ]; then
              sum=$(awk "BEGIN {printf \"%f\", $sum + $value}")
              count=$((count + 1))
            fi
          fi
        done
        
        if [ "$count" -gt 0 ]; then
            mean=$(awk "BEGIN {printf \"%f\", $sum / $count}")
            echo "${iteration};${mean}" >> "$output_file"
        fi
      done

      cd ..
    done
  done
done
