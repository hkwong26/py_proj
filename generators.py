""" Generator applications - why use this compated to list comprehesions """

def gen_def():
  num = [1,2,3,4]
  for i in nums:
    yield (i*i)
    
    
num_gen = gen_def()

print next(num_gen)
