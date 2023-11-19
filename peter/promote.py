from peter.config import *
from peter.calculate_quantities import *
from peter.misc import reset_idx

def promote_employees(dataset, strategy, max_competence, qualifications):
  modified_dataset = dataset.copy()

  for current_level in range(2, 7):
    upper_level = current_level - 1
    current_level_df = modified_dataset[modified_dataset['level'] == current_level]
    upper_level_df = modified_dataset[modified_dataset['level'] == upper_level]

    current_level_size = current_level_df.shape[0]
    upper_level_size = upper_level_df.shape[0]

    while (upper_level_df.shape[0] < MAX_EMPLOYEES[upper_level - 1]) and (not current_level_df.empty):
      if strategy == 'best':
        selected_row = current_level_df.loc[current_level_df['normalized_competence'] == current_level_df['normalized_competence'].max()].head(1)
      elif strategy == 'worst':
        selected_row = current_level_df.loc[current_level_df['normalized_competence'] == current_level_df['normalized_competence'].min()].head(1)
      elif strategy == 'random':
        selected_row = current_level_df.sample(n=1)

      selected_index = selected_row.index[0]

      modified_dataset['level'].iloc[selected_index] = upper_level

      current_level_df = modified_dataset.loc[modified_dataset['level'] == current_level]
      upper_level_df = modified_dataset.loc[modified_dataset['level'] == upper_level]
    # fim do while

    modified_dataset = calculate_competence_agent(modified_dataset, qualifications)
    modified_dataset = calculate_normalized_competence(modified_dataset, max_competence)
    modified_dataset.sort_values(['level'], inplace=True)
    modified_dataset = reset_idx(modified_dataset)
  # fim do for

  dataset = modified_dataset.copy()

  return(dataset)