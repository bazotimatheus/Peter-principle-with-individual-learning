#!/bin/bash

variables_py="config.py"
exec_py="main.py"

competences=(6 24)
strategies=(best worst random)
correlation_parameters=(0.2 0.8)

# Loop para iterar sobre os valuees das variáveis
for strategy in "${strategies[@]}"; do
  for competence in "${competences[@]}"; do
    for correlation_parameter in "${correlation_parameters[@]}"; do
      cd peter
      
      sed -i "s/STRATEGY = .*/STRATEGY = '$strategy'/" $variables_py
      sed -i "s/COMPETENCES = .*/COMPETENCES = $competence/" $variables_py
      sed -i "s/CORRELATION = .*/CORRELATION = $correlation_parameter/" $variables_py

      cd ..

      python3 main.py
    done
  done
done
