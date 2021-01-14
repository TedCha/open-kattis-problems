using System;
using System.Collections.Generic;

public class finalexam2
{
    public static void Main (string[] args)
    {
        int NumOfQuestions = int.Parse(Console.ReadLine());
        int Range = NumOfQuestions - 1;
        int count = 0;

        List<string> Answers = new List<string>();

        for (int i = 0; i < NumOfQuestions; i++)
        {
            Answers.Add(Console.ReadLine());
        }

        List<string> Responses = Answers.GetRange(1, Range);
        Responses.Add("X");

        for (int i = 0; i < NumOfQuestions; i++)
        {
            if (Answers[i] == Responses[i])
            {
                count += 1;
            }
        }

        Console.WriteLine(count);
    }
}