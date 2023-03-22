import java.util.Scanner;
class Quad{
	void quad(){
	  Scanner sc = new Scanner(System.in);
	  	double a = sc.nextInt();
		double b = sc.nextInt();
		double c = sc.nextInt();
		double d = (b*b)-4*a*c;
		 double w = Math.pow(d, 0.5);
		double r1=(-b+w)/2*a;
		double r2=(-b+w)/2*a;
		if(d>0){
		   System.out.println(r1);
		   System.out.println(r2);			
		}
		else if(d==0){
		   System.out.println(r1);
		}
		else{
			System.out.println("No real root.");
		}
	}
	public static void main(String args[]){
		Quad ob = new Quad();
		ob.quad();
	}
}