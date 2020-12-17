#include <iostream>
#include <windows.h>
#include <tchar.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <iomanip>

using namespace std;

bool isPrimeNumber(long long); // Check prime
void PrimElements(long long); // Primitive elements
long FastStep(long, long, long); // Fast step

int _tmain()
{
	// Finding primitive elements in Zp
	cout << "Write p: ";
	long p; cin >> p;
	if (isPrimeNumber(p))
		PrimElements(p);
	else
		cout << "Write the prime number!\n";
	return 0;
}

bool isPrimeNumber(long long num)
{
	bool prost = true;
	for (long long i = 2; i <= num / 2; i++)
	{
		if (num % i == 0)
		{
			prost = false;
			break;
		}
	}
	return prost;
}

long FastStep(long a_val, long t_val, long n_val)
{
	long num = t_val;
	queue<long> Bqueue;
	queue<long> Mqueue;
	// Dec2Bin
	while (true)
	{
		Bqueue.push(t_val);
		Mqueue.push(t_val % 2);
		if (t_val / 2 == 0) break;
		t_val /= 2;
	}
	int row = Bqueue.size();

	// Create a help table
	long **matrix = new long*[row];
	for (int i = 0; i < row; i++)
		matrix[i] = new long[3]{ 0 };

	for (int i = row - 1; i >= 0; i--)
	{
		matrix[i][0] = Bqueue.front();
		matrix[i][1] = Mqueue.front();
		Bqueue.pop(), Mqueue.pop();
	}

	// Calculation m
	matrix[0][2] = a_val;
	long num_before = a_val;
	for (int i = 1; i < row; i++)
	{
		if (matrix[i][1] == 1)
		{
			matrix[i][2] = (num_before * num_before * a_val) % n_val;
			num_before = (num_before * num_before * a_val) % n_val;
		}
		else
		{
			matrix[i][2] = (num_before * num_before) % n_val;
			num_before = (num_before * num_before) % n_val;
		}
	}

	// Delete dynamic memory
	for (int i = 0; i < row; i++)
		delete[] matrix[i];
	delete[] matrix;
	return num_before;
}

void PrimElements(long long p)
{
	// Create table
	long long **table = new long long*[2];
	for (int i = 0; i < 2; i++)
		table[i] = new long long[p - 1]{ 0 };

	// Fill the first row
	for (int i = 0; i < p - 1; i++)
		table[0][i] = i + 1;

	// Search ord(a) and save the second row
	for (int i = 0; i < p - 1; i++)
	{
		long long a = i + 1;
		long long j = 1;
		while (FastStep(a, j, p) != 1) j++;
		table[1][i] = j;
	}

	// Search primitive element
	vector<int> max_p;
	int max = 0;
	for (int i = 0; i < p - 1; i++)
	{
		if (table[1][i] >= max)
			if (table[1][i] != max)
			{
				max = 0; max_p.clear();
				max = table[1][i];
				max_p.push_back(i + 1);
			}
			else
				max_p.push_back(i + 1);
	}

	// Show table
	for (int i = 0; i < 2; i++, cout << endl)
		for (int j = 0; j < p - 1; j++)
			cout << setw(5) << table[i][j];

	// Output primitive elements
	cout << "Primitive elements: ";
	
	while (!max_p.empty())
	{
		cout << max_p.back() << " ";
		max_p.pop_back();
	}
	cout << endl;

	// Delete dynamic memory
	max_p.clear();
	for (int i = 0; i < 2; i++)
		delete[] table[i];
	delete[] table;
}