import java.io.*;

import java.net.*;

public class server{
	public static void main(String[] args) throws Exception{

		File file = new File("deliver_file.txt");

		int port = 4444;

		System.out.println("waiting for client connect");
		// create server
		ServerSocket ss = new ServerSocket(port);

		// connect client
		Socket client = ss.accept();
		System.out.println("Client connect success");

		// 數據封裝
		System.out.println("ready to deliver th file");
		OutputStream netOut = client.getOutputStream();

		OutputStream temp = new DataOutputStream(new BufferedOutputStream(netOut));

		// 建立緩衝區
		System.out.println("start deliver the file");
		byte[] buf = new byte[2048];

		FileInputStream fos = new FileInputStream(file);
		int num = fos.read(buf);


		while(num != -1)
		{
			temp.write(buf,0,num);// 把檔案寫到緩衝區內
			temp.flush();// 寫往客戶端
			num = fos.read(buf);
		}

		System.out.println("file deliver success");
		fos.close();
		temp.close();
	}
}