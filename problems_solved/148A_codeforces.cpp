#include <stdio.h>

int mark[120000], action[4], dragons;

int main ()
{
	for (int i = 0; i < 4; i++)
		scanf("%d", &action[i]);
	scanf("%d", &dragons);
	for (int i = 0; i < 4; i++)
	{
		for (int j = action[i]; j <= dragons; j += action[i])
			mark[j] = 1;
	}
	int count = 0;
	for (int i = 1; i <= dragons; i++)
		if (mark[i] == 1)
			count += 1;
	printf("%d\n", count);
	return 0;
}