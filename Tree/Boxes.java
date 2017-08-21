

import java.io.*;
import java.util.*;


/*
10
2 0 2 3 3 4 4 5 5 5
*/
class Box {
  public ArrayList<Integer> children;
  public int parent;
  public int rank;
  public Box() {
    this.children = new ArrayList<>();
  }
  public void ToString(){
  	System.out.println( Arrays.toString(children.toArray()) + " " + parent + " " + rank);
  }
 
}

class Boxes {
	public static void setRank(Box[] boxes, int index, int rank){
		boxes[index].rank = rank;
		for(int i : boxes[index].children){
			setRank(boxes, i - 1, rank + 1);
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(in.readLine()); // number of boxes

		Box[] boxes = new Box[n];
		for (int i = 0; i < n; i++) {
		  boxes[i] = new Box();
		}
		String[] boxesString = in.readLine().split(" "); // input boxes
		for(int i = 0; i < n; i ++){
			int parent = Integer.parseInt(boxesString[i]);
			boxes[i].parent = parent;
			if (parent != 0){
				boxes[parent - 1].children.add(i + 1);
			}
		}
		for(int i = 0; i < n; i ++){
			if (boxes[i].parent == 0){
				setRank(boxes, i, 0);
			}
		}
		// for(int i = 0; i < n; i ++ ){
		// 	boxes[i].ToString();
		// }

		int numtest = Integer.parseInt(in.readLine());
		for(int i = 0; i < numtest; i++){
			int total = 0;
			String[] testBoxes = in.readLine().split(" "); // input boxes
			int current = 0;
			for(int j = 0; j < testBoxes.size(); j++){

			}
		}
	}
}