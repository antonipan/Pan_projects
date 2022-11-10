Console.Clear();

Console.WriteLine("Сколько строк вы хотите проверить?");
int num = Convert.ToInt32(Console.ReadLine());
string [] line = new string [num];
for (int i = 0; i < num; i++)
{
    Console.WriteLine($"Введите {i+1}-ую строку");
    line [i] = Convert.ToString(Console.ReadLine());
}


string [] CheckArray (string [] array)
{
    int sizeOutArray = 0;
    for (int i = 0; i < array.Length; i++)
    {
        int size = array [i].Length;
        if (size < 4) 
        {
            sizeOutArray++;
        }
    }

    string [] arrayOut = new string [sizeOutArray];
    int index = 0;
    for (int i = 0; i < array.Length; i++)
    {
        int size = array [i].Length;
        if (size < 4) 
        {
            arrayOut[index] = array[i];
            index++;
        }
    }


    return arrayOut;
}

string [] mass = CheckArray(line);
Console.Write(string.Join(", ", mass));
