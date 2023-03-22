import java.util.Scanner;
class Parameter{
	int x,y;
	void show(){
		System.out.println("x="+x+" "+y);
	}
	public static void main(String a[]){
		Parameter ob = new Parameter();
		Scanner sc = new Scanner(System.in);
		 ob.x = sc.nextInt();
		 ob.y = sc.nextInt();
		 ob.show();
	}
}