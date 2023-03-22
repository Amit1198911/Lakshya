import java.util.Scanner;
class TF{
	int x=1,y=99;
	public int display(int x,int y){
		System.out.println(x+y);
		return 0;
		
	}
	public double display(double x,double y){
	       this.display(3,6);
		System.out.println(x+y);
              //System.out.println(this.x+this.y);
		return 0;
	}
	public static void main(String a[]){
	   TF t = new TF();
		t.display(22.2,52.1);
	   
	}
}