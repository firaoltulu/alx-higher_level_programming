#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * main - This Function generate a key
 * depending on a username for crackme5.
 *
 * @argc: number of arguments passed.
 * @argv: arguments passed to main.
 *
 * Return: 0 on success, 1 on error.
 */
int main(int argc, char *argv[])
{
	unsigned int one, two;
	size_t three, four;
	char *five = "A-CHRDw87lNS0E9B2TibgpnMVys5XzvtOGJcYLU+4mjW6fxqZeF3Qa1rPhdKIouk";
	char six[7] = "      ";

	if (argc != 2)
	{
		printf("Correct usage: ./keygen5 username\n");
		return (1);
	}
	else
	{
		three = strlen(argv[1]);
		six[0] = five[(three ^ 59) & 63];

		for (one = 0, four = 0; one < three; one++)
			four += argv[1][one];

		six[1] = five[(four ^ 79) & 63];
		for (one = 0, two = 1; one < three; one++)
			two *= argv[1][one];

		six[2] = five[(two ^ 85) & 63];
		for (two = argv[1][0], one = 0; one < three; one++)
			if ((char)two <= argv[1][one])
				two = argv[1][one];

		srand(two ^ 14);
		six[3] = five[rand() & 63];
		for (two = 0, one = 0; one < three; one++)
			two += argv[1][one] * argv[1][one];

		six[4] = five[(two ^ 239) & 63];
		for (two = 0, one = 0; (char)one < argv[1][0]; one++)
			two = rand();

		six[5] = five[(two ^ 229) & 63];
		printf("%s\n", six);
		return (0);
	}
}
