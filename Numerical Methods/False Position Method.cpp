#include<bits/stdc++.h>
#define pi 3.1415926

using namespace std;

// 0. exp(x) - 3*x*cos(2*x) - 8.3, (-10,2)
// 1. exp(x*sin(x)) - x*cos(2*x) - 2.8, (-5,5)

double f(int index ,double x)
{
	switch(index){
		case 0:
			return exp(x) - 3*x*cos(2*x) - 8.3;
		case 1:
			return exp(x*sin(x)) - x*cos(2*x) - 2.8;
		case 2:	
			return 18*cos(2*x/pi) - sqrt(2)*sin(3*x*x/pi);
		case 3:
			return exp(cos(x)) + cos(x)-2;
	}
	return 0 ;
}

int main()
{
	// init
	int l[4] = {-10,-5,-10,0};
	int r[4] = {2,5,10,10};
	string fx[4] = {"exp(x) - 3*x*cos(2*x) - 8.3","exp(x*sin(x)) - x*cos(2*x) - 2.8","18*cos(2*x/pi) - sqrt(2)*sin(3*x*x/pi)","exp(cos(x)) + cos(x)-2"};
	double epsilon[2] = {0.00000001,0.0000000001};
	int index_f,index_e ; 

	for(int index_f = 0 ; index_f < 4 ; index_f++)
	{
		printf("%d",index_f+1);
		printf("\n----------------------------------\n");
		printf("f(x) = ");
		cout << fx[index_f] << endl;
		printf("range is[%d,%d]\n",l[index_f],r[index_f] );

		for(int index_e = 0 ; index_e <2;index_e++)
		{
			printf("epsilon is %.10lf\n",epsilon[index_e] );
			printf("ans are :\n");

			for(int i=l[index_f] ; i <= r[index_f] ; i++)
			{
				if(f(index_f,i) == 0 )
				{
					cout << i << endl;
					continue;
				}

				double old_c = 0;

				if(i != r[index_f] && f(index_f,i)*f(index_f,i+1) < 0)
				{
					double a = i;
					double b = i+1;
					double c = (a*f(index_f,b) - b*f(index_f,a))/(f(index_f,b)-f(index_f,a));
					int time = 0;
					while(1)
					{
						time ++;
						if(f(index_f,a) * f(index_f,c) < 0 )
							b = c;
						else
							a = c; 

						if(abs(old_c - c) < epsilon[index_e])
						{
							printf("%.12lf , time = %d \n",c,time);
							break;
						}

						
						old_c = c;
						c = (a*f(index_f,b) - b*f(index_f,a))/(f(index_f,b)-f(index_f,a));
					}
				}
				// printf("f(%d) = %.12lf\n",i,f(i) );
			}
			printf("\n---------------------\n");
		}
			
	}

	
	return 0 ;
}