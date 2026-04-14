# Check if Array is Strictly Increasing OR Constant  : Return true if array is: strictly increasing OR all elements equal

public boolean checkArray(int[] arr) {
    boolean increasing = true;
    boolean constant = true;

    for (int i = 0; i < arr.length - 1; i++) {
        if (arr[i] >= arr[i + 1]) increasing = false;
        if (arr[i] != arr[i + 1]) constant = false;
    }

    return increasing || constant;
}
