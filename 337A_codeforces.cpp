#include <stdio.h>
#include <algorithm>
#include <array>

using namespace std;
array<int, 100> a;

int main () 
{
	int n, m;
	scanf("%d", &n);
	scanf("%d", &m);

	for (int i = 0; i < m; i++)
		scanf("%d", &a[i]);

	sort(a.begin(), a.begin() + m);

	// for (int i = 0; i < m; i++)
	// 	printf("%d ", a[i]);
	// printf("\n");

	int d, min;
	for (int i = 0; i < m; i++)
	{
		// printf("%d %d %d %d %d\n", i, i + n - 1, min, a[i], a[i + n - 1]);
		if (i + n - 1 < m)
			d = a[i + n - 1] - a[i];
		if (d < min || i == 0)
			min = d;
	}
	printf("%d\n", min);

	return 0;
}