#include <bits/stdc++.h>

using namespace std;

int main()
{
	int times;
	cin >> times;
	getchar();
	int len[26],max=0;
	for(int i=0;i<26;i++)
	{
		len[i] = 0;
	}
	while(times--)
	{
		string line;
		getline(cin,line);
		// cout << line << endl;
		for(int i=0;i<line.length();i++)
		{
			if(line[i] > 64 && line[i] < 91)
			{
				len[line[i] - 65]++;
			}
			else if(line[i] > 96 && line[i] < 123)
			{
				len[line[i] - 97]++;
			}
			else continue;
			int tmp = len[i];
			if(tmp > max)
			{
				max = tmp;
			}
		}

	}

	while(max > 0)
	{
		for(int i=0;i<26;i++)
		{
			if(len[i] == max)
			{
				cout << char(i+65) << " " << len[i] << endl;
			}
		}
		max--;
	}
		
}