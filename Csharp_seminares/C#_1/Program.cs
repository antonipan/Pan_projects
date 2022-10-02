// Задание №2. 

Console.Clear();
Console.WriteLine("Это задание №2");

Console.WriteLine("Введите любое целое число");
int a = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("и ещё одно");
int b = Convert.ToInt32(Console.ReadLine());

if (a>b) {
    Console.WriteLine($"Это минимальное: {b}, а это максимальное: {a}");
} 
else {
    Console.WriteLine($"Это минимальное: {a}, а это максимальное: {b}");
}


// Задание №4

Console.WriteLine("Это задание №4");
Console.WriteLine("Введите любое целое число");
int num1 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("и ещё одно");
int num2 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("и последнее");
int num3 = Convert.ToInt32(Console.ReadLine());
int max = num1;
if (num1 > max) max = num1;
if (num2 > max) max = num2;
if (num3 > max) max = num3;
Console.WriteLine($"Это максимальное: {max}");


// Задание №6. 

Console.WriteLine("Это задание №6");

Console.WriteLine("Введите любое целое число");
int x = Convert.ToInt32(Console.ReadLine());

int y = x%2;
if (y == 0) {
    Console.WriteLine($"Ура! Это число делится на ДВА: {x} ");

} else
Console.WriteLine($" УПС! число {x} не делится на два(((");



// Задание №8. 

Console.WriteLine("Это задание №8");

Console.WriteLine("Введите любое целое пложительное число");
int N = Convert.ToInt32(Console.ReadLine());

int count = 1;

while (count<=N) 
{
    int number = count % 2;
  
    count++;
}


