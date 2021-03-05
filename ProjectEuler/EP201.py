def main():
	#define
	N = 100
	K = 50
	num = [a*a for a in range(1,N+1)]
	#initial
	dp=[]
	for i in range(N+1):
		t = []
		for j in range(N+1):
			t.append({})
		dp.append(t)
	dp[1][0] = {0:1}
	dp[1][1] = {num[0]:1}
	#dp
	for i in range(2,N+1):
		for j in range(0,i+1):
			if N-i+j < K:continue
			if j > K:break
			dp[i][j] = dp[i-1][j].copy()
			for key in dp[i-1][j-1]:
				if key+num[i-1] not in dp[i][j]:
					dp[i][j][key+num[i-1]] = dp[i-1][j-1][key]
				else:
					dp[i][j][key+num[i-1]] += dp[i-1][j-1][key]
		tmp = dp[i-1]
		dp[i-1] = {}
		del tmp
	#outputs
	print (sum(key for key in dp[N][K] if dp[N][K][key] == 1))

if __name__ == '__main__':
	main()
