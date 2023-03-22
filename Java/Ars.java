import java.util.Scanner;
class Ars{

	void array(){
	     int sum=0;
	     Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
	     int x[]=new int[n];
	     for(int i=0;i<n;i++){
		x[i]=sc.nextInt();
		sum+=x[i];
	     }
		System.out.println(sum);
		
	}
	public static void main(String a[]){
             
	     Ars ob = new Ars();
	     ob.array();
	     
	     
	}
}