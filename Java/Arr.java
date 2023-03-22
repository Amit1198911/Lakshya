//class and objects
import java.util.Scanner;
class Arr{
	public static void main(String a[]){
             int x[]=new int[10];
	     Scanner sc = new Scanner(System.in);
	     
	     for(int i=0;i<10;i++){
		x[i]=sc.nextInt();
	     }
	     for(int i=0;i<10;i++){
		System.out.println(x[i]);
	     }
	     
	}
}