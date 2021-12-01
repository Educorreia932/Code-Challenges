with Ada.Text_IO; use Ada.Text_IO;

procedure Main is
    type Integer_Array is array (0..2000) of Integer;

	File            : File_Type;
    Input           : Integer_Array;
    I               : Natural := 1;

    function Part_1 return Natural is
	    Result   : Natural := 0;
        Previous : Integer := 2147483647;
    begin
        for I in 0..1997 loop
            declare
                N : Integer := Input(I);
            begin
                if N > Previous then
                    Result := Result + 1;
                end if;

                Previous := N;
            end;
        end loop;

        return Result;
    end;

    function Part_2 return Natural is
        Result          : Natural := 0;
        Previous_Window : Integer := 2147483647;
    begin
        for I in 0..1997 loop
            declare
                Current_Window : Integer := 0;
            begin
                for J in 1..3 loop
                    Current_Window := Current_Window + Input(I + J);
                end loop;

                if Current_Window > Previous_Window then
                    Result := Result + 1;
                end if;

                Previous_Window := Current_Window;
            end;
        end loop;

        return Result;
    end;
begin
    Open (File, In_File, "input.txt");

    -- Read input file into an array
	while not End_Of_File (File) loop
		declare
			N : Integer := Integer'Value (Get_Line (File));
		begin
            Input(I) := N;
            I := I + 1;
		end;
	end loop;

    Put_Line("Part 1: " & Part_1'Image);
    Put_Line("Part 2: " & Part_2'Image);
end; & Part_1'Image);
    Put_Line("Part 2: " & Part_2'Image);
end;