using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.Text;
using System.Net;
using System.IO;


public class connect : MonoBehaviour
{
	string name,age;
	// string url = "http://140.136.150.92:3000";

	public void name_click(Text aa)
	{
		name = aa.text;
	}

	public void age_click(Text aa)
	{
		age = aa.text;

		Debug.Log("name" + name);
		Debug.Log("age" + age);
		cc();
	}

	public void cc()
	{
		var request = WebRequest.Create("http://140.136.150.92:3000/welcome/user");
		using (var response = request.GetResponse())
		{
		   using (var stream = response.GetResponseStream())
		   {
		      using (var reader = new StreamReader(stream))
		      {
		         var html = reader.ReadToEnd();
		         Debug.Log(html);
		      }
		   }
		}
	}

}
