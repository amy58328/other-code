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

double df(int index ,double x)
{
	switch(index){
		case 0:
			return exp(x) - 3*cos(2*x) + 6*x*sin(2*x);
		case 1:
			return (sin(x)+x*cos(x))*exp(x*sin(x))- cos(2*x) + 2*x*sin(2*x);
		case 2:	
			return -2*x*exp(x*x) - 18*x*x*sin(18*x) + 2*x*cos(18*x);
		case 3:
			return -sin(x)*exp(cos(x))*x+exp(cos(x)) - sin(x);
	}
	return 0 ;
}

struct node
{
	double x;
	int time;
};

bool rule(node a,node b)
{
	return a.x < b.x;
}
int main()
{
	//init
	int l[4] = {-10,-5,-100,0};
	int r[4] = {2,5,100,10};
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
			
			set<double>s;
			vector<node>t;
			printf("epsilon is %.10lf\n",epsilon[index_e] );
			printf("ans are :\n");

			for(int i=l[index_f] ; i<=r[index_f] ; i++)
			{
				double x = i;
				int time = 0;
				while(1)
				{
					double delta = -(f(index_f,x)/df(index_f,x));

					x = x + delta;
					time++;
					if(abs(delta) < epsilon[index_e])
					{
						
						if(!s.count(x))
						{
							s.insert(x);
							t.push_back((node){x,time});
						}
						break;
					}

					else if(time > 10000)
					{
						break;
					}
				}
			}


			sort(t.begin(),t.end(),rule);
			for(int i=0 ; i<t.size() ; i++)
			{
				printf("%.12lf , time = %d\n",t[i].x,t[i].time );
			}

			printf("\n---------------------\n");
		}
			
		
	}

	return 0 ;
}