#area of a circle

import tensorflow as tf
import numpy as np

pi = tf.constant(3.141592654,name='pi')
area = tf.Variable(16*pi,name='x')

randArray = np.random.randint(5,size=50)
#Q2: 5x^2 + 3x +15
functionResultArray = tf.Variable(5*randArray**2+3*randArray+15)

#Q3
#i = tf.Variable(0, name='i')

#Q4
rollingAverage = tf.Variable(0,name='rollingAverage')

model = tf.global_variables_initializer()
with tf.Session() as session:
	writer = tf.summary.FileWriter("output",session.graph)
	session.run(model)
	#Q1
	#print(session.run(area)) # runs JUST the dependencies for area along with itself
	#Q2
	#print(session.run(functionResultArray))

	for n in randArray[3:47]:
		
		rollingAverage = (functionResultArray[n]+functionResultArray[n+1]+functionResultArray[n+2])/3
		print(session.run(rollingAverage))

	print(session.run(functionResultArray))
	writer.close()	
