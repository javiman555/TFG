import time
import procedures.ValueResults as ValueResults
import random

random.seed(2)

start = time.time()

valueResults = ValueResults.ValueResults(debug=True)

valueResults.execute()


'''
WavePrecision = WavePrecision.WavePrecision(waves)
print(WavePrecision.compareWavelete())

km1.fitDefault(waves)
km1.paintAll(2,2)
km1.fitByCourse(waves)
km1.paintAll(2,2)
km1.fitByCourseValue(waves)
km1.paintAll(2,2)
'''

end = time.time()
print(end - start)
    