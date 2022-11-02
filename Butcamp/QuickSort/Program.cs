Console.Clear();
// Алгоритм быстрой сортировки...
/* Console.WriteLine("Введите кол-во элементов массива:");
int n = Convert.ToInt32(Console.ReadLine());
// Заполнение массива
int[] array = new int[n];
for (int i = 0; i < n; i++)
{
    Console.Write("Введите число: ");
    array[i] = Convert.ToInt32(Console.ReadLine());
}
Console.WriteLine();
Console.WriteLine("Начальный массив: [" + string.Join(", ", array) + "]");
// Cортировка
for (int i = 0; i < n - 1; i++)
{
    int MinIndex = i;
    for (int j = i + 1; j < n; j++)
    {
        if (array[j] < array[MinIndex])
            MinIndex = j; 
    }
    int temp;
    temp = array[MinIndex];
    array[MinIndex] = array[i];
    array[i] = temp;
}
Console.WriteLine("Конечный массив: [" + string.Join(", ", array) + "]"); */

/* Console.WriteLine("Hello, World!");
string[] array1 = new string[5];
for (int i = 0; i < 5; i++)
{
    array1[i] = Console.ReadLine();
}
Console.WriteLine();
Console.Write("[" + string.Join(", ", array1) + "]");
for (int i = 0; i < 4; i++)
{
    int MinIndex = i;
    for (int j = i + 1; j < 5; j++)
    {
        if (array1[j].Length < array1[MinIndex].Length)
            MinIndex = j; 
    }
    string temp;
    temp = array1[MinIndex];
    array1[MinIndex] = array1[i];
    array1[i] = temp;
}
Console.WriteLine();
Console.WriteLine("Конечный массив: [" + string.Join(", ", array1) + "]"); */

/* Console.WriteLine("Введите размер массива");
int n = Convert.ToInt32(Console.ReadLine());
int[] a = new int[n];
int[] b = new int[n];
for (int i = 0; i < n; i++)
    {
        a[i] = Convert.ToInt32(Console.ReadLine());
    }
Console.WriteLine("Введите К");
int k = Convert.ToInt32(Console.ReadLine());
k = 5
;
if (k > 0)
    {
    for (int i = 0; i <= k; i++)
        b[i] = a[n - k + i];
    for (int i = 0; i < n - k; i++)
        b[k + i] = a[i];
    for (int i = 0; i < n; i++)
        Console.Write(b[i] + " ");
    }
else
    {
    k = -k;
    for (int i = 0; i < k; i++)
        b[n - k + i] = a[i];
    for (int i = 0; i < n - k; i++)
        b[i] = a[k + i];
    for (int i = 0; i < n; i++)
        Console.Write(b[i] + " ");
    } */

    /*
Cортировка пузырьком
Начальный массив: [3, 1, 5, 0, 7, 9, 8]
*/
/* Console.WriteLine("Введите кол-во элементов массива: ");
int n = Convert.ToInt32(Console.ReadLine());
int[] array = new int[n];
for (int i = 0; i < n; i++)
{
    Console.Write("Введите значения массива: ");
    array[i] = Convert.ToInt32(Console.ReadLine());
}
Console.WriteLine("Начальный массив: [" + string.Join(", ", array) + "]");
Console.WriteLine();
for (int i = 0; i < n; i++)
{
    for (int j = 0; j < n-1; j++)
    {
        if (array[j] > array[j + 1])
        {
            int temp = array[j];
            array[j] = array[j + 1];
            array[j + 1] = temp;
        }
        Console.WriteLine((i+1) + " [" + string.Join(", ", array) + "]");
    }
} */

/* Console.WriteLine("Введите кол-во элементов массива: ");
int n = Convert.ToInt32(Console.ReadLine());
int [] array = new int [n];
for (int i = 0; i < n; i++)
{
    Console.Write("Введите элемент: ");
    array[i] = Convert.ToInt32(Console.ReadLine());
}
Console.WriteLine("Начальный массив: [" + string.Join(", ", array) + "]");

for (int i = 0; i < n; i++)
{
    for (int j = 0; j < n - 1; j++)
    {
        if (array[j] > array [j + 1])
        {
            int temp;
            temp = array[j];
            array[j] = array[j+1];
            array[j+1] = temp;
        }
        Console.WriteLine((i + 1) + "Промежуточный массив: [" + string.Join(", ", array) + "]");
    }
} */


// Быстрая сортировка

int [] arr = {0, -5, 2, 3, 5, 9, -1, 7};
QuickSort(arr, 0, arr.Length - 1);
Console.Write($"Отсортированный массив - это: {string.Join(", ", arr)}");


int [] QuickSort(int [] inputArray, int minIndex, int maxIndex)
{
    if (minIndex >= maxIndex) return null;
    int pivot = GetPivotIndex (inputArray, minIndex, maxIndex);
    QuickSort(inputArray, minIndex, pivot - 1);
    QuickSort(inputArray, pivot+1, maxIndex);
    return inputArray;
}

int GetPivotIndex (int [] inputArray, int minIndex, int maxIndex)
{
    int pivotIndex = minIndex-1; 
    for (int i = minIndex; i <= maxIndex; i++)
    {
        if (inputArray[i] < inputArray[maxIndex])
        {
            pivotIndex++;
            Swap(inputArray, i, pivotIndex);
        }
    }
    pivotIndex++;
    Swap(inputArray, pivotIndex, maxIndex);
    return pivotIndex;
}
// 
void Swap(int [] inputArray, int leftValue, int rightValue)
{
    int temp = inputArray [leftValue];
    inputArray [leftValue] = inputArray [rightValue];
    inputArray [rightValue] = temp;
}