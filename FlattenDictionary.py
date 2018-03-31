def helper(flattenDic, key, dic):
  
  for k in dic.keys():
      key = key + "." + k
      if type(dic[k]) is dict:
        helper(flattenDic, key, dic[k])    
      else:
        flattenDic[key] = dic[k] 
          
  

def flatten_dictionary(dictionary):
  #pass # your code goes here
  flattenDic = {}
  for key in dictionary.keys():
      if type(dictionary[key]) is dict:
        helper(flattenDic, key, dictionary[key])  
      else:
        flattenDic[key] = dictionary[key] 
            
  return flattenDic

dic = {
    "Key1" : "1",
    "Key2" : {
        "a" : "2",
        "b" : "3",
        "c" : {
            "d" : "3",
            "e" : {
                "" : "1"
            }
        }
    }
}

print flatten_dictionary(dic)



