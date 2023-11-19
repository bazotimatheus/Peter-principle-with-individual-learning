LEVELS = 6
COMPETENCES = 24

MAX_EMPLOYEES = [1, 5, 11, 21, 41, 81]
RESPONSIBILITY = [1.0, 0.9, 0.8, 0.6, 0.4, 0.2]

MIN_COMPETENCE = 4.0
MAX_AGE = 65

MAX_EXECUTIONS = 5
MAX_ITERATIONS = 100

# Valid strategies: 'best', 'worst', 'random'
STRATEGY = 'random'

# The correlation parameter is a number between 0 and 1
# The original work uses 0.2 and 0.8
CORRELATION = 0.8

DATA_DIR = './data/'+STRATEGY+'-skills_'+str(COMPETENCES)+'-correlation_'+str(CORRELATION)
