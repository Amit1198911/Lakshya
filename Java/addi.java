import java.util.Scanner;
class addi{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int o = sc.nextInt();
		int p = sc.nextInt();
		int q = sc.nextInt();
		int r = sc.nextInt();
		 int a[][] = new int[n][m];
		 int b[][] = new int[o][p];
		 int b[][] = new int[o][p];
		int sum=0;

		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				a[i][j]=sc.nextInt();
			}
		}
    		for(int i=0;i<o;i++){		
		 for(int j=0;j<p;j++){
				a[o][p]=sc.nextInt();
			}       
		}

		
                 

		
		System.out.println(sum);
	}
}