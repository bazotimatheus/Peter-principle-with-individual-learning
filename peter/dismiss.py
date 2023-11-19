from peter.config import *
from peter.misc import reset_idx

def dismiss_employees(dataset):
  non_dismissed_employees = dataset.query('normalized_competence >= 0.4 and age <= 65').copy()
  non_dismissed_employees = reset_idx(non_dismissed_employees)
  return non_dismissed_employees
