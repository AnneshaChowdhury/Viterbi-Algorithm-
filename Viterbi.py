# Filename: Viterbi.py

import sys 

Weather = ( 'H', 'C' )

StartProb = { 'H': 0.8, 'C': 0.2 }

TransProb = {
  'H' : { 'H': 0.7, 'C': 0.3 },
  'C' : { 'H': 0.4, 'C': 0.6 },
  }

EmitProb = {
  'H' : { '1': 0.2, '2': 0.4, '3': 0.4 },
  'C' : { '1': 0.5, '2': 0.4, '3': 0.1 }, 
  }

def Viterbi(observation, weather, startprob, transprob, emitprob):
  """
  :param observation:	The observation sequence 
  :param weather:	The hidden states 
  :param startprob:	The initial probability of all states  
  :param transprob:	The transition probability 
  :param emitprob: 	The hidden state to unhidden state probability
  :return:		The hidden state path for the observation sequence 
  """
  # V[day][state] = probability 
  V = [{}]
  path = {}
 
  # do initialization (day == 0)
  for w in weather:
    V[0][w] = startprob[w] * emitprob[w][observation[0]]
    path[w] = w
  
  # viterbi implementation 
  for day in range(1, len(observation)):
    V.append({})
    newpath = {}
 
    for w in weather:
      # prob = v[day - 1][y0] * trans[y0][w] * emit[w][obs]
      (prob, state) = max([(V[day - 1][y0] * transprob[y0][w] * emitprob[w][observation[day]], y0) for y0 in weather])
      # record the highest probability 
      V[day][w] = prob
      # record the path 
      newpath[w] = path[state] + w
    path = newpath
 
  (prob, state) = max([(V[len(observation) - 1][w], w) for w in weather])
  return path[state]

# main logic 
if len(sys.argv) == 2:
  Observation = sys.argv[1]
  Len = len(Observation)
  if Len > 10:
    print 'Input string too long'
  elif Len > 0:
    print Viterbi(Observation, Weather, StartProb, TransProb, EmitProb)

