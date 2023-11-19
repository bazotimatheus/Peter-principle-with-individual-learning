import pandas as pd

from peter.config import *
from peter.calculate_quantities import *
from peter.generate_vectors import *
from peter.misc import *

def hire_first_employees(dataset, qualifications, normalized_qualifications, max_competence):
  for current_level in range(1, 7):
    number_employees_current_level = dataset.query('level == @current_level').shape[0]
    employees_to_hire = MAX_EMPLOYEES[current_level - 1] - number_employees_current_level
    
    if employees_to_hire > 0:
      new_employees = []
      for _ in range(employees_to_hire):
        data = {
            'level': current_level,
            'age': randint(20, 50),
        }
        
        skill_vector = generate_skill_vector(0.7, 0.2)
        
        data.update({'skill_' + str(skill): valor for skill, valor in enumerate(skill_vector)})
        data['competence'] = calculate_competence_new_agent(skill_vector, qualifications, current_level)
        data['efficiency'] = calculate_efficiency_new_agent(skill_vector, normalized_qualifications, current_level)
        data['learning_coefficient'] = generate_learning_coefficient()
        new_employees.append(data)
      
      new_employees_df = pd.DataFrame(new_employees)
      dataset = pd.concat([dataset, new_employees_df])
  
  dataset = reset_idx(dataset)
  dataset = calculate_normalized_competence(dataset, max_competence)

  return dataset

def hire_employees(dataset, qualifications, normalized_qualifications, max_competence):
  for current_level in range(1, 7):
    number_employees_current_level = dataset.query('level == @current_level').shape[0]
    employees_to_hire = MAX_EMPLOYEES[current_level - 1] - number_employees_current_level
    
    if employees_to_hire > 0:
      new_employees = []
      for _ in range(employees_to_hire):
        data = {
            'level': current_level,
            'age': generate_age(25, 5),
        }
        
        skill_vector = generate_skill_vector(0.7, 0.2)
        
        data.update({'skill_' + str(skill): valor for skill, valor in enumerate(skill_vector)})
        data['competence'] = calculate_competence_new_agent(skill_vector, qualifications, current_level)
        data['efficiency'] = calculate_efficiency_new_agent(skill_vector, normalized_qualifications, current_level)
        data['learning_coefficient'] = generate_learning_coefficient()
        new_employees.append(data)
      
      new_employees_df = pd.DataFrame(new_employees)
      dataset = pd.concat([dataset, new_employees_df])
  
  dataset = reset_idx(dataset)
  dataset = calculate_normalized_competence(dataset, max_competence)

  return dataset
