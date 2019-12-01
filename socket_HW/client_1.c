#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<sys/types.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<sys/socket.h>


#define server_IP "192.168.56.1"
#define target_PORT 4444


void connect_to_server(char *ip,int port,int socketfd)
{
	struct sockaddr_in info;
	//初始化，將struct涵蓋的bits設為0  
	bzero(&info,sizeof(info));
	//BSD是AF, POSIX是PF  
	//sockaddr_in為Ipv4結構  

	info.sin_family = PF_INET;
	//IP address setting
	info.sin_addr.s_addr = inet_addr(ip);
	//將port(int)轉換成port(network_short_int
	info.sin_port = htons(port);

	int error = connect(socketfd,(struct sockaddr *)&info,sizeof(info));
	
	if(error == -1)
	{
		printf("connect error\n");
	}
	else
	{	
		printf("connect seccess\n");
	}
}	

void get_file(char *FILENAME, int socketid)
{
	int len = 0;
	//接收資訊buffer
	char text[500];
	printf("Read data from server\n");

	recv(socketid,text,sizeof(text),0);	

	FILE *fp = fopen(FILENAME,"w");

	fprintf(fp,"%s",text);
	close(socketid);
	fclose(fp);
	
}
int main(){
	//create a client
	int socket_ = 0;
	socket_ = socket(AF_INET,SOCK_STREAM,0);
	
	if(socket_==-1)
	{
		printf("build failed\n");
	}
	else
	{
		printf("build success\n");
	}
	//socket的連線
	connect_to_server(server_IP,target_PORT,socket_);
	// 從server載檔案 
	get_file("get_1.txt",socket_);

	return 0 ;
}
