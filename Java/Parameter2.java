import java.util.*;
class Parameter2{
	int x,y;
	Scanner sc = new Scanner(System.in);
	void show(){
		System.out.println("x="+x+" "+y);
	}

	public static void main(String a[]){
		Parameter2 ob = new Parameter2();
		 ob.x = ob.sc.nextInt();
		 ob.y = ob.sc.nextInt();
		 ob.show();
	}
}