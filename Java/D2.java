import java.util.Scanner;
class D2{
	public static void main(String a[]){
             int x[][]=new int[3][3];
	     Scanner sc = new Scanner(System.in);
	     
	     for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
		  x[i][j]=sc.nextInt();

		}
	     }
		System.out.println();
	    
	     for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
		  System.out.print(x[i][j]+" ");
		}
		System.out.println(" ");
	     }
	     
	}
}