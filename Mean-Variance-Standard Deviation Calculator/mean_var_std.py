import numpy as np
def calculate(list):
  if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

  flat=np.array(list)
  mat=flat.reshape(3,3)
  calculations={
  'mean': [mat.mean(axis=0).tolist(), mat.mean(axis=1).tolist(), flat.mean().tolist()],
  'variance': [mat.var(axis=0).tolist(), mat.var(axis=1).tolist(), flat.var().tolist()],
  'standard deviation': [mat.std(axis=0).tolist(), mat.std(axis=1).tolist(), flat.std().tolist()],
  'max': [mat.max(axis=0).tolist(), mat.max(axis=1).tolist(), flat.max().tolist()],
  'min': [mat.min(axis=0).tolist(), mat.min(axis=1).tolist(), flat.min().tolist()],
  'sum': [mat.sum(axis=0).tolist(), mat.sum(axis=1).tolist(), flat.sum().tolist()]
  }

  return calculations

