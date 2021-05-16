#include <stdio.h>

int main () 
{
	int n, x, n_sub = 0, longest = 0, prev = 0, i; 
	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		prev = x;
		scanf("%d", &x);
		if (x >= prev)
			n_sub += 1;
		else
			n_sub = 1;
		if (n_sub > longest)
			longest = n_sub;
	}
	printf("%d\n", longest);
	return 0;
}