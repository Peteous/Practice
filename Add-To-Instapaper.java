import java.net.URL
import java.util.Scanner;
import urlEncode;

private String apiURL = "https://www.instapaper.com/api/add";
private String[] paramNames = ["username","password"];
private String[] paramData = ["username@example.com","Example_Password_1"]

public static void main(String[] args){
	Scanner scan = new Scanner();
	urlEncode url = new urlEncode();
	input = scan.nextLine();
	if(input.contains("http")){
		actionURL = url.urlEncode(input,apiURL,paramNames,paramData);
		URL site = new URL(actionURL);
		success = site.getContent();
	} else {
		System.out.println("Your entry did not contain a url");
	}
}
