N = int(input())
d_sum=0
d_max=0

for i in range(0,N):
	d = int(input())
	d_sum += d
	d_max = max(d_max, d)

print(d_sum)

if d_max > d_sum - d_max :
	print(d_max-(d_sum-d_max))
else:
	print(0)