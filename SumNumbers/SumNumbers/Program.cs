using System;

namespace SumNumbers
{
    class Program
    {
        static void Main(string[] args)
        {
            long sum = 0;
            int n = int.Parse(Console.ReadLine());
            for (int i = 0; i < n; i++)
            {
                sum = sum + int.Parse(Console.ReadLine());
            }
            Console.WriteLine("Sum = {0}", sum);
        }
    }
}
