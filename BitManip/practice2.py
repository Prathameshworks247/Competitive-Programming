# max lenght of subarray of 1,2,...N whose And is positive
import math
N = 10
p =  math.floor(math.log(10,2))
p2 = 2**p
pminus= 2**(p-1)
ans = max((p2-pminus),(N-p2))
if N == 1:
    print(1)
else:
    print(ans)
    
#tip:- just make them binary ans observe their binary values thorougly to get thep pattern without panicking 


