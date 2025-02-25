class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(exp):
            sign,i,const,coeff = 1,0,0,0
            while i<len(exp):
                if exp[i]=='+':
                    sign = 1
                    i+=1
                elif exp[i]=='-':
                    sign = -1
                    i+=1
                else:
                    j = i
                    while j<len(exp) and (exp[j].isdigit() or exp[j]=='x'):
                        j+=1
                    term = exp[i:j]
                    if 'x' in term:
                        val = term[:-1]
                        coeff += sign*(int(val) if val else 1)
                    else:
                        const += sign*int(term)
                    i = j
            return const,coeff
        lhs,rhs = equation.split(\=\)
        lconst,lcoeff = parse(lhs)
        rconst,rcoeff = parse(rhs)
        xcoeff = lcoeff-rcoeff
        constdiff = rconst-lconst
        if xcoeff==0:
            return \Infinite solutions\ if constdiff==0 else \No solution\
        return f'x={constdiff//xcoeff}'