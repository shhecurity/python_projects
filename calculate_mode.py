from collections import Counter

def calculate_mode(input):
    #compute the mode of a list of values enter by user
    #create a new empty dict
    results=[]
    counts=Counter(input)
    print(counts)
    countdict=dict(counts)
    print(countdict)
    largest= max(countdict.values())
    for i in countdict:
        if countdict[i]== largest:
            results.append(i)
            return results
        print('results:',results)   

            
            
        
        

            
    
        #find the key in the dict with the largest value
        #List the keys that have a value that is the largest
        #display message if no values entered
    
    
#   java code works besides returns int as string  

# const calculateMode = (list) => {
#   let occurences = {}
#   for (let i = 0; i< list.length; i++){
#     if (list[i] in occurences){
#       occurences[list[i]] += 1
#     } else {
#       occurences[list[i]]=1
#     }
#   }
#   let keys = Object.keys(occurences)
#   let results = []
#   let maxValue = 0
#   for (key of keys){
  
#     if (occurences[key] > maxValue){
#     maxValue = occurences[key]
#     results = []
#     results.push(key)
#   } else if (occurences[key]== maxValue){
#     results.push(key)
#     }
#   }
#   return results
# }
#    ___________________________________________end of java funct____________________________________________//
    # res = statistics.multimode(input) 
    # return res
    
    
    # results=[]
    # counts = Counter(input)
    # maxcount = max(counts.values())
    # for i,count in counts:
    #     if count == maxcount:
    #         results.append[i]
    

calculate_mode([1,1,2,2])



   # Multimode of List
# using loop + formula 
    # res = []
    # counted_list = Counter(input) 
    # temp = counted_list.most_common(1)[0][1] 
    # for ele in input:
    #     if input.count(ele) == temp:
    #         res.append(ele)
    #     res = list(set(res))
        
