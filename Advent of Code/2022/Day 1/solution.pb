OpenConsole() ; Open a console window. 

FileName.s = "input.txt"
File = ReadFile(#PB_Any, FileName)

Global Dim CaloriesPerElf(10000)

If File
    Count = 0
    
    While Eof(File) = 0
        Line.s = ReadString(File)

        If Len(Line) > 0
            CurrentCalories = CurrentCalories + Val(Line)
        Else
            CaloriesPerElf(Count) = CurrentCalories
            CurrentCalories = 0
            Count = Count + 1
        EndIf
    Wend   
Else
    PrintN("Could not open the file: " + FileName)
EndIf

SortArray(CaloriesPerElf(), #PB_Sort_Descending)

Procedure PartOne()
    ProcedureReturn CaloriesPerElf(0)
EndProcedure

Procedure PartTwo()
    ProcedureReturn CaloriesPerElf(0) + CaloriesPerElf(1) + CaloriesPerElf(2)
EndProcedure

PrintN(Str(PartOne()))
PrintN(Str(PartTwo()))
