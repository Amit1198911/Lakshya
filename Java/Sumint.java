import java.util.Scanner;
class Sumint{
	void sum_int(){
			Scanner sc = new Scanner(System.in);
			int n=sc.nextInt();
			int r=0;
			int sum=0;
			while(n!=0){
				r=n%10;
				sum+=r;
				n/=10;
			}
			System.out.println("Sum : "+sum);
		}
	public static void main(String a[]){
		Sumint ob = new Sumint();
		ob.sum_int();
		

	}
	
}