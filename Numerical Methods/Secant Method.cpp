#include<bits/stdc++.h>
#define pi 3.1415926

using namespace std;

double f(int index ,double x)
{
	switch(index){
		case 0:
			return exp(x) - 3*x*cos(2*x) - 8.3;
		case 1:
			return exp(x*sin(x)) - x*cos(2*x) - 2.8;
		case 2:	
			return x*x*cos(18*x)-exp(x*x)+3.5;
		case 3:
			return x * exp(cos(x)) + cos(x)-2;
	}
	return 0 ;
}

int main()
{
	//init
	int l[4] = {-10,-5,-10,0};
	int r[4] = {2,5,10,10};
	string fx[4] = {"exp(x) - 3*x*cos(2*x) - 8.3","exp(x*sin(x)) - x*cos(2*x) - 2.8","cos(18*x)-exp(x*x)+3.5","exp(x) + cos(x)-2"};
	double epsilon[2] = {0.00000001,0.0000000001};
	int index_f,index_e ; 
	//

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

			for(int i=l[index_f] ; i<r[index_f] ; i++)
			{
				double a,b,c;
				if(f(index_f,i) == 0)
				{
					printf("%.12lf\n",i);
					continue;
				}

				if(f(index_f,i)*f(index_f,i+1) < 0)
				{
					int time = 0;
					a = i;
					b = i+1;
					c = (a*f(index_f,b)-b*f(index_f,a))/(f(index_f,b)-f(index_f,a));
				
					while(1){
						time ++;
						

						if(abs(b - a) < epsilon[index_e])
						{
							printf("%.12lf , time = %d\n",b,time);
							break;
						}

						else if(time > 40)
						{
							break;
						}

						a = b;
						b = c;
						c = (a*f(index_f,b)-b*f(index_f,a))/(f(index_f,b)-f(index_f,a));
						
					}
				}

			}
			printf("\n---------------------\n");
		}
			
		
	}

	return 0 ;
}