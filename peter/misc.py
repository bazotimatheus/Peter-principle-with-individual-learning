from random import gauss, uniform

def generate_age(mean, std):
  valid_age = False
  age = None

  while not valid_age:
    age = int(gauss(mean, std))
    valid_age = 18 <= age < 60

  return age

def age_employees(dataset):
  dataset['age'] += 1
  return dataset

def reset_idx(dataset):
  indexes = []
  for i in range(0, dataset.shape[0] + 1):
    indexes.append(i)
  dataset.reset_index(names=indexes, inplace=True)
  dataset = dataset.drop(0, axis=1)
  return dataset

def generate_learning_coefficient():
  return uniform(0, 0.03)
