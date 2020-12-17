#include <iostream>
#include <windows.h>
#include <tchar.h>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <ctime>

using namespace std;

bool isPrimeNumber(long long); // Check prime

vector<long long> prime;
long long EulerFunc(long long, int); // Calculation Euler(Parallel)
long long EulerIteration(long long); // Calculation Euler(Iteration)

// Thread for split loop and mutex
DWORD WINAPI ThreadFactor(LPVOID);
HANDLE Mutex;
struct Data
{
	long long num; // Number
	long long begin; // Left side segment
	long long end; // Right side segment
};

int _tmain()
{
	// Euler
	cout << "Write the number: ";
	long long num; cin >> num;
	cout << "Write the number of intervals: ";
	int k; cin >> k;

	unsigned int start_time = clock(); // Start time
	//cout << "Euler value - " << EulerFunc(num, k) << endl; // Parallel
	cout << "Euler value - " << EulerIteration(num) << endl; // Iteration
	unsigned int end_time = clock(); // End time
	unsigned int search_time = end_time - start_time; // Result time
	cout << search_time / 1000 << "s" << endl;
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

long long EulerFunc(long long n, int k)
// Multithreaded search with reduced intervals
{
	long long result = n;
	if (isPrimeNumber(n))
		result = n - 1;

	Mutex = CreateMutex(NULL, FALSE, NULL);
	HANDLE *ThreadArray = new HANDLE[k];
	Data *DataArray = new Data[k];

	// Split intervals
	long long delta = (n / 2 - 2) / (k - 1);
	for (int i = 0; i < k; i++)
	{
		DataArray[i].num = n;
		DataArray[i].begin = 2 + delta * i;
		DataArray[i].end = 2 + delta * (i + 1);
		ThreadArray[i] = CreateThread(NULL, 0, ThreadFactor, DataArray + i, 0, 0);
	}
	
	// Waiting threads
	WaitForMultipleObjects(k, ThreadArray, TRUE, INFINITE);

	// Close descriptors
	for (int i = 0; i < k; i++)
		CloseHandle(ThreadArray[i]);

	// Find Euler value used prime numbers
	while (!prime.empty())
	{
		long long i = prime.back();
		result *= (1.0 - (1.0 / i));
		prime.pop_back();
	}

	// Delete dynamic memory
	delete[] ThreadArray;
	delete[] DataArray;
	return result;
}

DWORD WINAPI ThreadFactor(LPVOID lpParam)
{
	Data *Argument = (Data*)lpParam;
	long long number = Argument->num, begin = Argument->begin, end = Argument->end;

	for (long long i = begin; i < end; i++)
		if (number % i == 0)
			if (isPrimeNumber(i))
				{
					// Race condition
					WaitForSingleObject(Mutex, INFINITE);
					prime.push_back(i);
					ReleaseMutex(Mutex);
				}
	return 0;
}

long long EulerIteration(long long num)
{
	long long result = num;
	vector <long long> PrimeN;
	// Calculation divisors of a number
	for (int i = 2; i * i <= num; i++)
		if (num % i == 0)
		{
			while (num % i == 0) num /= i;
			PrimeN.push_back(i); // Save number
		}
	// If number is prime
	if (num > 1)
		PrimeN.push_back(num);

	// Calculation Euler used the prime numbers
	while (!PrimeN.empty())
	{
		result *= (1.0 - (1.0 / (double)PrimeN.back()));
		PrimeN.pop_back();
	}
	return result;
}