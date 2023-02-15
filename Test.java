public int findMultipleOfThree(int[] arr)
{
    for (int i = arr.length-1; i > -1; i--){
        if (arr[i] % 3 == 0){
            return arr[i];
        }
    }
}