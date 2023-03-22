import java.util.Scanner;
class This{
	int x,y;
	void f1(int x,int y){
		this.x = x;
                this.y = y;
		
	}
	public static void main(String a[]){
	   This ob = new This();
		ob.f1(2,3);
         System.out.println(ob.x+ob.y);
	}
}