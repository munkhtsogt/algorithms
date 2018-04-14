
def bubbleSort(d):
	for i in range(0, len(d)):
		for j in range(i + 1, len(d)):
			if d[i]['score'] < d[j]['score']:
				tmp = d[i]
				d[i] = d[j]
				d[j] = tmp
	
	return d

def sorting(arr):
	arr = [10, 9, 1, 2, 3, 4]
	arr.sort(reverse=True)
	print arr

def parser(data):
	'''
	print id, name, grade, score, year in descending order of score
	'''
	d = data['data']
	
	d.sort(key=lambda x: x['score'], reverse=True)
	
	for i in d:
		print i['id'], i['name'], i['grade'], i['score'], i['year']
	

Input = {  
	"data": [  
	    {"id": "a2b", "name": "Chris", "grade": "C", "year": "2015", "score": "78"},  
	    {"id": "c3b", "name": "Allen", "grade": "E", "year": "2016", "score": "58"},  
	    {"id": "dk2", "name": "Sam", "grade": "A", "year": "2017", "score": "95"},
	]  
}
		
parser(Input)
