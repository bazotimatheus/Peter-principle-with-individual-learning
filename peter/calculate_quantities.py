from peter.config import *
import numpy as np

def calculate_competence_agent(dataset, qualifications):
  level = dataset['level'].values
  skills = dataset[['skill_'+str(i) for i in range(COMPETENCES)]].values
  competence = np.array([np.sum(skills[i] * qualifications[n - 1]) for i, n in enumerate(level)])
  dataset['competence'] = competence
  return dataset
  
def calculate_competence_new_agent(skills_vector, qualifications, level):
  competence = np.sum(skills_vector * qualifications[level - 1])
  return competence

def calculate_max_competence(qualifications):
  max_competence = np.sum(qualifications, axis=1)
  return max_competence 

def calculate_normalized_competence(dataset, max_competence):
  dataset['normalized_competence'] = dataset['competence'] / [max_competence[level - 1] for level in dataset['level']]
  return dataset

def calculate_efficiency_agent(dataset, qualification_versor):
  for idx in range(0, dataset.shape[0]):
    level = dataset['level'].iloc[idx]
    skills = np.array([dataset['skill_' + str(i)].iloc[idx] for i in range(COMPETENCES)])
    efficiency = np.sum(RESPONSIBILITY[level - 1] * skills * qualification_versor[level - 1])
    dataset['efficiency'].iloc[idx] = efficiency
  return dataset

def calculate_efficiency_new_agent(skills_vector, qualification_versor, level):
    skills_vector = np.array(skills_vector)
    qualification_versor = np.array(qualification_versor[level - 1])
    
    efficiency = np.sum(RESPONSIBILITY[level - 1] * skills_vector * qualification_versor)
    return efficiency

def calculate_global_efficiency(dataset, qualification_versor):
  max_number_employers = np.array(MAX_EMPLOYEES)
  responsibilities = np.array(RESPONSIBILITY)
  
  max_global_efficiency = np.sum(max_number_employers * responsibilities * np.sum(qualification_versor, axis=1))
  efficiency_sums = np.sum(dataset['efficiency'])
  global_efficiency = efficiency_sums / max_global_efficiency
  return global_efficiency

def calculate_competences(dataset, f_first, f_second, f_third, f_fourth, f_fifth, f_sixth):
  for idx in range(0, dataset.shape[0]):
    level = dataset['level'].iloc[idx]
    competence = round(dataset['normalized_competence'].iloc[idx], 2)
    
    if level == 1:
      f_first.write(f"{competence}\n")
    elif level == 2:
      f_second.write(f"{competence}\n")
    elif level == 3:
      f_third.write(f"{competence}\n")
    elif level == 4:
      f_fourth.write(f"{competence}\n")
    elif level == 5:
      f_fifth.write(f"{competence}\n")
    else:
      f_sixth.write(f"{competence}\n")
      
def calculate_competences(dataset, output_files):
  for level, group in dataset.groupby('level'):
    competences = group['normalized_competence'].round(2)
    output_file = output_files[level - 1]
    competences.to_csv(output_file, index=False, header=False, mode='a')
