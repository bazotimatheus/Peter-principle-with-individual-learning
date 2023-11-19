from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

from peter import *

# Loop com diferentes 
# for output in tqdm(range(MAX_EXECUTIONS),desc='Progress', unit='execution'):
for output in range(MAX_EXECUTIONS):
  efficiency_path = DATA_DIR+'/efficiency/output_'+str(output)+'.csv'
  efficiency_file = open(efficiency_path, 'w')

  # path_first = DATA_DIR+'/competence/first_'+str(output)+'.csv'
  # path_second = DATA_DIR+'/competence/second_'+str(output)+'.csv'
  # path_third = DATA_DIR+'/competence/third_'+str(output)+'.csv'
  # path_fourth = DATA_DIR+'/competence/fourth_'+str(output)+'.csv'
  # path_fifth = DATA_DIR+'/competence/fifth_'+str(output)+'.csv'
  # path_sixth = DATA_DIR+'/competence/sixth_'+str(output)+'.csv'
  # file_first =  open(path_first, 'w')
  # file_second = open(path_second, 'w')
  # file_third =  open(path_third, 'w')
  # file_fourth = open(path_fourth, 'w')
  # file_fifth =  open(path_fifth, 'w')
  # file_sixth =  open(path_sixth, 'w')

  # list_competences = [file_first, file_second, file_third, file_fourth, file_fifth, file_sixth]

  qualifications, qualifications_versor = generate_qualification_vector_and_normalized(CORRELATION)
  max_competence = calculate_max_competence(qualifications)

  nomes_colunas = ['level', 'age', 'competence', 'normalized_competence', 'efficiency', 'learning_coefficient'] + ['skill_'+str(x) for x in range(COMPETENCES)]
  dataset = pd.DataFrame(columns = nomes_colunas)
  dataset = hire_first_employees(dataset, qualifications, qualifications_versor, max_competence)

  for iteration in tqdm(range(MAX_ITERATIONS), desc='Progress', unit='iterations'):
  # for iteration in range(MAX_ITERATIONS):
    global_efficiency = calculate_global_efficiency(dataset, qualifications_versor)
    efficiency_file.write(f'{iteration};{global_efficiency}\n')

    # calculate_competences(dataset, list_competences)

    dataset = dismiss_employees(dataset)
    dataset = promote_employees(dataset, STRATEGY, max_competence, qualifications)
    dataset = age_employees(dataset)
    dataset = update_skill_vector(dataset, qualifications)
    dataset = calculate_competence_agent(dataset, qualifications)
    dataset = calculate_normalized_competence(dataset, max_competence)
    dataset = calculate_efficiency_agent(dataset, qualifications_versor)
    dataset = hire_employees(dataset, qualifications, qualifications_versor, max_competence)

  # file_first.close()
  # file_second.close()
  # file_third.close()
  # file_fourth.close()
  # file_fifth.close()
  # file_sixth.close()

  efficiency_file.close()