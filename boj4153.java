import java.util.Scanner;

public class boj4153 {

	private static void rightTriangle(int []arr) {
		int triangle=arr[2]*arr[2];
		int side1=arr[0]*arr[0];
		int side2=arr[1]*arr[1];
		if(triangle==side1+side2) {
			System.out.println("right");
		}
		else {
			System.out.println("wrong");
		}
	}
	private static int[] bubbleSort(int []arr) {
		int tmp;
		
		for(int i=0;i<arr.length;i++) {
			for(int j=0;j<arr.length-i-1;j++) {
				if(arr[j]>arr[j+1]) {
					tmp=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=tmp;
				}
			}
		}
		return arr;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner=new Scanner(System.in);
		int [] a=new int[3];
		int maxindex;
		while(true) {
			for(int i=0;i<a.length;i++) {
				a[i]=scanner.nextInt();
				if(a[0]==0&&a[1]==0&&a[2]==0) System.exit(0);
			}
			bubbleSort(a);
			rightTriangle(a);
		}
	}

}
