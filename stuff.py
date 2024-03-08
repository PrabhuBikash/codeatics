#print&return
def print_and_return(message):return[print(message),message][1]

#primecalculator
def primes_upto(limit):
    primes = []
    is_prime = [False]*2 + [True]*(limit - 1)
    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            primes.append(number)
            for multiple in range(number*number,limit+1, number):
                is_prime[multiple] = False
    for number in range(int(limit**0.5)+1,limit+1):
        if is_prime[number]:primes.append(number)
    return primes

#sequenceGenerator
def GenerateSequence(formula,last=16,fun=str,var="n"):
  if fun=="print_in_line":fun=print_and_return 
  #place to add new values for fun
  if formula.upper()==("PRIME"or "PRIMES"):return[fun(i) for i in primes_upto(last)]
  formula=formula.replace(var,"n")
  return[fun(eval(formula))for n in range(1,last+1)]

print(GenerateSequence("(-1)**x",var="x"))