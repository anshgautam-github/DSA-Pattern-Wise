# ❓ Problem : Check if an array is sorted (either entirely increasing or decreasing).

public boolean isSorted(int[] arr) {
    boolean inc = true, dec = true;

    for (int i = 0; i < arr.length - 1; i++) {
        if (arr[i] > arr[i + 1]) inc = false;
        if (arr[i] < arr[i + 1]) dec = false;

        if (!inc && !dec) return false;
    }
    return true;
}



TC : O(n)
SC : O(1)
