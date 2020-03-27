#include<bits/stdc++.h>
#define pi 3.1415926

using namespace std;

double f(int index ,double x)
{
	switch(index){
		case 0:
			return log(8.3+3*x*cos(2*x))/log(exp(1));
			// return 3/(x-2);
		case 1:
			return log(x*cos(2*x)+2.8)/sin(x) * log(exp(1));
		case 2:	
			return cos(18*x)-exp(x*x)+3.5;
		case 3:
			return exp(cos(x)) + cos(x)-2;
	}
	return 0 ;
}

int main()
{
	//init
	int l[4] = {-10,-5,-10,0};
	int r[4] = {4,5,10,10};
	string fx[4] = {"exp(x) - 3*x*cos(2*x) - 8.3","exp(x*sin(x)) - x*cos(2*x) - 2.8","cos(18*x)-exp(x*x)+3.5","exp(x) + cos(x)-2"};
	double epsilon[2] = {0.00000001,0.0000000001};
	int index_f,index_e ; 
	//

	// for(int index_f = 0 ; index_f < 1 ; index_f++)
	{
		index_f = 3;
		
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
				if(f(index_f,i) == 0)
				{
					printf("%.12lf\n",i);
					continue;
				}
				double x=i;
				double old_x = f(index_f,x);
				// printf("x = %.12lf, old_x = %.12lf\n",x,old_x);
				int time = 0;
				int flag = 0;

				// printf("~~~~~~~~~~~~~~~~~\n");
				while(abs(x - old_x) > epsilon[index_e]) 
				{
					time ++;

					old_x = x;
					x =  f(index_f,x);

						// printf("x = %.12lf, old_x = %.12lf\n",x,old_x);
					if(time > 10000)
					{
						flag = 1;
						break;
					}
				}

				// printf("~~~~~~~~~~~~~~~~~\n");

				printf("time = %d\n",time);
				if(flag == 0)
				{
					printf("%.12lf , time = %d\n",old_x,time);
				}
				
			}
			printf("\n---------------------\n");
		}
			
		
	}

	return 0 ;
}
