#!/usr/bin/python3

import re
                
def calc(A,B):
        ai = str(A)
        bi = str(B)

        p = re.compile(r'^[1-9]\d{0,2}$')

        if not (p.match(ai) and p.match(bi)):
                return -1

        return int(ai) * int(bi)
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
