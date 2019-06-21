import sys
import urllib.request 
 
 
def main():
     
    #url = req.params.get('URL')
    Ns = str(sys.argv[1])
    #lenghts = req.params.get('lenghts')
 
    #if not url:
    #    url="localhost"
    if not Ns:
        Ns=10
    #if not lenghts:
    #    lenghts=1
 
    N = int(Ns)
    #lenght = int(lenghts)
 
    # return(f"Hello {URL}!")
    my_array=[]
    for i in computepi(N):
        my_array.append(str(i))
    my_array = my_array[:1] + ['.'] + my_array[1:]
    big_string = "".join(my_array)
    # if lenght > 1:
    #    s = url +"&Ns="+str(N)+"&lenghts="+str(lenght-1)+"&URL="+url
    #    contents = urllib.request.urlopen(s).read()
    #print(big_string)
    return big_string 
 
 
 
def computepi(N):
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    counter = 0
    while True:
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
            if counter>N-1:
                break
            else:
                counter=counter+1
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2




if __name__ == "__main__":
   main()


