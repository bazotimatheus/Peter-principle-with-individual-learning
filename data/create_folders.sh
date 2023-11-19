#!/bin/bash

competences=(6 24)
strategies=(best worst random)
correlation_parameters=(0.2 0.8)

for strategy in "${strategies[@]}"; do
  for competence in "${competences[@]}"; do
    for correlation_parameter in "${correlation_parameters[@]}"; do
      dir=$strategy"-skills_"$competence"-correlation_"$correlation_parameter

      mkdir $dir $dir/efficiency $dir/competence
    done
  done
done
