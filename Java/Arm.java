
class Arm{
	public static void main(String args[]){
          int temp=8208,a=8208,c=0,r=0,s=0;
	for(int i=0;i<4;i++){
		r=a%10;
		s+=r*r*r*r;
		a=a/10;
	
	}
	if(s==temp){
		System.out.println("Yes");
	}
	else{
		System.out.println("No");
	}
	

	}
}