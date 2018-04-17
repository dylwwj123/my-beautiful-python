import os,sys,pickle
class Athlete:
	def __init__(self,a_name,a_dob=None,a_times=[]):
	# __init__ 注意！！！
		self.name = a_name
		self.dob = a_dob
		self.times = a_times
	def top3(self):
		return (sorted(set([sanitize(t) for t in self.times] ) )[0:3] )
	def add_time(self,time_value):
		self.times.append(time_value)
	def add_times(self,list_value):
		self.times.extend(list_value)
		
def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins,secs) = time_string.split(splitter)
	return(mins + '.' + secs)
	
def get_coach_data(filename):
	try:
		with open(filename) as fi:
			data = fi.readline()
			temp = data.strip().split(',')
		return (Athlete(temp.pop(0),temp.pop(0),temp) )
	except IOError as err:
		print('File Error: ' +str(err) )
		return(None) #返回None
sarah = get_coach_data('sarah2.txt')
print(sarah.name + "'s fastest times are:" + str(sarah.top3() ) )
sarah.add_time('1.11')
sarah.add_times(['1.10','0.11','0.01'])
print(sarah.name + "'s fastest times are:" + str(sarah.top3() ) )