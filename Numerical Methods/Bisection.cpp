#include<bits/stdc++.h>

using namespace std;

double f(double x)
{
	//e^x-3xcox2x=8.3
	return exp(x) - 3*x*cos(2*x)-8.3;
	//e^xsinx-xcos2x=2.8
	// return  exp(x*sin(x)) - x*cos(2*x) - 2.8;
}

int main()
{
	int r,l;
	cin >> l >> r;
	double a,b,c;
	double epsilon = 0.0000000001;
	for(int i=l ; i<r ; i++)
	{
		if(f(i) == 0)
		{
			printf("%.12lf\n",i);
			continue;
		}

		if(f(i)*f(i+1) < 0)
		{
			a = i;
			b = i+1;
			while(1){
				c = (a+b)/2;

				if(f(c) == 0)
				{
					// cout << c << endl;
					printf("%.12lf\n",c);
					break;
				}

				if(f(a) * f(c) < 0)
				{
					b=c;
				}
				else
				{
					a=c;
				}

				if(abs(a-b) < 2*epsilon)
				{
					printf("%.12lf\n",c);					
					break;
				}
			}
		}
	}

	return 0 ;
}