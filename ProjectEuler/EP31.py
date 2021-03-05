def one_pos( sum, ctr, pos, vals, n ) :
        if pos == n-1: 
                ctr += 1
                return ctr
        else:
                while sum < 200:
                        ctr = one_pos( sum, ctr, pos+1, vals, n )
                        sum += vals[pos]
                if sum == 200:
                        ctr += 1

        return ctr


vals = [ 100, 50, 20, 10, 5, 2, 1 ]
n = len(vals)


ctr = one_pos( 0, 1, 0, vals, n )

print (str(ctr))
