import numpy as np
from random import randint, gauss
from numpy.linalg import norm

from peter.config import *

def generate_qualification_vector_and_normalized(correlation):
  nu = randint(0, 10) / 10.0

  w, h = COMPETENCES, LEVELS
  Q = np.zeros((h, w), dtype=float)
  normalized_Q = np.zeros((h, w), dtype=float)

  Q[h - 1] = np.random.rand(w)

  for i in range(h - 2, -1, -1):
    Q[i] = Q[i + 1] * correlation + nu * (1 - correlation)

  norm = np.linalg.norm(Q)

  for i in range(h - 2, -1, -1):
    normalized_Q[i] = Q[i] / norm

  return Q, normalized_Q

def generate_skill_vector(mean, std):
  valores = np.random.normal(mean, std, COMPETENCES)
  valores = np.clip(valores, 0, 1)
  return valores.tolist()

def update_skill_vector(dataset, qualifications):
  for skill in range(0, COMPETENCES):
    levels = dataset['level'].values - 1
    skills = dataset['skill_' + str(skill)].values
    learning_coefficients = dataset['learning_coefficient'].values
    
    new_skills = []
    
    for level, current_skill, learning_coefficient in zip(levels, skills, learning_coefficients):
      new_skill = current_skill + learning_coefficient * qualifications[level, skill]
      new_skill = min(new_skill, 1.0)
      new_skills.append(new_skill)

    dataset['skill_' + str(skill)] = new_skills

  return dataset
