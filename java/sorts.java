//Doing the sorting algorithms in hava

import java.util.List;
import java.util.Arrays;

public class sorts{

    /*
    Implement mergesort recursively in java! As a refersher on how java works.
    */

    public static int[] mergeSort (int[] array){
        int[] newArray = new int [array.length];
        if (array.length > 1){
            int mid = (array.length) / 2;
            int[] leftarray = Arrays.copyOfRange(array, 0, mid);
            int[] rightarray = Arrays.copyOfRange(array,mid,array.length);

            int[] newLeft = mergeSort(leftarray);
            int[] newRight = mergeSort(rightarray);

            int i = 0;
            int j = 0;
            int k = 0;

            while ( i < newLeft.length && j < newRight.length){
                if (newLeft[i] <= newRight[j]){
                    newArray[k] = newLeft[i];
                    i++;
                }
                else {
                    newArray[k] = newRight[j];
                    j++;
                }
                k++;
            }
            while ( i < newLeft.length){
                newArray[k] = newLeft[i];
                i++;
                k++;
            }
            while (j < newRight.length){
                newArray[k] = newRight[j];
                j++;
                k++;
            }
            return newArray;
        }
        return array;
    }

    public static void quickSort(int[] array, int low, int high){
        if (low < high){
            int partitionIndex = partition(array, low, high);
            
            quickSort(array,low,partitionIndex-1);
            quickSort(array,partitionIndex+1,high);
        }
    }
    
    public static int partition(int[] array, int low, int high){

        int pivotvalue = array[high];
        int i = low - 1;

        for (int j=low; j<high; j++){
            if (array[j]<=pivotvalue){
                i++;
                //swap the two values
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        int temp2 = array[i + 1];
        array[i + 1] = array[high];
        array[high] = temp2;

        return i+1;
    }

    public static void bubbleSort(int[] array){
        //java bubblesort without sort helper function
        for (int j = array.length -1; j> 0; j--){
            for (int i = 0; i<j; i++){
                if (array[i]> array[i+1]){
                    int temp = array[i];
                    array[i] = array[i+1];
                    array[i+1] = temp;
                }
            }
        }
    }

    public static void main(String[] args){
        int[] myArray = {10, 29, 99,34, 42, 9, 22, 19, 100};
        System.out.println("Prior to mergeSort" + Arrays.toString(myArray));
        System.out.println(Arrays.toString(mergeSort(myArray)));
        int[] myArray2 = {10, 29, 99,34, 42, 9, 22, 19, 100};
        System.out.println("Prior to quickSort:" + Arrays.toString(myArray2));
        quickSort(myArray2, 0, myArray2.length - 1);
        System.out.println(Arrays.toString(myArray2));

        System.out.println("Starting bubble sort");
        int[] myArray3 = {10, 19, 82, 14, 100, 99, 24, 84, 16, 34};
        System.out.println(Arrays.toString(myArray3));
        bubbleSort(myArray3);
        System.out.println(Arrays.toString(myArray3));
    }
}
