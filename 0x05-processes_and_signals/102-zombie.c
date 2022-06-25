#include "main.h"

/**
* infinite_while - function that creates an infinite loop.
* Return: Succes.
*/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
* create_zombies - function that creates zombie processes.
* Return: Succes.
*/

int main(void)
{
		int creating_zombies;

	for (creating_zombies = 0; creating_zombies < 6; creating_zombies++)
	{
		if (fork() == 0)
			printf("Zombie process created, PID: %d\n", getpid());
	}
	infinite_while();
	return (0);
}
